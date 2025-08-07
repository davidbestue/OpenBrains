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


def carregar_epochs_des_de_carpeta(folder_path, fs=256, pre_trigger_sec=3, export_epochs=True):
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
    eeg_signal = np.array(eeg_signal, dtype=np.float32)

    # --- FILTRAT (Notch + Bandpass) ---
    b_notch, a_notch = signal.iirnotch(50, 10, fs)
    eeg_filtered = signal.filtfilt(b_notch, a_notch, eeg_signal)
    b_band, a_band = signal.butter(2, [1/(fs/2), 38/(fs/2)], btype='band')
    eeg_filtered = signal.filtfilt(b_band, a_band, eeg_filtered)

    # --- INTERPOLACIÓ A MOSTREIG REGULAR ---
    start_time = timestamps[0]
    end_time = timestamps[-1]
    uniform_times = np.arange(start_time, end_time, 1/fs)
    eeg_uniform = np.interp(uniform_times, timestamps, eeg_filtered)

    # --- CARREGA EVENTS ---
    events = pd.read_csv(os.path.join(folder_path, events_file))
    keypress_times = events[events["event"].str.contains("keypress")]["time"].values

    # --- EPOCHING ---
    samples_before = int(pre_trigger_sec * fs)
    epochs = []

    for t_event in keypress_times:
        if t_event - pre_trigger_sec < uniform_times[0] or t_event > uniform_times[-1]:
            continue
        idx_end = np.searchsorted(uniform_times, t_event)
        idx_start = idx_end - samples_before
        if idx_start < 0:
            continue
        epoch = eeg_uniform[idx_start:idx_end]
        if len(epoch) == samples_before:
            epochs.append(epoch)

    if len(epochs) == 0:
        print("\n⚠️ No s'han trobat epochs vàlids.")
        return None

    epochs = np.array(epochs)

    # --- BASELINE CORRECTION ---
    baseline_window = int(0.2 * fs)  # primers 200 ms de cada eopch
    baseline = np.mean(epochs[:, :baseline_window], axis=1, keepdims=True)
    epochs = epochs - baseline

    # --- FILTRAT D'OUTLIERS ---
    threshold_uV = 100  # µV
    epochs_uV = epochs * 1e6
    mask = np.max(np.abs(epochs_uV), axis=1) < threshold_uV
    epochs = epochs[mask]

    if export_epochs:
        np.save(os.path.join(folder_path, "epochs.npy"), epochs)

    # --- GRAFICACIÓ POTENCIAL EVOCAT AMB SEM ---
    time_axis = np.linspace(-pre_trigger_sec, 0, samples_before)
    mean_potential = np.mean(epochs, axis=0)
    sem = np.std(epochs, axis=0) / np.sqrt(epochs.shape[0])

    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, mean_potential * 1e6, label="Mitjana")
    plt.fill_between(time_axis, (mean_potential - sem) * 1e6, (mean_potential + sem) * 1e6,
                     color='blue', alpha=0.3, label="±1 SEM")
    plt.axvline(0, color='r', linestyle='--', label='Pulsació')
    plt.title("Potencial evocat mitjà (3s abans de la decisó)")
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitud (µV)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # --- ESPECTROGRAMA ---
    fig = yasa.plot_spectrogram(mean_potential, sf=fs, fmin=0, fmax=60, cmap='Spectral_r')

    return epochs


# --- EXEMPLE D'EXECUCIÓ ---
if __name__ == "__main__":
    folder = "C:/Users/david/OneDrive/Documentos/GitHub/OpenBrains/Libet/2025-08-04_10-35-13_dani"  # o el path on tens les dades del participant
    carregar_epochs_des_de_carpeta(folder)
