# -*- coding: utf-8 -*-
"""
LIBET - EEG

@author: David Bestue | Open Brains
"""


from psychopy import visual, core, event
import numpy as np

# Crear la finestra
win = visual.Window(size=[800, 800], color='black', units='pix')

# Crear cercle del rellotge
cercle = visual.Circle(win, radius=250, edges=128, lineColor='white', fillColor=None)

# Crear agulles (línies)
agulla_secs = visual.Line(win, start=(0, 0), end=(0, 200), lineColor='red', lineWidth=3)
agulla_mins = visual.Line(win, start=(0, 0), end=(0, 150), lineColor='white', lineWidth=6)

# Text de pausa
text_pausa = visual.TextStim(win, text='PAUSA', pos=(0, -300), color='gray', height=40)

# Rellotge intern
clock = core.Clock()
running = False
temps_acumulat = 0.0

while True:
    keys = event.getKeys()
    if 'escape' in keys:
        break
    if 'space' in keys:
        if running:
            temps_acumulat += clock.getTime()
            running = False
        else:
            clock.reset()
            running = True

    # Calcul del temps
    if running:
        temps_actual = temps_acumulat + clock.getTime()
    else:
        temps_actual = temps_acumulat

    # Convertir a minuts i segons
    segons = temps_actual % 60
    minuts = (temps_actual // 60) % 60

    # Angles en radians (rotació negativa = sentit horari)
    angle_secs = 2 * np.pi * (segons / 60)
    angle_mins = 2 * np.pi * (minuts / 60)

    # Posició de les agulles
    agulla_secs.end = (np.sin(angle_secs) * 200, np.cos(angle_secs) * 200)
    agulla_mins.end = (np.sin(angle_mins) * 150, np.cos(angle_mins) * 150)

    # Dibuix
    cercle.draw()
    agulla_secs.draw()
    agulla_mins.draw()
    if not running:
        text_pausa.draw()
    win.flip()

# Tancar
win.close()
core.quit()
