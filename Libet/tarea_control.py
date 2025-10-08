# -*- coding: utf-8 -*-
"""
TASCA CONTROL
@author: David Bestue | Open Brains
"""




"""
SSVEP 12 Hz test - PsychoPy + numpy
Mostrado de pico a ~12 Hz para validar EEG en Oz.
Autor: Open Brains
"""
import time, math, csv
import numpy as np
from collections import deque
from psychopy import visual, core, event
import serial, serial.tools.list_ports
from datetime import datetime
import os
import threading


# --- DETECCIÓ DEL PORT USB SERIAL ---
puerto = None
baudrate = 230400
ports = serial.tools.list_ports.comports()
for port in ports:
    print(port.device, port.description)
    if 'Arduino' in port.description:     #if 'USB Serial Device' in port.description:
        puerto = port.device
        print(f"Port trobat: {port.device}")

# --- INICIALITZACIÓ SERIAL ---
ser = None
if puerto:
    try:
        ser = serial.Serial(puerto, baudrate, timeout=1)
        print(f"Connectat a {puerto} a {baudrate} bauds")
        time.sleep(2)
    except serial.SerialException as e:
        print(f"Error de connexió EEG: {e}")
        ser = None



# ======== PARÁMETROS EEG ========
FS_HINT = 256                 # Hz esperados (si no conoces exacto, estimaremos online)
WIN_SEC = 2.0                 # ventana para FFT (s)
F_TARGET = 12.0               # Hz de flicker
F_SHOW_MIN, F_SHOW_MAX = 6.0, 30.0

# ======== PARÁMETROS EXPERIMENTO ========
BLOCK_FLICKER = 10.0          # s ON
BLOCK_REST    = 10.0          # s OFF
N_CYCLES      = 5
FULLSCR       = True

# ======== INICIALIZACIÓN ========
win = visual.Window(size=[1200, 800], color='black', units='pix', fullscr=FULLSCR)
txt = visual.TextStim(win, text='', color='white', pos=(0, 320), height=32, wrapWidth=1000)

# Estímulo: tablero/cuadro central que invierte polaridad
size = 500
stim = visual.Rect(win, width=size, height=size, fillColor='white', lineColor=None)
bg   = visual.Rect(win, width=size, height=size, fillColor='black', lineColor=None)  # para invertir
grey = visual.Rect(win, width=size, height=size, fillColor=[0,0,0], lineColor=None)  # gris (0 en rgb255)

# Gráfica rápida: barra de potencia 12 Hz
bar_bg = visual.Rect(win, width=300, height=30, pos=(0, -330), fillColor=[-0.5,-0.5,-0.5], lineColor=None)
bar_ok = visual.Rect(win, width=1, height=30, pos=(-150, -330), anchor='left', fillColor='green', lineColor=None)
label12 = visual.TextStim(win, text='Potencia ~12 Hz', color='white', pos=(0, -290), height=22)

# Buffer de datos crudos
buf_sec = 5.0
bufN = int(FS_HINT*buf_sec)
raw_buf = deque(maxlen=max(1, bufN))
ts_buf  = deque(maxlen=max(1, bufN))

# Serie
ser = None
if puerto:
    try:
        ser = serial.Serial(puerto, baudrate, timeout=0.001)
        time.sleep(2.0)
        ser.reset_input_buffer()
        print(f">> Conectado a {puerto} @ {baudrate}")
    except Exception as e:
        print("No se pudo abrir el puerto serie:", e)

# Utilidades
clock = core.Clock()
exp_clock = core.Clock()

def read_one_sample():
    """Lee una muestra float del puerto. Adapta si tu ADC manda enteros."""
    if ser is None:
        return None
    line = ser.readline()
    if not line:
        return None
    try:
        return float(line.strip())
    except:
        return None


def estimate_fs(ts):
    """Estimación robusta de FS por diferencias temporales medianas."""
    if len(ts) < 10:
        return FS_HINT
    dt = np.diff(ts)
    if np.any(dt <= 0):
        dt = dt[dt > 0]
    if len(dt) == 0:
        return FS_HINT
    return 1.0 / np.median(dt)

def hann(n):
    return 0.5 - 0.5*np.cos(2*np.pi*np.arange(n)/max(1,(n-1)))

def power_at(freqs, pxx, f0, bw=0.5):
    """Potencia integrada en una ventanita +-bw alrededor de f0."""
    mask = (freqs >= (f0-bw)) & (freqs <= (f0+bw))
    if not np.any(mask):
        return 0.0
    return float(np.mean(pxx[mask]))

def compute_fft_features(x, fs):
    """FFT simple (sin SciPy). Devuelve freqs, pxx, potencia 12 Hz y espectro filtrado 6-30 Hz."""
    x = np.asarray(x, dtype=float)
    x = x - np.mean(x)
    n = len(x)
    w = hann(n)
    xw = x * w
    # FFT real
    X = np.fft.rfft(xw)
    pxx = (np.abs(X)**2) / np.sum(w**2)
    freqs = np.fft.rfftfreq(n, d=1.0/fs)
    # potencia en banda de interés
    p12 = power_at(freqs, pxx, F_TARGET, bw=0.3)
    # Subespectro 6-30 Hz
    mask = (freqs >= F_SHOW_MIN) & (freqs <= F_SHOW_MAX)
    return freqs[mask], pxx[mask], p12

# ======== RUTINA PRINCIPAL ========
def run_block(flicker_on=True, dur=10.0):
    global estado_actual
    if flicker_on:
        estado_actual = "flicker"
    else:
        estado_actual = "rest"
    #
    clock.reset()
    phase_on = True
    flip_int = 1.0/(2.0*F_TARGET)  # invertimos blanco/negro dos veces por ciclo -> 12 Hz
    next_flip_t = 0.0

    while clock.getTime() < dur:
        # Lectura rápida (varias por frame si hay)
        for _ in range(4):
            v = read_one_sample()
            if v is None:
                break
            tnow = exp_clock.getTime()
            raw_buf.append(v)
            ts_buf.append(tnow)

        # Estimación FS con timestamps
        fs_est = estimate_fs(list(ts_buf))

        # Bloque flicker o reposo
        if flicker_on:
            t = clock.getTime()
            if t >= next_flip_t:
                phase_on = not phase_on
                next_flip_t += flip_int
            # dibuja polaridad
            if phase_on:
                bg.draw(); stim.draw()
            else:
                stim.draw(); bg.draw()
            txt.text = f"Bloque FLICKER 12 Hz  |  FS≈ {fs_est:5.1f} Hz"
        else:
            grey.draw()
            txt.text = f"Bloque REPOSO (gris)  |  FS≈ {fs_est:5.1f} Hz"

        # Espectro y barra de potencia
        txt.draw()
        bar_bg.draw()
        p12 = 0.0
        if len(raw_buf) >= int(max(0.5, WIN_SEC)*fs_est):
            N = int(min(len(raw_buf), WIN_SEC*fs_est))
            x = np.array(list(raw_buf)[-N:], dtype=float)
            fre, pxx, p12 = compute_fft_features(x, fs_est)
            # Escala de barra (auto, robusta)
            # baseline = mediana del subespectro
            baseline = np.median(pxx) + 1e-12
            ratio = np.clip((p12 / baseline), 0.0, 8.0)   # limitado para barra
            bar_ok.width = 300 * (ratio/8.0)
            bar_ok.pos = (-150, -330)
            bar_ok.draw()
        label12.text = f"Potencia @12 Hz (relativa): {p12:.2e}"
        label12.draw()

        # teclas
        if 'escape' in event.getKeys():
            core.quit()

        win.flip()





#### EXPERIMENTO Y REGISTRO



estado_actual = "none"   # global

# --- buffers y control ---
datos_eeg = []
running = True

# --- función de lectura continua ---
def llegir_eeg_continu():
    global running, estado_actual
    while running:
        if ser and ser.in_waiting:
            try:
                linea = ser.readline().decode('utf-8').strip()
                if linea:
                    t_global = exp_clock.getTime()   # usa el mismo reloj que el experimento
                    datos_eeg.append(f"{t_global:.4f},{linea},{estado_actual}")
            except Exception:
                continue

# --- iniciar el hilo de lectura antes de la secuencia de bloques ---
eeg_thread = threading.Thread(target=llegir_eeg_continu, daemon=True)
eeg_thread.start()


# Instrucciones
txt.text = ("TEST SSVEP 12 Hz\n\n"
            "Coloca electrodos: señal ROJO en Oz, referencia AZUL en mastoides, tierra NEGRO en Fpz.\n"
            "Verás bloques de 10 s: patrón parpadeante (12 Hz) y reposo. \n"
            "Durante el parpadeo debe subir la potencia ~12 Hz.\n\n"
            "Pulsa ESPACIO para comenzar.")
txt.draw(); win.flip()
event.waitKeys(keyList=['space'])
event.clearEvents()


# Secuencia de bloques
for i in range(N_CYCLES):
    run_block(flicker_on=True, dur=BLOCK_FLICKER)
    run_block(flicker_on=False, dur=BLOCK_REST)

# Cierre
txt.text = "Fin del test. ¿Has visto la barra crecer en 12 Hz durante el flicker?\nPulsa cualquier tecla para salir."
txt.draw(); win.flip()
event.waitKeys()
win.close()


# detener hilo y guardar datos
running = False
eeg_thread.join(timeout=1.0)

out_file = f"ssvep_raw_{time.strftime('%Y%m%d_%H%M%S')}.csv"
with open(out_file, 'w', encoding='utf-8') as f:
    f.write("time_s,value,state\n")
    for row in datos_eeg:
        f.write(row + "\n")

print(f">> Guardado EEG continuo en {out_file}")



# ========= ANÁLISIS RÁPIDO INTEGRADO SEÑAL RAW =========

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# --- Parámetros de visualización / RMS ---
WIN_SEC = 1.0  # ventana RMS en segundos (ajusta a gusto)

# --- Carga robusta del CSV ---
df = pd.read_csv(out_file)  # usa la ruta que acabas de guardar
# normaliza nombres
df.columns = [c.strip().lower() for c in df.columns]

# verifica columnas
required = {'time_s','value','state'}
if not required.issubset(set(df.columns)):
    raise ValueError(f"Faltan columnas. Se esperaban: {required}, y hay: {set(df.columns)}")

# fuerza numéricos y elimina filas inválidas
df['time_s'] = pd.to_numeric(df['time_s'], errors='coerce')
df['value']  = pd.to_numeric(df['value'],  errors='coerce')
df = df.dropna(subset=['time_s','value']).reset_index(drop=True)

# limpia 'state': a minúsculas, sin espacios, mapeo a {flicker, rest, none}
state_raw = df['state'].astype(str).str.strip().str.lower()
state_map = {'flicker':'flicker', 'rest':'rest', 'none':'none'}
df['state'] = state_raw.map(state_map).fillna('none')  # cualquier cosa rara -> none

# extrae arrays
t = df['time_s'].to_numpy(dtype=float)
v = df['value'].to_numpy(dtype=float)
s = df['state'].to_numpy(dtype=str)

# --- Estima Fs y prepara RMS ---
dt = np.diff(t); dt = dt[dt > 0]
fs = 1.0 / np.median(dt) if len(dt) else FS_HINT
win = max(1, int(round(WIN_SEC * fs)))

def moving_rms(x, win_samples):
    if win_samples <= 1:
        return np.abs(x)
    sq = x**2
    k = np.ones(win_samples) / win_samples
    return np.sqrt(np.convolve(sq, k, mode='same'))

rms = moving_rms(v, win)

# --- Resumen por estado (RMS medio) ---
order_states = ['none', 'rest', 'flicker']  # orden lógico para mostrar
present_states = [st for st in order_states if np.any(s == st)]
by_state = {st: float(np.nanmean(rms[s == st])) for st in present_states}

print(f"Fs estimada: {fs:.2f} Hz | ventana RMS: {win} muestras (~{WIN_SEC:.2f} s)")
for st in present_states:
    print(f"  {st:>7s} -> RMS medio = {by_state[st]:.4g} | n={np.sum(s==st)}")

# --- Gráfico temporal con fondos por estado (colores fuertes + etiquetas) ---
color_fill = {
    'flicker': (0.20, 0.45, 1.00, 0.35),  # azul intenso translúcido
    'rest':    (1.00, 0.30, 0.30, 0.30),  # rojo translúcido
    'none':    (0.60, 0.60, 0.60, 0.25)   # gris translúcido
}


plt.figure(figsize=(12, 6))
plt.plot(t, rms, linewidth=1.6, label=f'RMS ~{WIN_SEC:.1f}s')
# detectar cambios de estado y segmentar
change_idx = np.where(s[1:] != s[:-1])[0] + 1
segments = np.r_[0, change_idx, len(s)]
#y_top = np.nanmax(rms) if np.isfinite(np.nanmax(rms)) else 1.0

for i in range(len(segments)-1):
    st = s[segments[i]]
    t0, t1 = t[segments[i]], t[segments[i+1]-1]
    plt.axvspan(t0, t1, color=color_fill.get(st, color_fill['none']), linewidth=0)

# leyenda de zonas
legend_patches = [Patch(facecolor=color_fill[st], edgecolor='none', label=st) for st in present_states]
plt.legend([*legend_patches], [st for st in present_states], loc='upper left', title='Estado', framealpha=0.9)
plt.xlabel("Tiempo (s)")
plt.ylabel("RMS (u.a.)")
plt.title("Energía (RMS) por tiempo con estados")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show(block=False)

# --- Barras comparando estados (mismos colores) ---
plt.figure(figsize=(6, 4))
bars = [by_state[st] for st in present_states]
bar_colors = [color_fill[st][:3] for st in present_states]  # sin alpha para barras
plt.bar(present_states, bars, color=bar_colors)
plt.ylabel("RMS medio")
plt.title("RMS medio por estado")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

plt.show(block=False)




# ====== ANÁLISIS ESPECÍFICO 12 Hz (sin funciones) ======
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from scipy import signal


# ----- Parámetros del análisis -----
F_TARGET = 12.0      # Hz del flicker
SEG_SEC  = 2.0       # segundos por segmento (resolución ~0.5 Hz)
OVERLAP  = 0.5       # solapamiento Welch (0..0.9)
F_MIN, F_MAX = 6.0, 30.0   # banda visible de PSD
BANDWIDTH = 0.3      # ±Hz alrededor de F_TARGET para integrar potencia
NOISE_SPAN = 3.0     # Hz a cada lado para ruido local (excluyendo la banda central)
GUARD = 0.5          # Hz de guarda alrededor de la banda central para el ruido

# ----- Carga robusta del CSV -----
df = pd.read_csv(out_file)  # usa la ruta que acabas de guardar
df.columns = [c.strip().lower() for c in df.columns]
req = {'time_s','value','state'}
if not req.issubset(df.columns):
    raise ValueError(f"El CSV debe tener columnas: {req}")

df['time_s'] = pd.to_numeric(df['time_s'], errors='coerce')
df['value']  = pd.to_numeric(df['value'],  errors='coerce')
df = df.dropna(subset=['time_s','value']).reset_index(drop=True)

# normalizar estados
state_raw = df['state'].astype(str).str.strip().str.lower()
df['state'] = state_raw.where(state_raw.isin(['flicker','rest','none']), 'none')

t = df['time_s'].to_numpy(float)
x = df['value'].to_numpy(float)
s = df['state'].to_numpy(str)

x_org = x.copy()
x     = x.copy()

# Calcular mediana y MAD (Median Absolute Deviation)
med = np.median(x)
mad = np.median(np.abs(x - med)) + 1e-12
rob_scale = 1.4826 * mad   # Escala robusta ≈ desviación estándar

# Parámetros de umbral
k_spike = 8.0   # para detectar picos aislados muy extremos
k_clip  = 6.0   # para recortar valores demasiado grandes (winsorizing)

# Z-score robusto
zrob = (x - med) / rob_scale

# Detectar outliers extremos
outliers = np.abs(zrob) > k_spike

# Marcar picos aislados (cuando solo un valor es outlier entre vecinos normales)
iso = outliers.copy()
if len(x) >= 3:
    iso[1:]  &= ~outliers[:-1]
    iso[:-1] &= ~outliers[1:]
else:
    iso[:] = False

# Interpolar picos aislados con vecinos inmediatos
idx_iso = np.where(iso)[0]
for i in idx_iso:
    if 0 < i < len(x)-1:
        x[i] = 0.5 * (x[i-1] + x[i+1])

# Winsorizar: recortar el resto de valores extremos
upper = med + k_clip * rob_scale
lower = med - k_clip * rob_scale
x = np.clip(x, lower, upper)

print(f"[Limpieza] Interpolados picos aislados: {len(idx_iso)} | "
      f"Winsorized fuera de ±{k_clip}·MAD: {np.sum(np.abs(zrob) > k_clip)}")


plt.figure(figsize=(12,5))
plt.plot(t, x_org, color='gray', alpha=0.6, label='Original (con outliers)')
plt.plot(t, x, color='blue', linewidth=1.2, label='Limpia (post outlier handling)')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV aprox.)")
plt.title("Comparación de señal original vs limpia")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show(block=False)



########


# ===== ESPECTROGRAMA (STFT) para flicker =====
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
from matplotlib.patches import Patch

# Parámetros
F_TARGET = 12.0        # Hz del flicker
SHOW_HARMONIC = True   # dibujar también 24 Hz
NPERSEG_SEC = 2.0      # ventana de 2 s => resolución ~0.5 Hz
OVERLAP = 0.5          # 50% de solapamiento
FMAX = 130.0            # límite superior del eje Y

# STFT
nperseg = max(16, int(round(NPERSEG_SEC * fs)))
noverlap = int(round(nperseg * OVERLAP))

# x debe ser 1D (usa la versión limpia si hiciste tratamiento de outliers)
x_stft = x.copy()  # o x_org si quieres ver bruto

# Espectrograma (potencia densa)
f, t_rel, Sxx = spectrogram(
    x_stft - np.mean(x_stft), fs=fs,
    nperseg=nperseg, noverlap=noverlap,
    detrend='constant', scaling='density', mode='psd'
)
# tiempo absoluto para alinear con tus estados (time_s)
t_abs = t[0] + t_rel

# Escala en dB con recorte robusto para evitar “quemados”
Sxx_db = 10.0 * np.log10(Sxx + 1e-18)
vmin = np.percentile(Sxx_db, 5)
vmax = np.percentile(Sxx_db, 95)

# Colores por estado (igual que en tus otros plots)
color_fill = {
    'flicker': (0.15, 0.35, 0.95, 0.35),  # azul
    'rest':    (0.95, 0.25, 0.25, 0.30),  # rojo
    'none':    (0.60, 0.60, 0.60, 0.25)   # gris
}

# Segmentos de estado (en el mismo tiempo absoluto)
change_idx = np.where(s[1:] != s[:-1])[0] + 1
segments = np.r_[0, change_idx, len(s)]

plt.figure(figsize=(11, 4.8))
# mapa tiempo-frecuencia
plt.pcolormesh(t_abs, f, Sxx_db, shading='gouraud', cmap='viridis', vmin=vmin, vmax=vmax)
cbar = plt.colorbar()
cbar.set_label('Potencia (dB re: densidad)')

# sombreado de estados
for i in range(len(segments) - 1):
    st = s[segments[i]]
    t0, t1 = t[segments[i]], t[segments[i+1]-1]
    plt.axvspan(t0, t1, color=color_fill.get(st, color_fill['none']), linewidth=0)

# líneas guía en 12 Hz (y 24 Hz opcional)
plt.axhline(F_TARGET, color='k', linestyle='--', linewidth=1, alpha=0.8, label=f'{F_TARGET:.0f} Hz')
if SHOW_HARMONIC:
    plt.axhline(2*F_TARGET, color='k', linestyle=':', linewidth=1, alpha=0.6, label=f'{2*F_TARGET:.0f} Hz')

# estética
plt.ylim(0, FMAX)
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.title('Espectrograma (STFT) con bloques de estado')
# leyenda de estados
present_states = [st for st in ['none','rest','flicker'] if np.any(s == st)]
patches = [Patch(facecolor=color_fill[st], edgecolor='none', label=st) for st in present_states]
plt.legend(handles=[*patches], loc='upper right', framealpha=0.9)
plt.tight_layout()
plt.show(block=False)
# ===== FIN ESPECTROGRAMA =====






########






plt.figure(figsize=(12,5))
plt.plot(t, x, label='Senyal original', color='darkblue', alpha=1, linewidth=1)

 # --- FILTRAT (Notch + Bandpass) ---
b_notch, a_notch = signal.iirnotch(50, 10, fs)
x = signal.filtfilt(b_notch, a_notch, x)

plt.plot(t, x, label='Senyal filtrada (notch 50 Hz)', color='orange', alpha=1, linewidth=2)
plt.xlabel("Temps (s)")
plt.ylabel("Amplitud")
plt.title("Efecte del filtre Notch a 50 Hz")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show(block=False)






# ----- Estimar Fs -----
dt = np.diff(t)
dt = dt[dt > 0]
fs = 1.0/np.median(dt) if len(dt) else 250.0
print(f"Fs estimada: {fs:.2f} Hz")

# ----- Preparar Welch y recorrido por ventanas deslizantes -----
nperseg = max(16, int(round(SEG_SEC*fs)))
noverlap = int(round(nperseg*OVERLAP))
step = max(1, nperseg - noverlap)

# ventana de Hann y escala (sin SciPy)
if nperseg <= 1:
    w = np.ones(1)
else:
    idx = np.arange(nperseg)
    w = 0.5 - 0.5*np.cos(2*np.pi*idx/(nperseg-1))


w_power = np.sum(w**2)

# ejes de frecuencia para rFFT
freqs = np.fft.rfftfreq(nperseg, d=1.0/fs)
mask_vis = (freqs >= F_MIN) & (freqs <= F_MAX)

# contenedores
times_win = []
p12_win   = []
snr_win   = []
state_win = []

# barridos de ventanas
N = len(x)
for start in range(0, N - nperseg + 1, step):
    seg = x[start:start+nperseg]
    seg_t = t[start:start+nperseg]
    seg_s = s[start:start+nperseg]
    # quitar media, aplicar Hann
    seg = seg - np.mean(seg)
    X = np.fft.rfft(seg * w)
    Pxx = (np.abs(X)**2) / w_power
    # potencia @ 12 Hz (promedio en ±BANDWIDTH)
    band = (freqs >= (F_TARGET - BANDWIDTH)) & (freqs <= (F_TARGET + BANDWIDTH))
    p_sig = float(np.mean(Pxx[band])) if np.any(band) else np.nan
    # ruido local (anillos excluyendo banda central + guarda)
    left_ring  = (freqs >= max(0.0, F_TARGET - NOISE_SPAN)) & (freqs <= (F_TARGET - BANDWIDTH - GUARD))
    right_ring = (freqs >= (F_TARGET + BANDWIDTH + GUARD)) & (freqs <= (F_TARGET + NOISE_SPAN))
    ring = left_ring | right_ring
    noise = float(np.median(Pxx[ring])) if np.any(ring) else np.nan
    snr = p_sig/noise if (noise is not None and noise > 0) else np.nan
    # timestamp representativo y estado mayoritario de la ventana
    times_win.append(float(np.mean(seg_t)))
    vals, counts = np.unique(seg_s, return_counts=True)
    state_win.append(str(vals[np.argmax(counts)]))
    p12_win.append(p_sig)
    snr_win.append(snr)

times_win = np.array(times_win, dtype=float)
p12_win   = np.array(p12_win,   dtype=float)
snr_win   = np.array(snr_win,   dtype=float)
state_win = np.array(state_win, dtype=str)

# ----- Resumen por estado (medianas) -----
order_states = ['none','rest','flicker']
present = [st for st in order_states if np.any(state_win==st)]

med_p12 = {st: float(np.nanmedian(p12_win[state_win==st])) for st in present}
med_snr = {st: float(np.nanmedian(snr_win[state_win==st])) for st in present}

print("Medianas por estado:")
for st in present:
    n = np.sum(state_win==st)
    print(f"  {st:>7s} | p12={med_p12[st]:.3e} | snr={med_snr[st]:.2f} | n_win={n}")

# ----- Gráfico 1: Potencia @12 Hz vs tiempo con estados claros -----
color_fill = {
    'flicker': (0.15, 0.35, 0.95, 0.35),  # azul
    'rest':    (0.95, 0.25, 0.25, 0.30),  # rojo
    'none':    (0.60, 0.60, 0.60, 0.25)   # gris
}


plt.figure(figsize=(12,5))
plt.plot(times_win, p12_win, label='Potencia @12 Hz (Welch)', linewidth=1.8)
# sombrear por estado detectando cambios
chg = np.where(state_win[1:] != state_win[:-1])[0] + 1
segs = np.r_[0, chg, len(state_win)]
for i in range(len(segs)-1):
    st = state_win[segs[i]]
    t0, t1 = times_win[segs[i]], times_win[segs[i+1]-1]
    plt.axvspan(t0, t1, color=color_fill.get(st, color_fill['none']), linewidth=0)
    if i>0:
        plt.axvline(t0, color='k', linestyle='--', alpha=0.25, linewidth=1)

# líneas de referencia: medianas por estado
for st in present:
    plt.hlines(med_p12[st], xmin=times_win.min(), xmax=times_win.max(),
               colors=color_fill[st][:3], linestyles='--', alpha=0.8, label=f"Mediana {st}")


plt.xlabel("Tiempo (s)")
plt.ylabel("Potencia @12 Hz (a.u.)")
plt.title("Evolución de potencia @12 Hz con bloques")
patches = [Patch(facecolor=color_fill[st], edgecolor='none', label=st) for st in present]
plt.legend(handles=patches, loc='upper left', framealpha=0.9)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show(block=False)


# ----- Gráfico 2: SNR @12 Hz por tiempo (opcional, muy ilustrativo) -----
plt.figure(figsize=(12,4))
plt.plot(times_win, snr_win, linewidth=1.6)
for i in range(len(segs)-1):
    st = state_win[segs[i]]
    t0, t1 = times_win[segs[i]], times_win[segs[i+1]-1]
    plt.axvspan(t0, t1, color=color_fill.get(st, color_fill['none']), linewidth=0)
    if i>0: plt.axvline(t0, color='k', ls='--', alpha=0.25, lw=1)
plt.xlabel("Tiempo (s)")
plt.ylabel("SNR @12 Hz")
plt.title("Relación señal/ruido @12 Hz por ventanas")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show(block=False)


# ----- Gráfico 3: Barras (medianas) por estado -----
plt.figure(figsize=(6,4))
vals = [med_p12[st] for st in present]
cols = [color_fill[st][:3] for st in present]
plt.bar(present, vals, color=cols)
plt.ylabel("Mediana potencia @12 Hz")
plt.title("Potencia @12 Hz por estado (mediana)")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show(block=False)


# ----- (Opcional) PSD medio por estado en 6–30 Hz -----
# Construimos una PSD agregando todas las ventanas por estado
do_psd = True
if do_psd:
    psd_acc = {st: [] for st in present}
    for start in range(0, N - nperseg + 1, step):
        seg = x[start:start+nperseg]
        seg_s = s[start:start+nperseg]
        vals, counts = np.unique(seg_s, return_counts=True)
        st = str(vals[np.argmax(counts)])
        if st not in present:
            continue
        seg = seg - np.mean(seg)
        X = np.fft.rfft(seg * w)
        Pxx = (np.abs(X)**2) / w_power
        psd_acc[st].append(Pxx[mask_vis])
    plt.figure(figsize=(9,5))
    f_vis = freqs[mask_vis]
    for st in present:
        if psd_acc[st]:
            P = np.vstack(psd_acc[st]).mean(axis=0)
            plt.plot(f_vis, P, label=st, color=color_fill[st][:3], linewidth=1.8)
    plt.axvline(F_TARGET, ls='--', color='k', alpha=0.5)
    plt.xlim([F_MIN, F_MAX])
    plt.xlabel("Frecuencia (Hz)"); plt.ylabel("Potencia (a.u.)")
    plt.title("PSD media por estado (6–30 Hz)")
    plt.legend(); plt.grid(alpha=0.3)
    plt.tight_layout()

plt.show(block=False)
# ====== FIN ANÁLISIS 12 Hz ======





# ===== ESPECTROGRAMA (STFT) para flicker =====
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
from matplotlib.patches import Patch

# Parámetros
F_TARGET = 12.0        # Hz del flicker
SHOW_HARMONIC = True   # dibujar también 24 Hz
NPERSEG_SEC = 2.0      # ventana de 2 s => resolución ~0.5 Hz
OVERLAP = 0.5          # 50% de solapamiento
FMAX = 40.0            # límite superior del eje Y

# STFT
nperseg = max(16, int(round(NPERSEG_SEC * fs)))
noverlap = int(round(nperseg * OVERLAP))

# x debe ser 1D (usa la versión limpia si hiciste tratamiento de outliers)
x_stft = x.copy()  # o x_org si quieres ver bruto

# Espectrograma (potencia densa)
f, t_rel, Sxx = spectrogram(
    x_stft - np.mean(x_stft), fs=fs,
    nperseg=nperseg, noverlap=noverlap,
    detrend='constant', scaling='density', mode='psd'
)
# tiempo absoluto para alinear con tus estados (time_s)
t_abs = t[0] + t_rel

# Escala en dB con recorte robusto para evitar “quemados”
Sxx_db = 10.0 * np.log10(Sxx + 1e-18)
vmin = np.percentile(Sxx_db, 5)
vmax = np.percentile(Sxx_db, 95)

# Colores por estado (igual que en tus otros plots)
color_fill = {
    'flicker': (0.15, 0.35, 0.95, 0.35),  # azul
    'rest':    (0.95, 0.25, 0.25, 0.30),  # rojo
    'none':    (0.60, 0.60, 0.60, 0.25)   # gris
}

# Segmentos de estado (en el mismo tiempo absoluto)
change_idx = np.where(s[1:] != s[:-1])[0] + 1
segments = np.r_[0, change_idx, len(s)]

plt.figure(figsize=(11, 4.8))
# mapa tiempo-frecuencia
plt.pcolormesh(t_abs, f, Sxx_db, shading='gouraud', cmap='viridis', vmin=vmin, vmax=vmax)
cbar = plt.colorbar()
cbar.set_label('Potencia (dB re: densidad)')

# sombreado de estados
for i in range(len(segments) - 1):
    st = s[segments[i]]
    t0, t1 = t[segments[i]], t[segments[i+1]-1]
    plt.axvspan(t0, t1, color=color_fill.get(st, color_fill['none']), linewidth=0)

# líneas guía en 12 Hz (y 24 Hz opcional)
plt.axhline(F_TARGET, color='k', linestyle='--', linewidth=1, alpha=0.8, label=f'{F_TARGET:.0f} Hz')
if SHOW_HARMONIC:
    plt.axhline(2*F_TARGET, color='k', linestyle=':', linewidth=1, alpha=0.6, label=f'{2*F_TARGET:.0f} Hz')

# estética
plt.ylim(0, FMAX)
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.title('Espectrograma (STFT) con bloques de estado')
# leyenda de estados
present_states = [st for st in ['none','rest','flicker'] if np.any(s == st)]
patches = [Patch(facecolor=color_fill[st], edgecolor='none', label=st) for st in present_states]
plt.legend(handles=[*patches], loc='upper right', framealpha=0.9)
plt.tight_layout()
plt.show(block=False)
# ===== FIN ESPECTROGRAMA =====


