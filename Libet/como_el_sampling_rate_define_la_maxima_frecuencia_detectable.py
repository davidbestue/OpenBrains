# -*- coding: utf-8 -*-
"""
Anàlisi de potencial evocat (EEG Libet)
@author: Open Brains
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


# Paràmetres de l'ona
f_ona = 10  # Hz
durada = 10  # segon
t_fina = np.linspace(0, durada, 1000)  # temps d'alta resolució
ona = np.sin(2 * np.pi * f_ona * t_fina)  # ona contínua de 10 Hz

# Freqüències de mostreig a comparar
fs_list = [15, 20, 25, 60]  # 1.5x, 2x i 4x mostres per cicle

# Funció per mostrar les gràfiques
plt.figure(figsize=(12, 8))
for i, fs in enumerate(fs_list, 1):
    t_mostra = np.arange(0, durada, 1/fs)
    mostres = np.sin(2 * np.pi * f_ona * t_mostra)
    #
    # Interpolació
    interp_func = interp1d(t_mostra, mostres, kind='cubic', fill_value="extrapolate")
    ona_interp = interp_func(t_fina)
    #
    plt.subplot(len(fs_list), 1, i)
    plt.plot(t_fina, ona, label='Ona real (10 Hz)', color='lightgray')
    plt.plot(t_fina, ona_interp, 'r', label='Ona reconstruïda')
    plt.stem(t_mostra, mostres, basefmt=" ", linefmt='r-', markerfmt='ro',
             label=f'Mostreig a {fs} Hz')
    plt.title(f'Mostreig a {fs} Hz ({fs/f_ona:.1f} mostres per cicle)')
    plt.xlabel('Temps (s)')
    plt.ylabel('Amplitud')
    plt.ylim(-1,1)
    plt.xlim(0,1)
    plt.grid(True)
    plt.legend(loc=4)
    
#
#


plt.tight_layout()
plt.show(block=False)
