# -*- coding: utf-8 -*-
"""
TASCA CONTROL
@author: David Bestue | Open Brains
"""




"""
SSVEP 12 Hz test - PsychoPy + numpy
Mostrado de pico a ~12 Hz para validar EEG en Oz.
Autor: Open Brains
"""
import time, math, csv
import numpy as np
from collections import deque
from psychopy import visual, core, event
import serial, serial.tools.list_ports
from datetime import datetime
import os
import threading


# --- DETECCIÓ DEL PORT USB SERIAL ---
puerto = None
baudrate = 230400
ports = serial.tools.list_ports.comports()
for port in ports:
    print(port.device, port.description)
    if 'USB Serial Device' in port.description:
        puerto = port.device
        print(f"Port trobat: {port.device}")

# --- INICIALITZACIÓ SERIAL ---
ser = None
if puerto:
    try:
        ser = serial.Serial(puerto, baudrate, timeout=1)
        print(f"Connectat a {puerto} a {baudrate} bauds")
        time.sleep(2)
    except serial.SerialException as e:
        print(f"Error de connexió EEG: {e}")
        ser = None



# ======== PARÁMETROS EEG ========
FS_HINT = 250                 # Hz esperados (si no conoces exacto, estimaremos online)
WIN_SEC = 2.0                 # ventana para FFT (s)
F_TARGET = 12.0               # Hz de flicker
F_SHOW_MIN, F_SHOW_MAX = 6.0, 30.0

# ======== PARÁMETROS EXPERIMENTO ========
BLOCK_FLICKER = 10.0          # s ON
BLOCK_REST    = 10.0          # s OFF
N_CYCLES      = 3
FULLSCR       = True

# ======== INICIALIZACIÓN ========
win = visual.Window(size=[1200, 800], color='black', units='pix', fullscr=FULLSCR)
txt = visual.TextStim(win, text='', color='white', pos=(0, 320), height=32, wrapWidth=1000)

# Estímulo: tablero/cuadro central que invierte polaridad
size = 500
stim = visual.Rect(win, width=size, height=size, fillColor='white', lineColor=None)
bg   = visual.Rect(win, width=size, height=size, fillColor='black', lineColor=None)  # para invertir
grey = visual.Rect(win, width=size, height=size, fillColor=[0,0,0], lineColor=None)  # gris (0 en rgb255)

# Gráfica rápida: barra de potencia 12 Hz
bar_bg = visual.Rect(win, width=300, height=30, pos=(0, -330), fillColor=[-0.5,-0.5,-0.5], lineColor=None)
bar_ok = visual.Rect(win, width=1, height=30, pos=(-150, -330), anchor='left', fillColor='green', lineColor=None)
label12 = visual.TextStim(win, text='Potencia ~12 Hz', color='white', pos=(0, -290), height=22)

# Buffer de datos crudos
buf_sec = 5.0
bufN = int(FS_HINT*buf_sec)
raw_buf = deque(maxlen=max(1, bufN))
ts_buf  = deque(maxlen=max(1, bufN))

# Serie
ser = None
if puerto:
    try:
        ser = serial.Serial(puerto, baudrate, timeout=0.001)
        time.sleep(2.0)
        ser.reset_input_buffer()
        print(f">> Conectado a {puerto} @ {baudrate}")
    except Exception as e:
        print("No se pudo abrir el puerto serie:", e)

# Utilidades
clock = core.Clock()
exp_clock = core.Clock()

def read_one_sample():
    """Lee una muestra float del puerto. Adapta si tu ADC manda enteros."""
    if ser is None:
        return None
    line = ser.readline()
    if not line:
        return None
    try:
        return float(line.strip())
    except:
        return None

def estimate_fs(ts):
    """Estimación robusta de FS por diferencias temporales medianas."""
    if len(ts) < 10:
        return FS_HINT
    dt = np.diff(ts)
    if np.any(dt <= 0):
        dt = dt[dt > 0]
    if len(dt) == 0:
        return FS_HINT
    return 1.0 / np.median(dt)

def hann(n):
    return 0.5 - 0.5*np.cos(2*np.pi*np.arange(n)/max(1,(n-1)))

def power_at(freqs, pxx, f0, bw=0.5):
    """Potencia integrada en una ventanita +-bw alrededor de f0."""
    mask = (freqs >= (f0-bw)) & (freqs <= (f0+bw))
    if not np.any(mask):
        return 0.0
    return float(np.mean(pxx[mask]))

def compute_fft_features(x, fs):
    """FFT simple (sin SciPy). Devuelve freqs, pxx, potencia 12 Hz y espectro filtrado 6-30 Hz."""
    x = np.asarray(x, dtype=float)
    x = x - np.mean(x)
    n = len(x)
    w = hann(n)
    xw = x * w
    # FFT real
    X = np.fft.rfft(xw)
    pxx = (np.abs(X)**2) / np.sum(w**2)
    freqs = np.fft.rfftfreq(n, d=1.0/fs)
    # potencia en banda de interés
    p12 = power_at(freqs, pxx, F_TARGET, bw=0.3)
    # Subespectro 6-30 Hz
    mask = (freqs >= F_SHOW_MIN) & (freqs <= F_SHOW_MAX)
    return freqs[mask], pxx[mask], p12

# ======== RUTINA PRINCIPAL ========
def run_block(flicker_on=True, dur=10.0):
    global estado_actual
    if flicker_on:
        estado_actual = "flicker"
    else:
        estado_actual = "rest"
    #
    clock.reset()
    phase_on = True
    flip_int = 1.0/(2.0*F_TARGET)  # invertimos blanco/negro dos veces por ciclo -> 12 Hz
    next_flip_t = 0.0

    while clock.getTime() < dur:
        # Lectura rápida (varias por frame si hay)
        for _ in range(4):
            v = read_one_sample()
            if v is None:
                break
            tnow = exp_clock.getTime()
            raw_buf.append(v)
            ts_buf.append(tnow)

        # Estimación FS con timestamps
        fs_est = estimate_fs(list(ts_buf))

        # Bloque flicker o reposo
        if flicker_on:
            t = clock.getTime()
            if t >= next_flip_t:
                phase_on = not phase_on
                next_flip_t += flip_int
            # dibuja polaridad
            if phase_on:
                bg.draw(); stim.draw()
            else:
                stim.draw(); bg.draw()
            txt.text = f"Bloque FLICKER 12 Hz  |  FS≈ {fs_est:5.1f} Hz"
        else:
            grey.draw()
            txt.text = f"Bloque REPOSO (gris)  |  FS≈ {fs_est:5.1f} Hz"

        # Espectro y barra de potencia
        txt.draw()
        bar_bg.draw()
        p12 = 0.0
        if len(raw_buf) >= int(max(0.5, WIN_SEC)*fs_est):
            N = int(min(len(raw_buf), WIN_SEC*fs_est))
            x = np.array(list(raw_buf)[-N:], dtype=float)
            fre, pxx, p12 = compute_fft_features(x, fs_est)
            # Escala de barra (auto, robusta)
            # baseline = mediana del subespectro
            baseline = np.median(pxx) + 1e-12
            ratio = np.clip((p12 / baseline), 0.0, 8.0)   # limitado para barra
            bar_ok.width = 300 * (ratio/8.0)
            bar_ok.pos = (-150, -330)
            bar_ok.draw()
        label12.text = f"Potencia @12 Hz (relativa): {p12:.2e}"
        label12.draw()

        # teclas
        if 'escape' in event.getKeys():
            core.quit()

        win.flip()





#### EXPERIMENTO Y REGISTRO



estado_actual = "none"   # global

# --- buffers y control ---
datos_eeg = []
running = True

# --- función de lectura continua ---
def llegir_eeg_continu():
    global running, estado_actual
    while running:
        if ser and ser.in_waiting:
            try:
                linea = ser.readline().decode('utf-8').strip()
                if linea:
                    t_global = exp_clock.getTime()   # usa el mismo reloj que el experimento
                    datos_eeg.append(f"{t_global:.4f},{linea},{estado_actual}")
            except Exception:
                continue

# --- iniciar el hilo de lectura antes de la secuencia de bloques ---
eeg_thread = threading.Thread(target=llegir_eeg_continu, daemon=True)
eeg_thread.start()


# Instrucciones
txt.text = ("TEST SSVEP 12 Hz\n\n"
            "Coloca electrodos: señal ROJO en Oz, referencia AZUL en mastoides, tierra NEGRO en Fpz.\n"
            "Verás bloques de 10 s: patrón parpadeante (12 Hz) y reposo. \n"
            "Durante el parpadeo debe subir la potencia ~12 Hz.\n\n"
            "Pulsa ESPACIO para comenzar.")
txt.draw(); win.flip()
event.waitKeys(keyList=['space'])
event.clearEvents()


# Secuencia de bloques
for i in range(N_CYCLES):
    run_block(flicker_on=True, dur=BLOCK_FLICKER)
    run_block(flicker_on=False, dur=BLOCK_REST)

# Cierre
txt.text = "Fin del test. ¿Has visto la barra crecer en 12 Hz durante el flicker?\nPulsa cualquier tecla para salir."
txt.draw(); win.flip()
event.waitKeys()
win.close()


# detener hilo y guardar datos
running = False
eeg_thread.join(timeout=1.0)

out_file = f"ssvep_raw_{time.strftime('%Y%m%d_%H%M%S')}.csv"
with open(out_file, 'w', encoding='utf-8') as f:
    f.write("time_s,value,state\n")
    for row in datos_eeg:
        f.write(row + "\n")

print(f">> Guardado EEG continuo en {out_file}")



# ========= ANÁLISIS RÁPIDO INTEGRADO =========


# ========= ANÁLISIS RÁPIDO INTEGRADO (SIN FUNCIÓN) =========
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# --- Parámetros de visualización / RMS ---
WIN_SEC = 1.0  # ventana RMS en segundos (ajusta a gusto)

# --- Carga robusta del CSV ---
df = pd.read_csv(out_file)  # usa la ruta que acabas de guardar
# normaliza nombres
df.columns = [c.strip().lower() for c in df.columns]

# verifica columnas
required = {'time_s','value','state'}
if not required.issubset(set(df.columns)):
    raise ValueError(f"Faltan columnas. Se esperaban: {required}, y hay: {set(df.columns)}")

# fuerza numéricos y elimina filas inválidas
df['time_s'] = pd.to_numeric(df['time_s'], errors='coerce')
df['value']  = pd.to_numeric(df['value'],  errors='coerce')
df = df.dropna(subset=['time_s','value']).reset_index(drop=True)

# limpia 'state': a minúsculas, sin espacios, mapeo a {flicker, rest, none}
state_raw = df['state'].astype(str).str.strip().str.lower()
state_map = {'flicker':'flicker', 'rest':'rest', 'none':'none'}
df['state'] = state_raw.map(state_map).fillna('none')  # cualquier cosa rara -> none

# extrae arrays
t = df['time_s'].to_numpy(dtype=float)
v = df['value'].to_numpy(dtype=float)
s = df['state'].to_numpy(dtype=str)

# --- Estima Fs y prepara RMS ---
dt = np.diff(t); dt = dt[dt > 0]
fs = 1.0 / np.median(dt) if len(dt) else 250.0
win = max(1, int(round(WIN_SEC * fs)))

def moving_rms(x, win_samples):
    if win_samples <= 1:
        return np.abs(x)
    sq = x**2
    k = np.ones(win_samples) / win_samples
    return np.sqrt(np.convolve(sq, k, mode='same'))

rms = moving_rms(v, win)

# --- Resumen por estado (RMS medio) ---
order_states = ['none', 'rest', 'flicker']  # orden lógico para mostrar
present_states = [st for st in order_states if np.any(s == st)]
by_state = {st: float(np.nanmean(rms[s == st])) for st in present_states}

print(f"Fs estimada: {fs:.2f} Hz | ventana RMS: {win} muestras (~{WIN_SEC:.2f} s)")
for st in present_states:
    print(f"  {st:>7s} -> RMS medio = {by_state[st]:.4g} | n={np.sum(s==st)}")

# --- Gráfico temporal con fondos por estado (colores fuertes + etiquetas) ---
color_fill = {
    'flicker': (0.20, 0.45, 1.00, 0.35),  # azul intenso translúcido
    'rest':    (1.00, 0.30, 0.30, 0.30),  # rojo translúcido
    'none':    (0.60, 0.60, 0.60, 0.25)   # gris translúcido
}


plt.figure(figsize=(12, 6))
plt.plot(t, rms, linewidth=1.6, label=f'RMS ~{WIN_SEC:.1f}s')
# detectar cambios de estado y segmentar
change_idx = np.where(s[1:] != s[:-1])[0] + 1
segments = np.r_[0, change_idx, len(s)]
#y_top = np.nanmax(rms) if np.isfinite(np.nanmax(rms)) else 1.0

for i in range(len(segments)-1):
    st = s[segments[i]]
    t0, t1 = t[segments[i]], t[segments[i+1]-1]
    plt.axvspan(t0, t1, color=color_fill.get(st, color_fill['none']), linewidth=0)

# leyenda de zonas
legend_patches = [Patch(facecolor=color_fill[st], edgecolor='none', label=st) for st in present_states]
plt.legend([*legend_patches], [st for st in present_states], loc='upper left', title='Estado', framealpha=0.9)
plt.xlabel("Tiempo (s)")
plt.ylabel("RMS (u.a.)")
plt.title("Energía (RMS) por tiempo con estados")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show(block=False)

# --- Barras comparando estados (mismos colores) ---
plt.figure(figsize=(6, 4))
bars = [by_state[st] for st in present_states]
bar_colors = [color_fill[st][:3] for st in present_states]  # sin alpha para barras
plt.bar(present_states, bars, color=bar_colors)
plt.ylabel("RMS medio")
plt.title("RMS medio por estado")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

plt.show(block=False)
# ========= FIN ANÁLISIS =========


