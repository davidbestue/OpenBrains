# -*- coding: utf-8 -*-
"""
LIBET - EEG

@author: David Bestue | Open Brains
"""

from psychopy import visual, core, event

# Crear finestra
win = visual.Window(size=[800, 600], color='black', units='pix')

# Crear rellotge intern i visual
reloj = core.Clock()
text = visual.TextStim(win, text='00:00.000', pos=(0, 0), color='white', height=50)

# Estat inicial: rellotge aturat
running = False
temps_acumulat = 0.0

while True:
    # Gestiona les tecles
    keys = event.getKeys()
    if 'escape' in keys:
        break
    if 'space' in keys:
        if running:
            temps_acumulat += reloj.getTime()
            running = False
        else:
            reloj.reset()
            running = True

    # Actualitza temps
    if running:
        temps_actual = temps_acumulat + reloj.getTime()
    else:
        temps_actual = temps_acumulat

    # Formateja el text (minuts:segons.mil·lisegons)
    minuts = int(temps_actual // 60)
    segons = int(temps_actual % 60)
    milis = int((temps_actual % 1) * 1000)
    text.text = f'{minuts:02d}:{segons:02d}.{milis:03d}'

    # Dibuixa
    text.draw()
    win.flip()

# Tancar finestra
win.close()
core.quit()
