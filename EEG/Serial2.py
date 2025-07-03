# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:53:43 2017

@author: David Bestue | Open Brains
"""

import serial
import time
import datetime

# CONFIGURACIÓN
PORT = 'COM6'
BAUDRATE = 230400
DURATION = 10  # segundos
FILENAME = datetime.datetime.now().strftime("datos.dat")

# INICIAR SERIAL
ser = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=1)
time.sleep(2)  # Esperar a que Arduino arranque

# ABRIR ARCHIVO
with open(FILENAME, 'w') as f:
    print(f"Grabando datos por {DURATION} segundos...")
    start_time = time.time()

    while time.time() - start_time < DURATION:
        raw = ser.readline()
        if raw:
            line = raw.decode('utf-8', errors='replace').strip()
            timestamp = time.time()
            f.write(f"{timestamp},{line}\n")
            print(line)

# CERRAR SERIAL
ser.close()
print(f"Grabación finalizada. Datos guardados en: {FILENAME}")




import numpy as np
import matplotlib.pyplot as plt
filename = 'datos.dat'
data = np.fromfile(filename, dtype=np.int32)
len(data)





#import serial.tools.list_ports
#ports = serial.tools.list_ports.comports()
#ports
#for port in ports:
#  print(port.device, port.description)
#...
#COM3 Standard Serial over Bluetooth link (COM3)
#COM4 Standard Serial over Bluetooth link (COM4)
#COM5 USB Serial Device (COM5)