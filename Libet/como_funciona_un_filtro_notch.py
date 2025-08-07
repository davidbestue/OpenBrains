# -*- coding: utf-8 -*-
"""
Anàlisi de potencial evocat (EEG Libet)
@author: Open Brains
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000  # Hz
t = np.linspace(0, 1, fs, endpoint=False)
senyal = np.sin(2 * np.pi * 50 * t) + np.random.randn(fs) * 0.1

# Disseny del filtre notch
f0 = 50  # Hz
Q = 30   # Factor de qualitat
b_notch, a_notch = signal.iirnotch(f0, Q, fs)

# Aplicació del filtre
senyal_filtrada = signal.filtfilt(b_notch, a_notch, senyal)

# Gràfica
plt.figure(figsize=(12, 5))
plt.plot(t, senyal, label='Senyal original (amb 50 Hz)', alpha=0.6)
plt.plot(t, senyal_filtrada, label='Senyal filtrada (notch 50 Hz)', linewidth=2)
plt.xlabel("Temps (s)")
plt.ylabel("Amplitud")
plt.title("Efecte del filtre Notch a 50 Hz")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()