# -*- coding: utf-8 -*-
"""
ANÁLISIS TAREA CONTROL
@author: David Bestue | Open Brains
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import signal
from scipy.signal import spectrogram



##### CASOS DE ÉXITO:
#parpadeo: 
#out_file = 'ssvep_raw_20260130_095132.csv'
#vmin_val=20, vmax_val=80, F_TARGET = 4.0,

#mover los ojos:
#out_file = 'ssvep_raw_20260130_101048.csv'
#vmin_val=20, vmax_val=80, F_TARGET = 3.0,

##mover el dedo: --> NO LO VEMOS EN FRONTAL
#out_file='ssvep_raw_20260130_103128.csv'



out_file = 'ssvep_raw_20260130_105607.csv'

out_file = 'ssvep_raw_20260130_112745.csv'


out_file = 'ssvep_raw_20260130_113242.csv'


# --- Carga robusta del CSV ---
df = pd.read_csv(out_file)  # usa la ruta que acabas de guardar


# Limpieza mínima
df['value'] = pd.to_numeric(df['value'], errors='coerce')
df = df.dropna(subset=['value']).copy()

############################################# Parámetros ADS1219
VREF = 2.048
GAIN = 4
LSB_uV = (VREF / GAIN) / (2**23) * 1e6  # ≈ 0.061 µV
# Conversión
df['eeg_uV'] = df['value'].astype(np.int64) * LSB_uV
################################################################

# --- estimar fs a partir de timestamps ---
t = df['time_s'].to_numpy()
dt = np.diff(t)
dt = dt[dt > 0]                       # seguridad
fs = 1.0 / np.median(dt)              # Hz

# --- parámetros ---
SAT = 2**23 - 1                       # saturación ADC 24 bits
MAX_GAP_SEC = 0.05                    # 50 ms
MAX_GAP_SAMPLES = int(MAX_GAP_SEC * fs)

# --- marcar saturaciones ---
is_sat = df['value'].abs() >= SAT
df['eeg_uV_clean'] = df['eeg_uV'].copy()
df.loc[is_sat, 'eeg_uV_clean'] = np.nan

# --- interpolar solo huecos cortos ---
df['eeg_uV_clean'] = (
    df['eeg_uV_clean']
    .interpolate(
        method='linear',
        limit=MAX_GAP_SAMPLES,
        limit_direction='both'
    )
)

print(f"fs estimada: {fs:.2f} Hz")
print(f"% muestras saturadas: {100 * is_sat.mean():.2f}%")


######Regla de laboratorio muy conservadora (y bastante estándar):
#< 1 % → perfecto
#1–5 % → aceptable con cuidado
#5–10 % → dudoso
#>10 % → bloque descartado


timestamps = np.array(df['time_s'] )
eeg_signal = np.array(df['eeg_uV_clean'] )
states = np.array(df['state'] )


# --- FILTRAT (Bandpass) ---

#La freqüència de Nyquist és la meitat de la freqüència de mostreig (fs/2) 
#i representa la màxima freqüència que es pot reconstruir fidelment en un senyal digital. 
#Segons el teorema de Nyquist-Shannon, cal almenys dues mostres per cicle per captar correctament una oscil·lació.
#Mirar arxivo de como_el_samping_rate_define_la_maxima_frecuencia_detectable.py

freq_min = 0.01
freq_max = 40

b_band, a_band = signal.butter(2, [freq_min/(fs/2), freq_max/(fs/2)], btype='band')  
# normalitzem les freqüències fent que fs/2 (la freqüència de Nyquist) sigui el valor màxim, equivalent a 1.
# Band pass filter: Filtre pasabanda: filtre que deixa passar les freqüències entre un límit inferior (f_low) i un superior (f_high), bloquejant la resta.
#Indica el rang de freqüències a deixar passar (en aquest cas, de 1 Hz a 40 Hz).

eeg_bandpassed = signal.filtfilt(b_band, a_band, eeg_signal)
plt.figure(figsize=(12, 5))
plt.plot(timestamps, eeg_bandpassed, color='darkblue', alpha=1, linewidth=2)
plt.xlabel("Temps (s)")
plt.ylabel("Amplitud (µV)")
plt.title("Senyal EEG després del Band pass filter")
plt.tight_layout()
plt.show(block=False)




# ===== ESPECTROGRAMA (STFT) para flicker =====
timestamps = np.asarray(timestamps, dtype=float)
states     = np.asarray(states, dtype=str)
x          = np.asarray(eeg_bandpassed, dtype=float)


# --- parámetros STFT ---
# (usa los tuyos si ya los tienes definidos)
F_TARGET = 8.0        # Hz del flicker
NPERSEG_SEC = 2.0      # ventana de 2 s => resolución ~0.5 Hz
OVERLAP = 0.5          # 50% de solapamiento
nperseg = int(round(NPERSEG_SEC * fs))
noverlap = int(round(nperseg * OVERLAP))

# --- espectrograma ---
f, t_rel, Sxx = spectrogram(
    x,
    fs=fs,
    nperseg=nperseg,
    noverlap=noverlap,
    detrend='constant',
    scaling='density',
    mode='psd'
)

Sxx_db = 10*np.log10(Sxx + 1e-18)

# --- tiempo REAL del espectrograma usando timestamps ---
# Paso entre ventanas (en muestras)
step = nperseg - noverlap

# Índices (en muestras) del centro de cada ventana
# SciPy define t_rel en centros; esto replica eso en índices.
center_idx = (np.arange(len(t_rel)) * step + (nperseg / 2.0)).astype(int)
center_idx = np.clip(center_idx, 0, len(timestamps) - 1)

# Tiempo absoluto real por columna del espectrograma
t_spec = timestamps[center_idx]

# --- plot espectrograma ---
plt.figure(figsize=(12, 5))
# vmin_val=20
# vmax_val=80
# plt.pcolormesh(t_spec, f, Sxx_db, shading='gouraud', cmap='jet', vmin=vmin_val, vmax=vmax_val)
plt.pcolormesh(t_spec, f, Sxx_db, shading='gouraud', cmap='jet')

plt.colorbar(label='Potencia (dB)')
plt.xlabel('Tiempo real (s)')
plt.ylabel('Frecuencia (Hz)')

# líneas guía en 12 Hz
#plt.axhline(F_TARGET, color='k', linestyle='--', linewidth=1, alpha=0.8, label=f'{F_TARGET:.0f} Hz')


# bloques
change_idx = np.where(states[1:] != states[:-1])[0] + 1
change_times = timestamps[change_idx]
prev_states = states[change_idx - 1]
new_states = states[change_idx]

# inicio: entra en flicker
flicker_start_times = change_times[new_states == 'flicker']
# final: sale de flicker
flicker_end_times = change_times[prev_states == 'flicker']

for t_evt in flicker_start_times:
    plt.axvline(
        t_evt,
        color='darkred',
        linewidth=1.5,
        linestyle='-',
        alpha=0.9
    )

# final de flicker → línea roja discontinua
for t_evt in flicker_end_times:
    plt.axvline(
        t_evt,
        color='darkred',
        linewidth=0.5,
        linestyle='--',
        alpha=0.9
    )


plt.ylim(freq_min, freq_max)  # si tu bandpass fue 1–40
plt.title('Espectrograma (STFT) ')
plt.tight_layout()

# Esto fuerza a que el eje X vaya hasta el final real del registro
plt.xlim(timestamps[0], timestamps[-1])

plt.show(block=False)


#### Potencial evocado de la señal de EEG flicker vs rest dos lineas con CI cada una durante 10s. 
#### ¿Coger toda la señal del EEG o de la transformada de fourier alrededor d elos 12Hz?¿Qué es más correcto?

# ... (Tu código anterior llega hasta plt.show() del espectrograma) ...

# =============================================================================
# ANÁLISIS DE POTENCIAL EVOCADO (SSVEP AMPLITUDE TIME-COURSE)
# =============================================================================


# 1. Definir parámetros de la ventana de análisis
EPOCH_SEC = 10.0
n_samples_epoch = int(EPOCH_SEC * fs)
t_epoch = np.linspace(0, EPOCH_SEC, n_samples_epoch)

# 2. Crear una señal específica para el análisis de amplitud (Banda Estrecha)
#    Queremos ver la energía EXCLUSIVAMENTE en 12 Hz (+- 1 Hz de margen)
f_narrow_min = F_TARGET - 1.5
f_narrow_max = F_TARGET + 1.5

b_narrow, a_narrow = signal.butter(2, [f_narrow_min/(fs/2), f_narrow_max/(fs/2)], btype='band')
eeg_narrow = signal.filtfilt(b_narrow, a_narrow, eeg_signal)

# 3. Calcular la ENVOLVENTE (Amplitud instantánea) usando Hilbert
#    Esto soluciona el problema de la cancelación de fase.
analytic_signal = signal.hilbert(eeg_narrow)
amplitude_envelope = np.abs(analytic_signal)

# 4. Función para extraer épocas
def get_epochs(start_times, signal_data, n_samples):
    epochs_list = []
    valid_starts = []
    
    for start_t in start_times:
        # Buscar índice más cercano al tiempo de inicio
        idx_start = np.searchsorted(timestamps, start_t)
        idx_end = idx_start + n_samples
        
        # Verificar que no nos salimos del array
        if idx_end <= len(signal_data):
            epoch = signal_data[idx_start:idx_end]
            epochs_list.append(epoch)
            valid_starts.append(start_t)
            
    if not epochs_list:
        return np.array([]), 0
        
    return np.array(epochs_list), len(epochs_list)

# 5. Extraer tiempos de inicio de cada condición
#    (Reusamos la lógica de detección de cambios que ya tenías)
#    flicker_start_times ya lo calculaste arriba
#    Calculamos rest_start_times similarmente:
rest_start_times = change_times[new_states == 'rest']

# Extraer matrices de épocas (N_trials x N_timepoints)
flicker_epochs, n_flicker = get_epochs(flicker_start_times, amplitude_envelope, n_samples_epoch)
rest_epochs, n_rest = get_epochs(rest_start_times, amplitude_envelope, n_samples_epoch)

print(f"Épocas extraídas - Flicker: {n_flicker}, Rest: {n_rest}")

# =============================================================================
# GRAFICAR: 12Hz Amplitude Time-Course
# =============================================================================

plt.figure(figsize=(10, 6))

# Usamos Seaborn para pintar línea + intervalo de confianza (CI) automáticamente
# Necesitamos convertir a DataFrame 'long format' para seaborn, o hacerlo manual.
# Lo haremos manual para mantenerlo ligero sin depender mucho de pandas melting.

def plot_with_ci(time_vec, data_matrix, color, label):
    if data_matrix.size == 0:
        print(f"No hay datos para {label}")
        return
    
    # Media y Desviación Estándar / Error Estándar
    mean_sig = np.mean(data_matrix, axis=0)
    std_sig = np.std(data_matrix, axis=0)
    n_trials = data_matrix.shape[0]
    
    # Intervalo de confianza 95% (1.96 * error estándar)
    ci = 1.96 * (std_sig / np.sqrt(n_trials))
    
    plt.plot(time_vec, mean_sig, color=color, linewidth=2, label=f"{label} (n={n_trials})")
    plt.fill_between(time_vec, mean_sig - ci, mean_sig + ci, color=color, alpha=0.2)

# Plot Flicker
plot_with_ci(t_epoch, flicker_epochs, color='red', label='Flicker (12Hz)')

# Plot Rest
plot_with_ci(t_epoch, rest_epochs, color='gray', label='Rest')

plt.title(f"Evolución de la Amplitud en {F_TARGET} Hz (Hilbert Envelope)")
plt.xlabel("Tiempo desde inicio del bloque (s)")
plt.ylabel("Amplitud (µV)")
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show(block=False)