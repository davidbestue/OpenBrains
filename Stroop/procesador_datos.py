# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:53:43 2017

@author: David Bestue | Open Brains
"""

import pandas as pd                                                                 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os
import glob
from ast import literal_eval


path_folder_all = 'C:\\Users\\David\\Documents\\GitHub\\OpenBrains\\Stroop\\data'

search_string=os.path.join(path_folder_all,'*.csv') 
files = glob.glob(search_string) #list of data files in the named location
files

file = files[2]
df_all = pd.read_csv(file) 
df = df_all[['texto', 'color', 'respuesta.rt', 'respuesta_rect.rt', 'respuesta_mix.rt', 'participant']] 

##
#df = df_[~df_.texto.isnull()].reset_index() 

## conseguir columna única de rt
df['respuesta.rt'] = df['respuesta.rt'].fillna(0) 
df['respuesta_rect.rt'] = df['respuesta_rect.rt'].fillna(0) 
df['respuesta_mix.rt'] = df['respuesta_mix.rt'].fillna(0) 

condition = []

for i in range(len(df)):
    if df['respuesta.rt'].iloc[i]!=0:
        df['respuesta.rt'].iloc[i] = literal_eval(df['respuesta.rt'].iloc[i])[-1] 
    #
    if df['respuesta_rect.rt'].iloc[i]!=0:
        df['respuesta_rect.rt'].iloc[i] = literal_eval(df['respuesta_rect.rt'].iloc[i])[-1] 
    #
    if df['respuesta_mix.rt'].iloc[i]!=0:
        df['respuesta_mix.rt'].iloc[i] = literal_eval(df['respuesta_mix.rt'].iloc[i])[-1] 



df['rt'] = df['respuesta.rt'] + df['respuesta_rect.rt'] + df['respuesta_mix.rt']

df = df[~(df['rt']==0)].reset_index() 


df1 = df[['texto', 'color', 'rt', 'participant']]



conditions=[]

for i in range(len(df1)):
    if isinstance(df1['texto'].iloc[i], str):
        if isinstance(df1['color'].iloc[i], str) == False:
            conditions.append('palabra_negra')
        elif isinstance(df1['color'].iloc[i], str) == True:
            conditions.append('palabra_color')
    else:
        conditions.append(['rectangulo'])




