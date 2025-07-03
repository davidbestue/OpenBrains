# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:53:43 2017

@author: David Bestue | Open Brains
"""

import serial
import time

# 1) Ajusta el puerto y baudios
ser = serial.Serial(port='COM5', baudrate=9600, timeout=1)

# 2) Arduino se reinicia al abrir el puerto USB; espera un par de segundos
time.sleep(2)

# 3) Lee línea a línea
try:
    while True:
        raw = ser.readline()           # bytes
        if raw:                        # línea no vacía
            line = raw.decode('utf-8', errors='replace').strip()
            print(line)                # ej. “523”
except KeyboardInterrupt:
    pass
finally:
    ser.close()




#>>> import serial.tools.list_ports
#>>> ports = serial.tools.list_ports.comports()
#>>> ports
#[<serial.tools.list_ports_common.ListPortInfo object at 0x00000285CE29AEF0>, <serial.tools.list_ports_common.ListPortInfo object at 0x00000285CE29A8C0>, <serial.tools.list_ports_common.ListPortInfo object at 0x00000285CE29B8B0>]
#>>> for port in ports:
#...     print(port.device, port.description)
#...
#COM3 Standard Serial over Bluetooth link (COM3)
#COM4 Standard Serial over Bluetooth link (COM4)
#COM5 USB Serial Device (COM5)