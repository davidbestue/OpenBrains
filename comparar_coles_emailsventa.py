# -*- coding: utf-8 -*-
"""
Anàlisi de potencial evocat (EEG Libet)
@author: Open Brains
"""


import pandas as pd

# Cargar los dos archivos Excel
df1 = pd.read_excel("C:/Users/david/Downloads/Escoles treballat (de informe anual) (1).xlsx")
df2 = pd.read_excel("C:/Users/david/Downloads/Primaria_catalunya_2024.xlsx")

# Suponiendo que la columna que quieres comparar se llama "Nombre"
col1 = df1["Nombre"]
col2 = df2["Denominació_completa"]

# Crear una lista para almacenar coincidencias
coincidencias = []

# Buscar coincidencias y sus posiciones
for i, valor in enumerate(col1):
    # Buscar todas las posiciones en col2 donde aparece el valor
    posiciones = df2.index[df2["Denominació_completa"] == valor].tolist()
    if posiciones:
        coincidencias.append({
            "Valor": valor,
            "Posición en archivo1": i,
            "Posiciones en archivo2": posiciones
        })

# Convertir a DataFrame para mejor visualización
resultado = pd.DataFrame(coincidencias)

# Mostrar en pantalla
print(resultado)

