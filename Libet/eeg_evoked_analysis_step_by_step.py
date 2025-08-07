# -*- coding: utf-8 -*-
"""
Anàlisi de potencial evocat (EEG Libet)
@author: Open Brains
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import spectrogram
import os
import yasa
import pywt




folder_path = "C:/Users/david/OneDrive/Documentos/GitHub/OpenBrains/Libet/2025-08-04_10-35-13_dani" 
fs=256
pre_trigger_sec=3 
post_trigger_sec = 1
baseline_relax_sec = 0.2 #200ms
export_epochs=True


#Carrega dades EEG i events, segmenta els 3s previs a "keypress" i retorna els epochs + figura.
#Parameters:
#    folder_path (str): Ruta a la carpeta que conté els fitxers EEG i events
#    fs (int): Freqüència de mostreig (Hz)
#     pre_trigger_sec (int): Segons a agafar abans del keypress
#     export_epochs (bool): Desa els epochs a .npy per a anàlisi posterior

# Returns:
#     epochs (np.ndarray): Array [n_trials x n_samples] amb els segments
# """


eeg_file = [f for f in os.listdir(folder_path) if f.endswith("_EEG_continu.txt")][0]
events_file = [f for f in os.listdir(folder_path) if f.endswith("_events.csv")][0]



# --- LECTURA SEGURA DEL FITXER EEG ---
eeg_path = os.path.join(folder_path, eeg_file)
timestamps = []
eeg_signal = []
with open(eeg_path, 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 2:
            try:
                timestamps.append(float(parts[0]))
                eeg_signal.append(float(parts[1]))
            except ValueError:
                continue

#
timestamps = np.array(timestamps)
eeg_signal = np.array(eeg_signal, dtype=np.float32)



# FS correcto?
diffs = np.diff(timestamps)
fs_real = 1 / np.median(diffs)
print(f"Freqüència de mostreig real estimada: {fs_real:.2f} Hz")






# --- INTERPOLACIÓ A MOSTREIG REGULAR ---
#Estem transformant una senyal EEG amb mostreig irregular (provinent del port sèrie) en una senyal amb mostreig regular mitjançant interpolació lineal. 
#Aquest pas és essencial per aplicar filtres, segmentar epochs i analitzar correctament la dinàmica temporal del senyal cerebral.
#Mirar como_funciona_la_interpolacion_a_tiempos_regulares

start_time = timestamps[0]
end_time = timestamps[-1]
uniform_times = np.arange(start_time, end_time, 1/fs)
eeg_interpolated = np.interp(uniform_times, timestamps, eeg_signal)

plt.figure(figsize=(12, 5))
plt.plot(timestamps, eeg_signal, color='darkblue', label='no interpolada', alpha=1, linewidth=2)
plt.plot(uniform_times, eeg_interpolated, color='darkorange', label= 'interpolada', alpha=1, linewidth=2)
plt.xlabel("Temps (s)")
plt.ylabel("Amplitud (a.u.)")
plt.title("Senyal EEG")
plt.legend()
plt.tight_layout()
plt.show(block=False)



 # --- FILTRAT (Notch + Bandpass) ---
b_notch, a_notch = signal.iirnotch(50, 10, fs)
eeg_notched = signal.filtfilt(b_notch, a_notch, eeg_interpolated)

plt.figure(figsize=(12, 5))
plt.plot(uniform_times, eeg_interpolated, label='Senyal original', color='darkblue', alpha=1, linewidth=1)
plt.plot(uniform_times, eeg_notched, label='Senyal filtrada (notch 50 Hz)', color='orange', alpha=1, linewidth=2)
plt.xlabel("Temps (s)")
plt.ylabel("Amplitud")
plt.title("Efecte del filtre Notch a 50 Hz")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show(block=False)


#La freqüència de Nyquist és la meitat de la freqüència de mostreig (fs/2) 
#i representa la màxima freqüència que es pot reconstruir fidelment en un senyal digital. 
#Segons el teorema de Nyquist-Shannon, cal almenys dues mostres per cicle per captar correctament una oscil·lació.
#Mirar arxivo de como_el_samping_rate_define_la_maxima_frecuencia_detectable.py

b_band, a_band = signal.butter(2, [1/(fs/2), 38/(fs/2)], btype='band')  
# normalitzem les freqüències fent que fs/2 (la freqüència de Nyquist) sigui el valor màxim, equivalent a 1.
# Band pass filter: Filtre pasabanda: filtre que deixa passar les freqüències entre un límit inferior (f_low) i un superior (f_high), bloquejant la resta.
#Indica el rang de freqüències a deixar passar (en aquest cas, de 1 Hz a 38 Hz).

eeg_bandpassed = signal.filtfilt(b_band, a_band, eeg_notched)
plt.figure(figsize=(12, 5))
plt.plot(uniform_times, eeg_bandpassed, color='darkblue', alpha=1, linewidth=2)
plt.xlabel("Temps (s)")
plt.ylabel("Amplitud (a.u.)")
plt.title("Senyal EEG després del Band pass filter")
plt.tight_layout()
plt.show(block=False)


# --- CARREGA EVENTS ---
events = pd.read_csv(os.path.join(folder_path, events_file))
keypress_times = events[events["event"].str.contains("keypress")]["time"].values
end_relax_times = events[events["event"].str.contains("start_trial")]["time"].values


# --- EPOCHING ---
#Dividir la senyal contínua (longa i ininterrompuda) en segments més curts (anomenats epochs), 
#que estan alineats temporalment a un esdeveniment d’interès (com ara un estímul, una decisió o una resposta motora).
samples_before = int(pre_trigger_sec * fs)
samples_after = int(post_trigger_sec * fs)  
samples_total = samples_before + samples_after
samples_relax = int(baseline_relax_sec * fs)  

epochs_list = []

# Per associar cada keypress amb el seu relax anterior
def buscar_baseline(t_event):
    idx = np.searchsorted(end_relax_times, t_event) - 1 #obtenim l'índex del final relaxament anterior:
    if idx < 0:
        return None
    return end_relax_times[idx]
#

for t_event in keypress_times:
        # --- EPOCH EVENT ---
        if t_event - pre_trigger_sec < uniform_times[0] or t_event > uniform_times[-1]:
            print(f"⚠️ Error de registre dels temps per a l'esdeveniment a {t_event:.3f}s")
            continue
        idx_event = np.searchsorted(uniform_times, t_event)
        idx_end = idx_event + samples_after
        idx_start = idx_event - samples_before
        if idx_start < 0:
            print(f"⚠️ No hi ha suficient temps previa per a l'esdeveniment a {t_event:.3f}s")
            continue
        if idx_end > eeg_bandpassed.shape[0] - 1:
            print(f"⚠️ No hi ha suficient temps posterior per a l'esdeveniment a {t_event:.3f}s")
            continue
        epoch = eeg_bandpassed[idx_start:idx_end]
        ###
        # --- BASELINE DE RELAXACIÓ ---
        t_relax_end = buscar_baseline(t_event)
        if t_relax_end is None:
            print(f"⚠️ No s'ha trobat relaxació prèvia a l'esdeveniment a {t_event:.3f}s")
            continue
        # Convertim temps a índexs
        idx_relax_end = np.searchsorted(uniform_times, t_relax_end)
        if idx_relax_end > eeg_bandpassed.shape[0]:
            print(f"⚠️ Relaxació posterior fora del rang per a {t_event:.3f}s")
            continue
        #
        idx_relax_start = idx_relax_end - samples_relax
        baseline_segment = eeg_bandpassed[idx_relax_start:idx_relax_end]  # Ultims 200ms abans de començar el trial
        if len(baseline_segment) < int(0.2 * fs):  
            print(f"⚠️ Segment de baseline massa curt per a {t_event:.3f}s")
            continue
        ##
        # --- BASELINE CORRECTION ---
        # Calculem la mitjana només dels últims 200 ms de la relaxació per a cada epoch individualment.
        # Això permet centrar cada senyal al voltant de 0 µV de manera personalitzada,
        # evitant que un únic valor de baseline afecti tots els epochs.
        # Mirar la importància d'aquest pas a como_funciona_el_baseline_correction.py
        baseline = np.mean(baseline_segment)
        epoch_corrected = epoch - baseline
        if len(epoch_corrected) == samples_total:
            epochs_list.append(epoch_corrected)
        else:
            print(f"⚠️ Epoch descartat: longitud {len(epoch_corrected)} ≠ {samples_total}")
        #


#
if len(epochs_list) == 0:
    print("\n⚠️ No s'han trobat epochs vàlids.")
else:
    print(f"Número d'epochs: {len(epochs_list)}")

epochs_list = np.array(epochs_list)


# --- FILTRAT D'OUTLIERS ---
threshold_uV = 999* 1e15 # µV (100µV)## INCORRECTO, PARA JUGAR!
#threshold_uV = 100  # µV
epochs_uV = epochs_list * 1e6
mask = np.max(np.abs(epochs_uV), axis=1) < threshold_uV
epochs = epochs_list[mask]

print(f"Percentatge d'outliers: {len(epochs)/len(epochs_list)*100}%")
print(f"Número d'epochs vàlids: {len(epochs)}")


if export_epochs:
    np.save(os.path.join(folder_path, "epochs.npy"), epochs)



# --- GRAFICACIÓ POTENCIAL EVOCAT AMB SEM ---
time_axis = np.linspace(-pre_trigger_sec, post_trigger_sec, samples_total)
mean_potential = np.mean(epochs, axis=0)
sem = np.std(epochs, axis=0) / np.sqrt(epochs.shape[0])
ci95 = sem * 1.96

plt.figure(figsize=(10, 4))
plt.plot(time_axis, mean_potential * 1e6, label="Mitjana")
plt.axhline(0, color='black', linestyle='--', linewidth=1)  # línia horitzontal de base
plt.fill_between(time_axis, (mean_potential - ci95) * 1e6, (mean_potential + ci95) * 1e6,
                 color='blue', alpha=0.3, label="IC 95%")
plt.axvline(0, color='r', linestyle='--', label='Pulsació')
plt.title("Potencial evocat mitjà (3s abans de la decisó)")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitud (µV)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)


# --- ESPECTROGRAMES: STFT y CWT ---
# Ver las diferencias de resolucion en como_funciona_el_STFT_vs_el_CWT.py
# Mejor el CWT

# STFT (Short-Time Fourier Transform) 
#Espectrograma (STFT): mostra com les freqüències canvien al llarg del temps dividint la senyal en finestres 
#(sacrificant resolució temporal o freqüencial segons la mida de la finestra).

f, t_spec, Sxx = spectrogram(mean_potential, fs=fs, nperseg=fs, noverlap=int(fs * 0.5))  # finestra de 1s, 50% solapament
plt.figure(figsize=(10, 4))
plt.pcolormesh(t_spec - pre_trigger_sec, f, 10 * np.log10(Sxx), shading='gouraud', cmap='viridis')
plt.colorbar(label='Potència (dB)')
plt.ylabel('Freqüència (Hz)')
plt.xlabel('Temps (s)')
plt.title('Espectrograma (STFT)')
plt.ylim(0, 60)
plt.axvline(0, color='black', linestyle='--', label='Esdeveniment')
plt.legend()
plt.tight_layout()
plt.show(block=False)

# CWT (Transformada Wavelet Contínua) ---
# És una transformada que analitza una senyal comparant-la amb una funció anomenada ona mare (wavelet), 
#comprimint-la o estirant-la per capturar informació en diferents escales (freqüències) i moments temporals.
#És com un STFT pero enlloc de tenir una finestra fixa, va variant

# Suposem que mean_potential i fs estan definits
scales = np.arange(1, 128)
coefficients, frequencies = pywt.cwt(mean_potential, scales, 'morl', sampling_period=1/fs)

plt.figure(figsize=(10, 4))
plt.imshow(np.abs(coefficients), extent=[-pre_trigger_sec, post_trigger_sec, frequencies[-1], frequencies[0]],
           cmap='viridis', aspect='auto')
plt.colorbar(label='Amplitud')
plt.ylabel('Freqüència (Hz)')
plt.xlabel('Temps (s)')
plt.title('Transformada Wavelet Contínua (CWT)')
plt.ylim(0, 60)
plt.axvline(0, color='white', linestyle='--', label='Esdeveniment')
plt.legend()
plt.tight_layout()
plt.show(block=False)
