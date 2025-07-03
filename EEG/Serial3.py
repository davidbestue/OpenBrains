# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:53:43 2017

@author: David Bestue | Open Brains
"""


import serial
import time

# Configura el puerto serie
puerto = 'COM6'  # En Windows. En Linux/Mac sería '/dev/ttyUSB0' o similar
baudrate = 230400  # Cambia a 115200 si actualizas tu Arduino

try:
    # Abre conexión serial
    ser = serial.Serial(puerto, baudrate, timeout=1)
    print(f"Conectado a {puerto} a {baudrate} baudios")
    print("Presiona Ctrl+C para detener...")
   
    # Espera un momento para que se establezca la conexión
    time.sleep(2)
   
    # Lista para almacenar los datos
    datos = []
    tiempo_inicio = time.time()
    contador = 0
   
    print("Leyendo durante 10 segundos...")
   
    while time.time() - tiempo_inicio < 30:  # Lee durante 10 segundos
        try:
            # Lee una línea del puerto serie
            linea = ser.readline().decode('utf-8').strip()
           
            if linea:  # Si hay datos
                datos.append(linea)
                contador += 1
                print(f"{contador}: {linea}")  # Muestra con contador
               
        except UnicodeDecodeError:
            # Ignora caracteres extraños
            continue
   
    # Calcula estadísticas
    tiempo_total = time.time() - tiempo_inicio
    frecuencia = contador / tiempo_total
   
    print(f"\n--- RESUMEN ---")
    print(f"Tiempo total: {tiempo_total:.2f} segundos")
    print(f"Datos leídos: {contador}")
    print(f"Frecuencia: {frecuencia:.2f} Hz")
   
    # Guarda todos los datos al archivo
    with open('datos4.dat', 'w') as archivo:
        for dato in datos:
            archivo.write(dato + '\n')
   
    print(f"Datos guardados en 'datos4.dat'")
               
except serial.SerialException as e:
    print(f"Error de conexión serial: {e}")
    print("Verifica que el puerto esté correcto y no esté en uso")
   
except KeyboardInterrupt:
    print("\nDetenido por usuario antes de completar los 10 segundos")
   
except Exception as e:
    print(f"Error: {e}")
   
finally:
    try:
        ser.close()
        print("Conexión cerrada")
    except:
        pass








import numpy as np
import matplotlib.pyplot as plt
filename = 'datos4.dat'
data = np.loadtxt('datos4.dat', dtype=int)
len(data)
