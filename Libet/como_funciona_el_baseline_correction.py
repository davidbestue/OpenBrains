# -*- coding: utf-8 -*-
"""
Anàlisi de potencial evocat (EEG Libet)
@author: Open Brains
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulem 3 epochs amb la mateixa forma d'ona però amb baselines diferents
fs = 200  # Hz
pre_trigger = 1  # segons abans de l'esdeveniment
post_trigger = 1  # segons després de l'esdeveniment
t = np.linspace(-pre_trigger, post_trigger, int((pre_trigger + post_trigger) * fs), endpoint=False)
n_epochs = 3

# Onda simulada: potencial de preparació negatiu centrat a -0.2s
true_wave = -1e-6 * np.exp(-((t + 0.2) ** 2) / 0.02)

# Afegim diferents baselines artificials
baselines = [2e-6, -5e-6, 0]  # 10 µV, -5 µV, 0 µV
epochs = np.array([true_wave + b for b in baselines])

# Apliquem correcció de baseline (primers 200 ms)
baseline_window = int(0.2 * fs)  # primers 200 ms
baseline = np.mean(epochs[:, :baseline_window], axis=1, keepdims=True)
epochs_corrected = epochs - baseline

# Gràfiques
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# Gràfica 1: Senyals originals amb baselines diferents
for i in range(n_epochs):
    axs[0].plot(t, epochs[i] * 1e6, label=f"Epoch {i+1}")


axs[0].axhline(y=0, linestyle='--', color='black')
axs[0].set_title("Senyals originals amb baselines diferents")
axs[0].set_ylabel("Amplitud (µV)")
axs[0].set_ylim(-6,6)
axs[0].legend()
axs[0].grid(True)

# Gràfica 2: Mitjana sense correcció de baseline
mean_unfiltered = np.mean(epochs, axis=0)
axs[1].axhline(y=0, linestyle='--', color='black')
axs[1].plot(t, mean_unfiltered * 1e6, color='darkred')
axs[1].set_title("Mitjana dels epochs sense correcció de baseline")
axs[1].set_ylabel("Amplitud (µV)")
axs[1].set_ylim(-6,6)
axs[1].grid(True)

# Gràfica 3: Mitjana amb correcció de baseline
mean_corrected = np.mean(epochs_corrected, axis=0)
axs[2].plot(t, mean_corrected * 1e6, color='darkblue')
axs[2].axhline(y=0, linestyle='--', color='black')
axs[2].set_title("Mitjana dels epochs DESPRÉS de la correcció de baseline")
axs[2].set_xlabel("Temps (s)")
axs[2].set_ylabel("Amplitud (µV)")
axs[2].set_ylim(-6,6)
axs[2].grid(True)

plt.tight_layout()
plt.show(block=False)
