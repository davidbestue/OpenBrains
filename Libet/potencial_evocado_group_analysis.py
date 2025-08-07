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
# Estètica
plt.title("Potencial evocat grupal")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitud (µV)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)

