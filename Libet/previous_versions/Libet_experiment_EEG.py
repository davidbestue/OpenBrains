# -*- coding: utf-8 -*-
"""
LIBET - EEG

@author: David Bestue | Open Brains
"""
import numpy as np
from psychopy import visual, core, event
import pandas as pd
import time
from datetime import datetime
import serial.tools.list_ports
import serial



# --- CONECTAR EEG
ports = serial.tools.list_ports.comports()
for port in ports:
    print(port.device, port.description)
    if 'USB Serial Device' in port.description:
        puerto = port.device
        print(f"Puerto encontrado: {port.device}")


# Configura el puerto serie
#puerto = 'COM6'  # En Windows. En Linux/Mac sería '/dev/ttyUSB0' o similar
baudrate = 230400  # Cambia a 115200 si actualizas tu Arduino

try:
    ser = serial.Serial(puerto, baudrate, timeout=1)
    print(f"Conectado a {puerto} a {baudrate} baudios")
    time.sleep(2)
except serial.SerialException as e:
    print(f"Error al conectar al EEG: {e}")
    ser = None




# --- PARÀMETRES EXPERIMENT ---
rotation_duration = 2.56  # segons per volta completa
clock_radius = 250

# --- INICIALITZACIÓ ---
win = visual.Window(size=[800, 800], color='black', units='pix', fullscr=True)
mouse = event.Mouse(visible=True, win=win)
experiment_clock = core.Clock()
results = []

# --- ESTÍMULS CONSTANTS ---
circle = visual.Circle(win, radius=clock_radius, edges=128, lineColor='white', fillColor=None)
hand = visual.Line(win, start=(0, 0), end=(0, clock_radius), lineColor='red', lineWidth=3)


# Marques (només visuals, no clicables)
marks = []
for i in range(12):
    angle = 2 * np.pi * (i / 12)
    label = str(i)
    x = np.sin(angle) * (clock_radius + 20)
    y = np.cos(angle) * (clock_radius + 20)
    mark = visual.TextStim(win, text=label, pos=(x, y), color='white', height=24)
    marks.append(mark)


# --- DADES PARTICIPANT ---

# Textos estàtics
intro = visual.TextStim(win, text="Abans de començar, introdueix les teves dades:", pos=(0, 300), color='white', height=30)
instructions = visual.TextStim(win, text="Prem ENTER per passar al següent camp", pos=(0, -300), color='grey', height=20)

# Camps i respostes
fields = ['Nom', 'Edat']
responses = ['', '']
current_field = 0

field_texts = [
    visual.TextStim(win, text='', pos=(0, 150), color='white', height=28),
    visual.TextStim(win, text='', pos=(0, 75), color='white', height=28)
]

# ===== FASE 1: NOM I EDAT =====
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
        # Dibuixar pantalla
        intro.draw()
        instructions.draw()
        for i, field in enumerate(fields):
            prefix = "> " if i == current_field else "  "
            field_texts[i].text = f"{prefix}{field}: {responses[i]}"
            field_texts[i].draw()
        win.flip()
        continue
    break  # sortim del bucle si tot està entrat

# ===== FASE 2: GÈNERE (amb tecles 1-4) =====
gender_options = ['Home', 'Dona', 'No binari', 'Prefereixo no dir-ho']
gender_prompt = visual.TextStim(win, text="Selecciona el teu gènere:\n\n"
                                           "[1] Home\n"
                                           "[2] Dona\n"
                                           "[3] No binari\n"
                                           "[4] Prefereixo no dir-ho",
                                pos=(0, 0), color='white', height=28, alignText='center')
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

instructions = visual.TextStim(win, text=instructions_text,
                                color='white', height=24,
                                wrapWidth=700, alignText='left')

instructions.draw()
win.flip()

# Espera fins que es premi qualsevol tecla
event.waitKeys()



# --- LOOP PRINCIPAL ---
experiment_clock.reset()
running = True

while running:
    # --- EEG: Iniciem registre després del missatge de relaxació ---
    datos_eeg = []
    tiempo_inicio = time.time()
    t = experiment_clock.getTime()
    angle_deg = (t % rotation_duration) / rotation_duration * 360
    angle_rad = np.deg2rad(angle_deg)

    x = np.sin(angle_rad) * clock_radius
    y = np.cos(angle_rad) * clock_radius
    hand.end = (x, y)

    # Dibuixar rellotge en moviment
    circle.draw()
    hand.draw()
    for mark in marks:
        mark.draw()
    win.flip()

    keys = event.getKeys()
    if 'escape' in keys:
        running = False
        break

    if 'space' in keys:
        real_time = t
        real_angle = angle_deg % 360

        # --- INSTRUCCIÓ ---
        instruccio = visual.TextStim(
            win,
            text="Fes clic al punt del cercle on creus que estava l’agulla\nquan vas decidir prémer.",
            color='white',
            height=24,
            wrapWidth=700,
            pos=(0, -300)
        )
        circle.draw()
        for mark in marks:
            mark.draw()
        instruccio.draw()
        win.flip()
        core.wait(2.0)

        # --- ESPERA CLIC ---
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

        # --- CÀLCUL ANGLE I TEMPS ESTIMAT ---
        angle_click = (np.degrees(np.arctan2(x_click, y_click)) + 360) % 360
        angle_diff = ((angle_click - real_angle + 180) % 360) - 180
        time_diff = (angle_diff / 360) * rotation_duration #negativo significa que la respuesta es previa a la real
        estimated_real_time = real_time + time_diff
        #
        # --- VISUALITZAR AGULLA DE RESPOSTA ---
        feedback_hand = visual.Line(
            win,
            start=(0, 0),
            end=(np.sin(np.deg2rad(angle_click)) * clock_radius,
                 np.cos(np.deg2rad(angle_click)) * clock_radius),
            lineColor='green',
            lineWidth=4
        )

        # Mostrar el clic del participant
        circle.draw()
        feedback_hand.draw()
        for mark in marks:
            mark.draw()
        win.flip()
        core.wait(1.5)

        # --- GUARDAR DADES ---
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
        # --- Pausa entre trials per evitar contaminació EEG ---
        pause_message = visual.TextStim(win,
            text="Estigues relaxat/da i no et moguis durant uns segons...",
            color='white', height=30, wrapWidth=1000, pos=(0, 0)
            )
        # Mostra el missatge
        pause_message.draw()
        win.flip()
        # Espera entre 3 i 6 segons de forma aleatòria
        pause_duration = np.random.uniform(3, 6)
        core.wait(pause_duration)






# --- DESAR A CSV ---
df = pd.DataFrame(results)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
safe_name = participant_name.strip().replace(" ", "_") # Preparar el nom segur del participant (sense espais ni caràcters especials)
filename = f"{timestamp}_{safe_name}.csv" # Nom del fitxer
df.to_csv(filename, index=False) # Guardar l'arxiu


# --- MISSATGE FINAL ---
final_msg = visual.TextStim(win, text="Resultats desats.\nGràcies per participar.", color='white', height=25)
final_msg.draw()
win.flip()
core.wait(2)

win.close()
core.quit()
