# -*- coding: utf-8 -*-
"""
LIBET - EEG INTEGRAT CONTINU
@author: David Bestue | Open Brains
"""
import numpy as np
from psychopy import visual, core, event
import pandas as pd
import time
from datetime import datetime
import serial.tools.list_ports
import serial
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

# --- PARÀMETRES ---
rotation_duration = 2.56
clock_radius = 250

# --- INICIALITZACIÓ PANTALLA ---
win = visual.Window(size=[800, 800], color='black', units='pix', fullscr=True)
mouse = event.Mouse(visible=True, win=win)
experiment_clock = core.Clock()
results = []
markers = []


# --- ESTÍMULS CONSTANTS ---
circle = visual.Circle(win, radius=clock_radius, edges=128, lineColor='white', fillColor=None)
hand = visual.Line(win, start=(0, 0), end=(0, clock_radius), lineColor='red', lineWidth=3)
marks = []
for i in range(12):
    angle = 2 * np.pi * (i / 12)
    x = np.sin(angle) * (clock_radius + 20)
    y = np.cos(angle) * (clock_radius + 20)
    mark = visual.TextStim(win, text=str(i), pos=(x, y), color='white', height=24)
    marks.append(mark)



# --- FUNCIONS DE LECTURA EEG CONTÍNUA ---
datos_eeg = []
running = True
def llegir_eeg_continu():
    while running:
        if ser and ser.in_waiting:
            try:
                linea = ser.readline().decode('utf-8').strip()
                if linea:
                    t_global = experiment_clock.getTime()
                    datos_eeg.append(f"{t_global:.4f},{linea}")
            except:
                continue

# --- INICI LECTURA EEG EN FIL ---
eeg_thread = threading.Thread(target=llegir_eeg_continu)
eeg_thread.start()

# --- INTRO PARTICIPANT ---
intro = visual.TextStim(win, text="Abans de començar, introdueix les teves dades:", pos=(0, 300), color='white', height=30)
instructions = visual.TextStim(win, text="Prem ENTER per passar al següent camp", pos=(0, -300), color='grey', height=20)
fields = ['Nom', 'Edat']
responses = ['', '']
current_field = 0
field_texts = [visual.TextStim(win, text='', pos=(0, 150 - 75*i), color='white', height=28) for i in range(len(fields))]
while True:
    keys = event.getKeys()
    for key in keys:
        if key == 'return':
            if current_field < len(fields) - 1:
                current_field += 1
            else:
                participant_name = responses[0].strip().replace(" ", "_")
                participant_age = responses[1].strip()
                win.flip()
                core.wait(0.5)
                break
        elif key == 'backspace':
            responses[current_field] = responses[current_field][:-1]
        elif key == 'space':
            responses[current_field] += ' '
        elif len(key) == 1:
            responses[current_field] += key
    else:
        intro.draw()
        instructions.draw()
        for i, field in enumerate(fields):
            prefix = "> " if i == current_field else "  "
            field_texts[i].text = f"{prefix}{field}: {responses[i]}"
            field_texts[i].draw()
        win.flip()
        continue
    break

# --- GÈNERE ---
gender_options = ['Home', 'Dona', 'No binari', 'Prefereixo no dir-ho']
gender_prompt = visual.TextStim(win, text="Selecciona el teu gènere:\n\n[1] Home\n[2] Dona\n[3] No binari\n[4] Prefereixo no dir-ho", pos=(0, 0), color='white', height=28, alignText='center')
gender_instructions = visual.TextStim(win, text="Prem una tecla del 1 al 4 per seleccionar", pos=(0, -250), color='grey', height=20)
while True:
    gender_prompt.draw()
    gender_instructions.draw()
    win.flip()
    keys = event.waitKeys()
    if keys[0] in ['1', '2', '3', '4']:
        participant_gender = gender_options[int(keys[0]) - 1]
        break
core.wait(0.5)

# --- CREAR CARPETA DE RESULTATS ---
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
safe_name = participant_name.strip().replace(" ", "_")
folder_name = f"{timestamp}_{safe_name}"
os.makedirs(folder_name, exist_ok=True)

# --- INSTRUCCIONS INICIALS ---
instructions_text = """
INSTRUCCIONS

A la pantalla veuràs un rellotge amb una única agulla vermella que gira de forma contínua en sentit horari. L’agulla fa una volta completa cada 2.56 segons.

Quan tu vulguis, prem la barra espaiadora.

Però atenció: el més important no és quan prems, sinó QUAN DECIDEIXES fer-ho.

Després de prémer, el rellotge s’aturarà i et demanarem que facis clic sobre el punt del rellotge on creus que estava l’agulla en el moment precís en què has decidit prémer la tecla (no quan l’has premut físicament, sinó quan has sentit la voluntat de fer-ho).

Quan facis clic, apareixerà una agulla verda durant 2 segons, mostrant la teva resposta. Un cop desaparegui, la tasca torna a començar.

Fes-ho de forma natural, sense pressa. Pots repetir la tasca tantes vegades com vulguis. Per acabar l’experiment, prem la tecla “Esc”.

Prem qualsevol tecla per començar.
"""
instructions = visual.TextStim(win, text=instructions_text, color='white', height=24, wrapWidth=700, alignText='left')
instructions.draw()
win.flip()
event.waitKeys()

# --- LOOP PRINCIPAL ---
experiment_clock.reset()
running_loop = True
while running_loop:
    start_relax = experiment_clock.getTime()
    markers.append((start_relax, f"start_relax{len(results)+1}"))
    pause_message = visual.TextStim(win, text="Estigues relaxat/da i no et moguis durant uns segons...", color='white', height=30, wrapWidth=1000)
    pause_message.draw()
    win.flip()
    pause_duration = np.random.uniform(3, 6)
    core.wait(pause_duration)
    #
    start_trial = experiment_clock.getTime()
    markers.append((start_trial, f"start_trial{len(results)+1}"))

    while True:
        t = experiment_clock.getTime()
        angle_deg = (t % rotation_duration) / rotation_duration * 360
        angle_rad = np.deg2rad(angle_deg)
        hand = visual.Line(win, start=(0, 0), end=(np.sin(angle_rad) * clock_radius, np.cos(angle_rad) * clock_radius), lineColor='red', lineWidth=3)
        circle.draw()
        hand.draw()
        for mark in marks:
            mark.draw()
        win.flip()

        keys = event.getKeys()
        if 'escape' in keys:
            running_loop = False
            break
        if 'space' in keys:
            real_time = t
            real_angle = angle_deg % 360
            markers.append((real_time, f"keypress_trial{len(results)+1}"))
            break

    if not running_loop:
        break

    instruccio = visual.TextStim(win, text="Fes clic al punt del cercle on creus que estava l’agulla\nquan vas decidir prémer.", color='white', height=24, wrapWidth=700, pos=(0, -300))
    circle.draw()
    for mark in marks:
        mark.draw()
    instruccio.draw()
    win.flip()
    core.wait(2.0)

    clicked = False
    while not clicked:
        mouse.clickReset()
        circle.draw()
        for mark in marks:
            mark.draw()
        win.flip()
        buttons, _ = mouse.getPressed(getTime=True)
        if buttons[0]:
            pos = mouse.getPos()
            x_click, y_click = pos
            dist = np.sqrt(x_click**2 + y_click**2)
            if dist <= clock_radius + 30:
                clicked = True

    markers.append((experiment_clock.getTime(), f"estimatedtimeclick_trial{len(results)+1}"))

    angle_click = (np.degrees(np.arctan2(x_click, y_click)) + 360) % 360
    angle_diff = ((angle_click - real_angle + 180) % 360) - 180
    time_diff = (angle_diff / 360) * rotation_duration
    estimated_real_time = real_time + time_diff

    feedback_hand = visual.Line(win, start=(0, 0), end=(np.sin(np.deg2rad(angle_click)) * clock_radius, np.cos(np.deg2rad(angle_click)) * clock_radius), lineColor='green', lineWidth=4)
    circle.draw()
    feedback_hand.draw()
    for mark in marks:
        mark.draw()
    win.flip()
    core.wait(1.5)

    results.append({
        'participant': participant_name,
        'age': participant_age,
        'gender': participant_gender,
        'real_angle': round(real_angle, 2),
        'real_time': round(real_time, 4),
        'angle_click': round(angle_click, 2),
        'estimated_time': round(estimated_real_time, 4),
        'difference_sec': round(time_diff, 4)
    })

# --- ATURAR EEG I GUARDAR ---
running = False
eeg_thread.join()

eeg_file = os.path.join(folder_name, f"{safe_name}_EEG_continu.txt")
with open(eeg_file, 'w') as f:
    for line in datos_eeg:
        f.write(line + '\n')

event_file = os.path.join(folder_name, f"{safe_name}_events.csv")
pd.DataFrame(markers, columns=['time','event']).to_csv(event_file, index=False)

# --- GUARDAR DADES FINALS ---
df = pd.DataFrame(results)
output_csv = os.path.join(folder_name, f"{safe_name}_resultats.csv")
df.to_csv(output_csv, index=False)

final_msg = visual.TextStim(win, text="Resultats desats.\nGràcies per participar.", color='white', height=25)
final_msg.draw()
win.flip()
core.wait(2)
win.close()
core.quit()
