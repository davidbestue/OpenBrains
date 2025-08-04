# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:53:43 2017

@author: David Bestue | Open Brains
"""


import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
	print(port.device, port.description)
	if 'USB Serial Device' in port.description:
		puerto = port.device
		print(f"Puerto encontrado: {port.device}")





