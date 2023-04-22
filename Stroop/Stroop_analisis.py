
# coding: utf-8

# In[41]:


## Importar librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
#from statsmodels.formula.api import ols
#import statsmodels.api as sm
#from statsmodels.stats.multicomp import pairwise_tukeyhsd
#import statsmodels.formula.api as smf
import tkinter as tk
from tkinter import filedialog


# In[42]:


#abrir dialogue box para seleccionar path de la carpeta
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

xl = pd.ExcelFile(file_path)
df = pd.read_excel(xl, 'datos completos')


# # Plots

# ### barplot

# In[43]:


# sns.barplot(x='condition', y='rt', data=df, palette=['darkorange', 'darkblue', 'lightcoral'], estimator=np.mean)

# plt.gca().spines['right'].set_visible(False)  # aesthetics                                                                              # remove right spines
# plt.gca().spines['top'].set_visible(False)                                                                                  # remove top spines
# plt.gca().get_xaxis().tick_bottom()                                                                                         
# plt.gca().get_yaxis().tick_left()
# plt.gca().tick_params(direction='in') #direction
# plt.xticks([0,1,2], ['negras', 'rectángulo', 'color'])
# plt.xlabel('')
# plt.ylabel('reaction time (s)')
# #plt.ylim(0, 1.5);


# ### boxplot + trials

# In[44]:


# sns.boxplot(x = "condition",  y = "rt",  data = df, 
#             palette=['darkorange', 'darkblue', 'lightcoral'])

# sns.stripplot(x = "condition",  y = "rt",  data = df,
#              palette=['darkorange', 'darkblue', 'lightcoral'])


# plt.gca().spines['right'].set_visible(False)  # aesthetics                                                                              # remove right spines
# plt.gca().spines['top'].set_visible(False)                                                                                  # remove top spines
# plt.gca().get_xaxis().tick_bottom()                                                                                         
# plt.gca().get_yaxis().tick_left()
# plt.gca().tick_params(direction='in') #direction
# plt.xticks([0,1,2], ['negras', 'rectángulo', 'color'])
# plt.xlabel('')
# plt.ylabel('reaction time (s)')
# plt.ylim(0, 2.5);


# ### confidence interval + subjects 

# In[45]:


#import scikits.bootstrap as bootstraps
from matplotlib.patches import Rectangle


def bootstrap_ci(data):
    # Calculamos la media de los datos
    data_mean = np.mean(data)

    # Definimos la cantidad de muestras bootstrap que queremos generar
    n_bootstraps = 1000

    # Generamos muestras bootstrap con reemplazo
    bootstrap_samples = np.random.choice(data, size=(n_bootstraps, len(data)), replace=True)

    # Calculamos la media de cada muestra bootstrap
    bootstrap_means = np.mean(bootstrap_samples, axis=1)

    # Ordenamos las medias bootstrap de menor a mayor
    sorted_means = np.sort(bootstrap_means)

    # Calculamos los percentiles 2.5 y 97.5 de las medias bootstrap
    ci_lower = sorted_means[int(0.025 * n_bootstraps)]
    ci_upper = sorted_means[int(0.975 * n_bootstraps)]

    return ci_lower, ci_upper


##


# In[46]:


m_pn=df.loc[df['condition']=='palabra_negra', 'rt'].mean()
ci_pn= bootstrap_ci(df.loc[df['condition']=='palabra_negra', 'rt'].values)

m_r=df.loc[df['condition']=='rectangulo', 'rt'].mean()
ci_r= bootstrap_ci(df.loc[df['condition']=='rectangulo', 'rt'].values)

m_pc=df.loc[df['condition']=='palabra_color', 'rt'].mean()
ci_pc= bootstrap_ci(df.loc[df['condition']=='palabra_color', 'rt'].values)

# In[47]:


###
plt.figure()

idxs_x = [0,1,2]
palette=['darkorange', 'darkblue', 'lightcoral']
cis = [ci_pn, ci_r, ci_pc]
means = [m_pn, m_r, m_pc]

for idx, cond in enumerate(['palabra_negra', 'rectangulo', 'palabra_color']):
    
    ##plot_rectange
    plt.gca().add_patch(Rectangle((idx, cis[idx][0]), 0.6, cis[idx][1]-cis[idx][0], 
                                  alpha=0.4, fill=True, facecolor=palette[idx],
                                  linewidth=1,  edgecolor=palette[idx]))  
    ##plot_mean
    plt.plot([idx, idx+0.6], [means[idx], means[idx]], color=palette[idx], linewidth=4) 
    
    ##
    subj_values = df.loc[df['condition']==cond].groupby('participant', as_index=False)['rt'].mean().rt.values
    for i in range(len(subj_values)):
        jitter=np.random.uniform(-0.1, 0.1)
        plt.plot(idx+0.3+jitter, subj_values[i], color=palette[idx], marker='o', markersize=6 )
    


plt.gca().spines['right'].set_visible(False)  # aesthetics                                                                              # remove right spines
plt.gca().spines['top'].set_visible(False)                                                                                  # remove top spines
plt.gca().get_xaxis().tick_bottom()                                                                                         
plt.gca().get_yaxis().tick_left()
plt.gca().tick_params(direction='in') #direction
plt.xticks([0+0.3,1+0.3,2+0.3], ['c1: negres', 'c2: rectangles', 'color'], fontsize=13)
plt.xlabel('')
plt.ylabel('temps de reacció (s)', fontsize=13)
plt.yticks(fontsize=10)
plt.title('efecte stroop', fontsize=16)
#plt.ylim(0.5, 1.5);
plt.show(block=False)




# ### historgram trials

# In[48]:


plt.figure()
sns.distplot(df.loc[df['condition']=='palabra_negra', 'rt'],  color='darkorange', bins=np.linspace(0,3,60),
             fit=norm, kde=False, fit_kws={"color":'darkorange', 'linewidth':2}, label='c1: negres')

sns.distplot(df.loc[df['condition']=='rectangulo', 'rt'],  color='darkblue', bins=np.linspace(0,3,60),
             fit=norm, kde=False, fit_kws={"color":'darkblue', 'linewidth':2}, label='c2: rectangles' )

sns.distplot(df.loc[df['condition']=='palabra_color', 'rt'],  color='lightcoral', bins=np.linspace(0,3,60),
             fit=norm, kde=False, fit_kws={"color":'lightcoral', 'linewidth':2}, label='color' )

plt.gca().spines['right'].set_visible(False)  # aesthetics                                                                              # remove right spines
plt.gca().spines['top'].set_visible(False)                                                                                  # remove top spines
plt.gca().get_xaxis().tick_bottom()                                                                                         
plt.gca().get_yaxis().tick_left()
plt.gca().tick_params(direction='in') #direction
plt.legend(loc=1, frameon=False, prop={'size': 13})
plt.xlabel('temps de reacció (s)', fontsize=13)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10);
plt.title('distribució de temps de reacció', fontsize=16)
plt.show()



# # Stats

# #### Anova + multiple comparisons (simple)
# ##### The correct Anova should be paired


# df_stats = df.copy()
# df_stats['condition']= df_stats['condition'].replace(['palabra_negra', 'rectangulo', 'palabra_color'], ['control 1', 'control 2', 'test'])

# mod = ols(formula='rt ~ condition', data=df_stats).fit()
# aov_table = sm.stats.anova_lm(mod, typ=2)

# print( '                                 ')
# print( '                                 Anova Table')
# print( '==============================================================================')
# print( aov_table)
# print( '==============================================================================')
# print( '                                 ')
# print( '                                 ')
# print( '                                 ')



####### Multiple comparisons
#tukey = pairwise_tukeyhsd(endog=df_stats.rt.values, groups=df_stats['condition'].values,  alpha=0.05)
#print( tukey.summary()    )
#print( '                                 ')
#print( '                                ')


# #### regression (subjects random intercepts - complex)

#resultados = smf.mixedlm(formula='rt ~ condition', data=df_stats, groups=df_stats['participant']).fit()
#print(resultados.summary())

