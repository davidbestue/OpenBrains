# -*- coding: utf-8 -*-
"""
Anàlisi de potencial evocat (EEG Libet)
@author: Open Brains
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- Simulació de la senyal EEG ---
fs = 200  # Hz
durada = 5  # segons
t_regular = np.linspace(0, durada, int(fs * durada), endpoint=False)

# Senyal amb 10 Hz + soroll
eeg_original = np.sin(2 * np.pi * 10 * t_regular) + np.random.randn(len(t_regular)) * 0.1

# Simulem timestamps irregulars
np.random.seed(0)
t_irregular = t_regular + np.random.uniform(-0.002, 0.002, size=len(t_regular))
t_irregular = np.clip(t_irregular, 0, durada)
t_irregular = np.sort(t_irregular)

# Interpolació sobre temps regulars
t_uniform = np.linspace(0, durada, int(fs * durada), endpoint=False)
eeg_interpolada = np.interp(t_uniform, t_irregular, eeg_original)

# --- Gràfica comparativa ---
plt.figure(figsize=(14, 4))
plt.plot(t_irregular, eeg_original, label='Original (irregular)', color='orange')
plt.plot(t_uniform, eeg_interpolada, label='Interpolada (regular)', color='darkblue')
plt.xlabel("Temps (s)")
plt.ylabel("Amplitud (a.u.)")
plt.title("Senyal EEG pre i post interpolació")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)
