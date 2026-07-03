# -*- coding: utf-8 -*-
"""
ANÀLISI MULTISUJECTE - EXPERIMENT DE LIBET
@author: Open Brains / Col·laborador
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURACIÓ DE L'ANÀLISI ---
#folder_path = "resultats_pilot"  # Carpeta principal on els alumnes deixen les seves carpetas
folder_path = "C:\\Users\\david\\Downloads\\libet_pias"
folder_path = "C:\\Users\\david\\Downloads\\libet_sarria"


pre_trigger_sec = 3.0    # Quants segons abans de prémer mirem (rampa de Libet)
post_trigger_sec = 1.0   # Quants segons després de prémer mirem
fs = 250                 # Freqüència de mostreig del fitxer simulat (250 Hz)

# Càlcul de mostres totals per època
samples_pre = int(pre_trigger_sec * fs)
samples_post = int(post_trigger_sec * fs)
samples_total = samples_pre + samples_post

all_epochs = []
all_w_times = []

print("🔍 Iniciant l'escaneig de la carpeta de resultats...")

# --- 1. LECTURA DE DADES DE TOTS ELS ALUMNES ---
# Busquem subcarpetes dins de la carpeta "results"
subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

if not subfolders:
    print(f"❌ Error: No s'ha trobat cap subcarpeta dins de '{folder_path}'.")
    print("Assegura't que els alumnes han col·locat les seves carpetes completes allà.")
    exit()

for student_folder in subfolders:
    folder_name = os.path.basename(student_folder)
    print(f"📂 Processant: {folder_name}...")
    
    # Identificar arxius per extensions/patrons
    files = os.listdir(student_folder)
    eeg_file = [f for f in files if f.endswith("_EEG_continu.txt")]
    events_file = [f for f in files if f.endswith("_events.csv")]
    results_file = [f for f in files if f.endswith("_resultats.csv")]
    
    if not eeg_file or not events_file or not results_file:
        print(f"⚠️ Alerta: La carpeta {folder_name} no conté tots els fitxers necessaris. Ometent...")
        continue
        
    # Carregar W-times (difference_sec) del fitxer de resultats de l'alumne
    try:
        df_res = pd.read_csv(os.path.join(student_folder, results_file[0]))
        w_times = df_res['difference_sec'].dropna().tolist()
        all_w_times.extend(w_times)
    except Exception as e:
        print(f"❌ Error llegint resultats de {folder_name}: {e}")
        continue

    # Carregar EEG Continu de l'alumne
    # Com que el fitxer pot ser gran, el llegim de forma eficient
    try:
        eeg_times = []
        eeg_values = []
        with open(os.path.join(student_folder, eeg_file[0]), 'r') as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    eeg_times.append(float(parts[0]))
                    eeg_values.append(float(parts[1]))
        
        eeg_times = np.array(eeg_times)
        eeg_values = np.array(eeg_values)
    except Exception as e:
        print(f"❌ Error llegint EEG de {folder_name}: {e}")
        continue

    # Carregar esdeveniments (Triggers)
    try:
        df_events = pd.read_csv(os.path.join(student_folder, events_file[0]))
        # Filtrem només les pulsacions de la barra d'espai
        keypress_events = df_events[df_events['event'].str.contains('keypress_trial', na=False)]
    except Exception as e:
        print(f"❌ Error llegint esdeveniments de {folder_name}: {e}")
        continue

    # --- 2. EXTRACCIÓ D'ÈPOQUES (EPOCHING) ---
    for _, row in keypress_events.iterrows():
        t_trigger = row['time']
        
        # Busquem l'índex de temps a l'EEG més proper al nostre trigger
        idx_trigger = np.searchsorted(eeg_times, t_trigger)
        
        # Definim l'interval de l'època en índexs de l'array
        idx_start = idx_trigger - samples_pre
        idx_end = idx_trigger + samples_post
        
        # Validem que l'època estigui completament dins dels límits del fitxer d'EEG
        if idx_start >= 0 and idx_end < len(eeg_values):
            epoch = eeg_values[idx_start:idx_end]
            
            # --- CORRECCIÓ DE LÍNIA DE BASE (Baseline Correction) ---
            # Restem la mitjana dels primers 500ms de l'època per centrar-la a 0
            baseline_samples = int(0.5 * fs)
            baseline = np.mean(epoch[:baseline_samples])
            epoch_corrected = epoch - baseline
            
            all_epochs.append(epoch_corrected)

# --- 3. ESTADÍSTICA GLOBAL I GRAFICACIÓ ---
if not all_epochs:
    print("❌ No s'ha pogut extreure cap època vàlida. Revisa els fitxers de dades.")
    exit()

epochs_matrix = np.array(all_epochs)
mean_w_time = np.mean(all_w_times)
total_trials = epochs_matrix.shape[0]

print("\n--- ESTADÍSTIQUES FINALS ---")
print(f"📊 Nombre total d'alumnes/carpetes vàlides: {len(subfolders)}")
print(f"🎯 Nombre total de trials acumulats: {total_trials}")
print(f"⏱️ W-time mitjà calculat (decisió conscient): {mean_w_time:.3f} segons de la pulsació.")

# Càlcul de la mitjana i l'error estàndard (SEM)
time_axis = np.linspace(-pre_trigger_sec, post_trigger_sec, samples_total)
mean_potential = np.mean(epochs_matrix, axis=0)
sem = np.std(epochs_matrix, axis=0) / np.sqrt(total_trials)
ci95 = sem * 1.96

# Multipliquem per 1e6 per passar de Volts a Microvolts (µV)
mean_potential_uv = mean_potential * 1e6
ci95_uv = ci95 * 1e6

# Crear el Gràfic
plt.figure(figsize=(11, 5))
plt.plot(time_axis, mean_potential_uv, label=f"Potencial Evocat Mitjà (n={total_trials} trials)", color='blue', linewidth=2)
plt.fill_between(time_axis, mean_potential_uv - ci95_uv, mean_potential_uv + ci95_uv,
                 color='blue', alpha=0.2, label="Interval de Confiança 95%")

# Línies de referència
plt.axhline(0, color='black', linestyle='--', linewidth=0.8) # Línia de base 0 µV
plt.axvline(0, color='red', linestyle='-', linewidth=1.5, label='Pulsació Física (Barra Espaiadora)')
plt.axvline(mean_w_time, color='orange', linestyle='--', linewidth=1.5, label=f'Temps de decisió Mitjà ({mean_w_time:.3f} s)')

# Estètica del gràfic
plt.title("L'Experiment de Libet", fontsize=14, pad=15)
plt.xlabel("Temps respecte a l'acció física (segons)", fontsize=12)
plt.ylabel("Amplitud de la senyal (µV) ]", fontsize=12)

plt.gca().invert_yaxis()  # <--- AFEGEIX AQUESTA LÍNIA PER A MOSTRAR EL POTENCIAL CAP AMUNT

plt.xlim(-pre_trigger_sec, post_trigger_sec)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc="upper left", fontsize=10)
plt.tight_layout()


# Mostrar per pantalla
plt.show(block=False)




# --- 3. ESTADÍSTICA GLOBAL I GRAFICACIÓ EN DOS PANELLS ---
if not all_epochs:
    print("❌ No s'ha pogut extreure cap època vàlida. Revisa els fitxers de dades.")
    exit()

epochs_matrix = np.array(all_epochs)
mean_w_time = np.mean(all_w_times)
total_trials = epochs_matrix.shape[0]

print("\n--- ESTADÍSTIQUES FINALS ---")
print(f"📊 Nombre total d'alumnes/carpetes vàlides: {len(subfolders)}")
print(f"🎯 Nombre total de trials de classe: {total_trials}")
print(f"⏱️ W-time mitjà (decisió conscient): {mean_w_time:.3f} segons de la pulsació.")

# Temps original (alineat amb la pulsació a t=0)
time_axis_pulsacio = np.linspace(-pre_trigger_sec, post_trigger_sec, samples_total)

# Temps alineat amb la decisió (desplacem l'eix de temps restant el w_time mitjà)
# Al restar-ho, el moment de la decisió passa a ser el nou "zero" de l'eix de temps
time_axis_decisio = time_axis_pulsacio - mean_w_time

# Càlcul de la mitjana i l'error estàndard (SEM) en microvolts (µV)
mean_potential_uv = np.mean(epochs_matrix, axis=0) * 1e6
sem_uv = (np.std(epochs_matrix, axis=0) / np.sqrt(total_trials)) * 1e6
ci95_uv = sem_uv * 1.96

# --- CREAR EL GRÀFIC DOBLE (1 fila, 2 columnes) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5), sharey=True)
fig.suptitle("L'Experiment de Libet", fontsize=16, y=1.02)

# ==========================================
# PANELL 1: ALINEAT AMB LA PULSACIÓ FÍSICA
# ==========================================
ax1.plot(time_axis_pulsacio, mean_potential_uv, color='blue', linewidth=2, label="Potencial Evocat")
ax1.fill_between(time_axis_pulsacio, mean_potential_uv - ci95_uv, mean_potential_uv + ci95_uv, color='blue', alpha=0.15, label="IC 95%")

ax1.axhline(0, color='black', linestyle='--', linewidth=0.8) 
ax1.axvline(0, color='red', linestyle='-', linewidth=1.5, label='Pulsació Física (t=0)')
ax1.axvline(mean_w_time, color='orange', linestyle='--', linewidth=1.5, label=f'W-time estimat ({mean_w_time:.3f} s)')

ax1.set_title("Alineat amb l'Acció Física (M-Time)", fontsize=12, pad=10)
ax1.set_xlabel("Temps respecte a la pulsació (segons)", fontsize=11)
ax1.set_ylabel("Amplitud de la senyal (µV)", fontsize=11)
ax1.set_xlim(-pre_trigger_sec, post_trigger_sec)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc="upper left", fontsize=9)
ax1.invert_yaxis()  # Eix invertit (negatiu amunt) per intuïció visual

# ==========================================
# PANELL 2: ALINEAT AMB LA DECISIÓ CONSCIENT
# ==========================================
ax2.plot(time_axis_decisio, mean_potential_uv, color='purple', linewidth=2, label="Potencial Evocat")
ax2.fill_between(time_axis_decisio, mean_potential_uv - ci95_uv, mean_potential_uv + ci95_uv, color='purple', alpha=0.15, label="IC 95%")

ax2.axhline(0, color='black', linestyle='--', linewidth=0.8)
ax2.axvline(0, color='orange', linestyle='-', linewidth=1.5, label='Decisió Conscient (t=0)')
# La pulsació física en aquest nou eix estarà a l'equivalent positiu del w_time absolut
ax2.axvline(-mean_w_time, color='red', linestyle='--', linewidth=1.5, label=f'Pulsació Física (+{-mean_w_time:.3f} s)')

ax2.set_title("Alineat amb la Voluntat Conscient (W-Time)", fontsize=12, pad=10)
ax2.set_xlabel("Temps respecte a la decisió (segons)", fontsize=11)
ax2.set_xlim(-pre_trigger_sec - mean_w_time, post_trigger_sec - mean_w_time) # Ajustem límits de l'eix desplaçat
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc="upper left", fontsize=9)
# Nota: "sharey=True" fa que ax2 s'encomani automàticament de la inversió de l'eix Y de ax1

plt.tight_layout()
plt.show(block=False)