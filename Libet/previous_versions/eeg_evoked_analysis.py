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


def carregar_epochs_des_de_carpeta(folder_path, fs=200, pre_trigger_sec=0, export_epochs=True):
    """
    Carrega dades EEG i events, segmenta els 3s previs a "keypress" i retorna els epochs + figura.

    Parameters:
        folder_path (str): Ruta a la carpeta que conté els fitxers EEG i events
        fs (int): Freqüència de mostreig (Hz)
        pre_trigger_sec (int): Segons a agafar abans del keypress
        export_epochs (bool): Desa els epochs a .npy per a anàlisi posterior

    Returns:
        epochs (np.ndarray): Array [n_trials x n_samples] amb els segments
    """
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
    timestamps = np.array(timestamps)
    eeg_signal = np.array(eeg_signal)

    # --- FILTRAT (Notch + Bandpass) ---
    b_notch, a_notch = signal.iirnotch(50, 10, fs)
    eeg_filtered = signal.filtfilt(b_notch, a_notch, eeg_signal)
    b_band, a_band = signal.butter(2, [1/(fs/2), 38/(fs/2)], btype='band')
    eeg_filtered = signal.filtfilt(b_band, a_band, eeg_filtered)

    # --- CARREGA EVENTS ---
    events = pd.read_csv(os.path.join(folder_path, events_file))
    keypress_times = events[events["event"].str.contains("keypress")]["time"].values

    # --- EPOCHING ---
    samples_before = int(pre_trigger_sec * fs)
    epochs = []
    valid_events = 0

    for t_event in keypress_times:
        if t_event - pre_trigger_sec < timestamps[0]:
            continue
        mask = (timestamps >= t_event - pre_trigger_sec) & (timestamps < t_event)
        if np.sum(mask) == samples_before:
            epoch = eeg_filtered[mask]
            epochs.append(epoch)
            valid_events += 1

    if valid_events == 0:
        print("\n⚠️ No s'han trobat epochs vàlids.")
        return None

    epochs = np.array(epochs)

    # --- EXPORTACIÓ OPCIONAL ---
    if export_epochs:
        np.save(os.path.join(folder_path, "epochs.npy"), epochs)

    # --- GRAFICACIÓ ---
    time_axis = np.linspace(-pre_trigger_sec, 0, samples_before)
    mean_potential = np.mean(epochs, axis=0)

    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, mean_potential * 1e6)
    plt.axvline(0, color='r', linestyle='--', label='Pulsació')
    plt.title("Potencial evocat mitjà (3s abans de la decisió)")
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitud (\u00b5V)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return epochs


# --- EXEMPLE D'EXECUCIÓ ---
if __name__ == "__main__":
    folder = "C:/Users/david/OneDrive/Documentos/GitHub/OpenBrains/Libet/2025-08-04_09-44-19_peterson"  # o el path on tens les dades del participant
    carregar_epochs_des_de_carpeta(folder)
