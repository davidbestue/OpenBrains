# -*- coding: utf-8 -*-
"""
Anàlisi de potencial evocat (EEG Libet)
@author: Open Brains
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import os
import yasa



folder_path = "C:/Users/david/OneDrive/Documentos/GitHub/OpenBrains/Libet/2025-08-04_10-35-13_dani" 
fs=256
pre_trigger_sec=3, 
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



