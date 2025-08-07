# -*- coding: utf-8 -*-
"""
Anàlisi de potencial evocat (EEG Libet)
@author: Open Brains
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from glob import glob

# Ruta on tens els arxius de cada subjecte

folder_paths = [os.path.normpath(p) for p in glob("C:/Users/david/OneDrive/Documentos/GitHub/OpenBrains/Libet/*/epochs.npy")]

all_subject_means = []

for path in folder_paths:
	epochs = np.load(path)  # (n_epochs, n_samples)
	if epochs.shape[0] < 3:
		print(f"⚠️ Pocs trials per {path}. S'omet.")
	#
	subject_mean = np.mean(epochs, axis=0)  # (n_samples,)
	all_subject_means.append(subject_mean)

all_subject_means = np.array(all_subject_means)  # (n_subjects, n_samples)

# Calculem mitjana i IC95 entre subjectes
mean_potential = np.mean(all_subject_means, axis=0)
sem = np.std(all_subject_means, axis=0, ddof=1) / np.sqrt(all_subject_means.shape[0])
ci95 = sem * 1.96

# Eix temporal
samples_total = all_subject_means.shape[1]
time_axis = np.linspace(-pre_trigger_sec, post_trigger_sec, samples_total)


#Calcula el W-time (temps de consciència subjectiva de la decisió), en segons
results_paths = [ os.path.normpath(p) for p in glob("C:/Users/david/OneDrive/Documentos/GitHub/OpenBrains/Libet/*/*_resultats.csv")]
all_times = []
# 3. Recorrem cada fitxer i recollim les diferències
for path in results_paths:
	df = pd.read_csv(path)
	differences = df['difference_sec'].dropna().tolist()
	all_times.extend(differences)

mean_w_time = sum(all_times) / len(all_times)
print(f"✅ W-time mitjà (difference_sec): {mean_w_time:.3f} segons")





# --- Gràfica ---
plt.figure(figsize=(10, 4))
# Dibuixa les mitjanes individuals (amb línia fina i semitransparent)
for subj_mean in all_subject_means:
    plt.plot(time_axis, subj_mean * 1e6, color='gray', linewidth=0.7, alpha=0.5)

# Dibuixa la mitjana grupal
plt.plot(time_axis, mean_potential * 1e6, label="Mitjana grupal", color='blue', linewidth=2)
# Interval de confiança del 95%
plt.fill_between(time_axis,
                 (mean_potential - ci95) * 1e6,
                 (mean_potential + ci95) * 1e6,
                 color='blue', alpha=0.3, label="IC 95%")

# Línies de referència
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(0, color='red', linestyle='--', label='Pulsació')
plt.axvline(mean_w_time, color='orange', linestyle='--', label='W-time (decisió conscient)')
# Estètica
plt.title("Potencial evocat grupal")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitud (µV)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)



# --- Paràmetres ---
threshold_uV = -0.5  # mínim descens considerat com a RP (en µV)
min_duration = 0.2   # mínim durada que es manté sota el llindar (segons)

# --- Convertim mean_potential a µV i definim eix de temps ---
mean_uV = mean_potential * 1e6  # passem a microvolts
samples_total = mean_potential.shape[0]
time_axis = np.linspace(-pre_trigger_sec, post_trigger_sec, samples_total)

# --- Detectar inici del RP (quan baixa per sota el llindar i s’hi manté) ---
under_thresh = mean_uV < threshold_uV
min_samples = int(min_duration * fs)

rp_start_index = None
for i in range(len(under_thresh) - min_samples):
    if np.all(under_thresh[i:i+min_samples]):
        rp_start_index = i
        break

rp_start_time = time_axis[rp_start_index] if rp_start_index else None

# --- Ajust lineal al tram inicial (per il·lustrar canvi progressiu) ---
fit_range = int(0.3 * fs)  # 300ms
if rp_start_index and rp_start_index + fit_range < len(mean_uV):
    slope, intercept, r_value, p_value, std_err = linregress(
        time_axis[rp_start_index:rp_start_index + fit_range],
        mean_uV[rp_start_index:rp_start_index + fit_range]
    )
    fit_line = intercept + slope * time_axis
else:
    fit_line = None

# --- Gràfica amb tot ---
plt.figure(figsize=(10, 5))
plt.plot(time_axis, mean_uV, label='ERP mitjà', color='navy')
plt.axvline(0, color='red', linestyle='--', label='Pulsació')
plt.axvline(mean_w_time, color='orange', linestyle='--', label='W-time (decisió conscient)')
plt.axhline(threshold_uV, color='gray', linestyle=':', label=f'Llindar {threshold_uV} µV')

if rp_start_index:
    plt.axvline(rp_start_time, color='green', linestyle='--', label=f'Inici RP: {rp_start_time:.3f}s')
    if fit_line is not None:
        plt.plot(time_axis, fit_line, color='purple', linestyle=':', label='Ajust lineal')

plt.title("Detecció de l'inici del potencial de preparació (RP)")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitud (µV)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show(block=False)

