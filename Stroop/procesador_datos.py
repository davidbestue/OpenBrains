# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:53:43 2017

@author: David Bestue | Open Brains
"""

import pandas as pd                                                                 
import numpy as np 
import matplotlib.pyplot as plt 
#import seaborn as sns 
import os
import glob
from ast import literal_eval
import tkinter as tk
from tkinter import filedialog

#abrir dialogue box para seleccionar path de la carpeta
root = tk.Tk()
root.withdraw()
path_folder_all = filedialog.askdirectory()

search_string=os.path.join(path_folder_all,'*.csv') 
files = glob.glob(search_string) #list of data files in the named location


## dataframe con todos los datos relevantes

summary=[]

for file in files:
    #
    df_all = pd.read_csv(file) 
    df = df_all[['texto', 'color', 'respuesta.rt', 'respuesta_rect.rt', 'respuesta_mix.rt', 'participant']] 
    #
    ## conseguir columna única de rt
    df['respuesta.rt'] = df['respuesta.rt'].fillna(0) 
    df['respuesta_rect.rt'] = df['respuesta_rect.rt'].fillna(0) 
    df['respuesta_mix.rt'] = df['respuesta_mix.rt'].fillna(0) 
    #
    condition = []
    #
    for i in range(len(df)):
        if df['respuesta.rt'].iloc[i]!=0:
            df['respuesta.rt'].iloc[i] = literal_eval(df['respuesta.rt'].iloc[i])[-1] 
        #
        if df['respuesta_rect.rt'].iloc[i]!=0:
            df['respuesta_rect.rt'].iloc[i] = literal_eval(df['respuesta_rect.rt'].iloc[i])[-1] 
        #
        if df['respuesta_mix.rt'].iloc[i]!=0:
            df['respuesta_mix.rt'].iloc[i] = literal_eval(df['respuesta_mix.rt'].iloc[i])[-1] 
        #
    #
    df['rt'] = df['respuesta.rt'] + df['respuesta_rect.rt'] + df['respuesta_mix.rt']
    #
    ## quitar filas sin rt
    df = df[~(df['rt']==0)].reset_index() 
    #
    ## quitar columnas extra de rt
    df1 = df[['texto', 'color', 'rt', 'participant']]
    #
    #columna de condiciones (3 bloques)
    conditions=[]
    #
    for i in range(len(df1)):
        if isinstance(df1['texto'].iloc[i], str):
            if isinstance(df1['color'].iloc[i], str) == False:
                conditions.append('palabra_negra')
            elif isinstance(df1['color'].iloc[i], str) == True:
                conditions.append('palabra_color')
        else:
            conditions.append('rectangulo')
        #
    #
    df1['condition'] = conditions
    #
    #poner colores correctos
    df1['color'] = df1['color'].fillna('negro')   
    df1['color'] = df1['color'].replace(['[1, 0.1, -1]', '[0.004, -1, 0.004]', '[-1, -1, 1]', '[-1, 0.04, -1]'], ['naranja', 'lila', 'azul', 'verde'])
    #
    #poner texto (estímulo presentado) correct
    df1['texto'] = df1['texto'].fillna('rectangulo')   
    #
    ## append in summary
    summary.append(df1)
    #
#
##
data = pd.concat(summary).reset_index() 



### dataframe simplificado
simplificado =[]

for subj in data.participant.unique():
    mean_rt_pn = data.loc[(data['condition']=='palabra_negra') & (data['participant']==subj)].rt.mean() 
    mean_rt_rec = data.loc[(data['condition']=='rectangulo') & (data['participant']==subj)].rt.mean()
    mean_rt_pcol = data.loc[(data['condition']=='palabra_color') & (data['participant']==subj)].rt.mean()  
    simplificado.append([mean_rt_pn, mean_rt_rec, mean_rt_pcol, subj ])


df_simple = pd.DataFrame(simplificado)
df_simple.columns=['palabra negra (C1)', 'rectangulo (C2)', 'palabra color (E)', 'sujeto']



##guardar ambos archivos en el mismo excel
writer = pd.ExcelWriter(os.path.join(path_folder_all,'resumen.xlsx'))
data.to_excel(writer, sheet_name='datos completos') 
df_simple.to_excel(writer, sheet_name='simplificado')
writer.save()   #save reconstructions (heatmaps)

