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
from psychopy.visual import ShapeStim



# --- DETECCIÓ DEL PORT USB SERIAL ---
puerto = None
baudrate = 230400
ports = serial.tools.list_ports.comports()
for port in ports:
    print(port.device, port.description)
    if 'Arduino' in port.description:     #if 'USB Serial Device' in port.description:
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
FS_HINT = 90                 # Hz esperados (si no conoces exacto, estimaremos online)
WIN_SEC = 2.0                 # ventana para FFT (s)
F_TARGET = 12.0               # Hz de flicker
F_SHOW_MIN, F_SHOW_MAX = 6.0, 30.0

# ======== PARÁMETROS EXPERIMENTO ========
BLOCK_FLICKER = 20.0          # s ON
BLOCK_REST    = 20.0          # s OFF
N_CYCLES      = 3
FULLSCR       = True

# ======== INICIALIZACIÓN ========
win = visual.Window(size=[1200, 800], color='black', units='pix', fullscr=FULLSCR)
txt = visual.TextStim(win, text='', color='white', pos=(0, 320), height=32, wrapWidth=1000)

# Estímulo: tablero/cuadro central que invierte polaridad
win.mouseVisible = False
size = 500
stim = visual.Rect(win, width=size, height=size, fillColor='white', lineColor=None)
bg   = visual.Rect(win, width=size, height=size, fillColor='black', lineColor=None)  # para invertir
grey = visual.Rect(win, width=size, height=size, fillColor=[0,0,0], lineColor=None)  # gris (0 en rgb255)

# Crear cruz simple en el centro
fix_cross = visual.ShapeStim(
    win=win,
    vertices='cross',
    size=(0.05, 0.05),  # Tamaño pequeño (≈4px)
    lineColor='black',
    fillColor='black',
    lineWidth=2,
    pos=(0, 0)
)


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
                fix_cross.draw()
                bg.draw(); stim.draw()
            else:
                
                stim.draw(); bg.draw()
            txt.text = f"Bloque FLICKER 12 Hz  |  FS≈ {fs_est:5.1f} Hz"
        else:
            grey.draw()
            txt.text = f"Bloque REPOSO (gris)  |  FS≈ {fs_est:5.1f} Hz"

        # Espectro y barra de potencia
        #txt.draw()
        #bar_bg.draw()
        fix_cross.draw()
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
            #bar_ok.draw()
        label12.text = f"Potencia @12 Hz (relativa): {p12:.2e}"
        #label12.draw()

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
# txt.text = ("TEST SSVEP 12 Hz\n\n"
#             "Coloca electrodos: señal ROJO en Oz, referencia AZUL en mastoides, tierra NEGRO en Fpz.\n"
#             "Verás bloques de 10 s: patrón parpadeante (12 Hz) y reposo. \n"
#             "Durante el parpadeo debe subir la potencia ~12 Hz.\n\n"
#             "Pulsa ESPACIO para comenzar.")

txt.text = ("TEST SSVEP 12 Hz\n\n"
            "Coloca electrodos: señal ROJO en Oz, referencia NEGRO en Fpz, ground AZUL en mastoide.\n"
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



# ###SON NUMEROS EN BINARIOS Y NO ESTÁ SIGNED
# #
# #[i if (i&(1<<23)) == 0 else i-2*(1<<23) for i in out_file] (!!!!!!!!)

