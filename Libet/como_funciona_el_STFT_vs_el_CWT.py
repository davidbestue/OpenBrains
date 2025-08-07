# -*- coding: utf-8 -*-
"""
Anàlisi de potencial evocat (EEG Libet)
@author: Open Brains
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
import pywt

# --- Senyal sintètica ---
fs = 500  # Hz
t = np.linspace(0, 2, int(2 * fs), endpoint=False)
signal = np.sin(2 * np.pi * 10 * t)  # Ona de 10 Hz

# Afegim burst de 20 Hz entre 1.4 i 1.6 s
burst = (t > 1.4) & (t < 1.6)
signal[burst] += 0.7 * np.sin(2 * np.pi * 20 * t[burst])

# --- STFT ---
f_stft, t_stft, Sxx = spectrogram(signal, fs=fs, nperseg=128, noverlap=64)
Sxx_dB = 10 * np.log10(Sxx + 1e-10)

# --- CWT amb Morlet ---
scales = np.arange(1, 128)
coeffs, freqs = pywt.cwt(signal, scales, 'cmor1.5-1.0', sampling_period=1/fs)
power_cwt = np.abs(coeffs) ** 2

# --- Visualització ---
fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# STFT
pcm1 = axs[0].pcolormesh(t_stft, f_stft, Sxx_dB, shading='gouraud', cmap='Spectral_r')
axs[0].set_title("Espectrograma (STFT)")
axs[0].set_ylabel("Freqüència (Hz)")
axs[0].set_ylim(0, 60)
axs[0].axvline(1.4, color='k', linestyle='--')
axs[0].axvline(1.6, color='k', linestyle='--')
fig.colorbar(pcm1, ax=axs[0], label='Potència (dB)')

# CWT
pcm2 = axs[1].pcolormesh(t, freqs, power_cwt, shading='gouraud', cmap='Spectral_r')
axs[1].set_title("Transformada Wavelet Contínua (CWT)")
axs[1].set_xlabel("Temps (s)")
axs[1].set_ylabel("Freqüència (Hz)")
axs[1].set_ylim(0, 60)
axs[1].axvline(1.4, color='k', linestyle='--')
axs[1].axvline(1.6, color='k', linestyle='--')
fig.colorbar(pcm2, ax=axs[1], label='Potència')

plt.tight_layout()
plt.show(block=False)

