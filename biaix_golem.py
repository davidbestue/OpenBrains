# -*- coding: utf-8 -*-
"""
TASCA CONTROL
@author: David Bestue | Open Brains
"""

import math
import matplotlib.pyplot as plt

# -----------------------------
# Datos del artículo
# -----------------------------
# Medias y desviaciones estándar (SD)
pre_pos_mean, pre_pos_sd = 10.78, 2.89   # alumnes bons
pre_neg_mean, pre_neg_sd = 10.83, 3.40   # alumnes dolents

post_pos_mean, post_pos_sd = 10.42, 2.70
post_neg_mean, post_neg_sd =  8.94, 2.97

# Tamaño muestral aproximado
n = 275 / 3  # ≈ 92

# -----------------------------
# Cálculo del SEM
# -----------------------------
pre_pos_sem  = pre_pos_sd  / math.sqrt(n)
post_pos_sem = post_pos_sd / math.sqrt(n)
pre_neg_sem  = pre_neg_sd  / math.sqrt(n)
post_neg_sem = post_neg_sd / math.sqrt(n)

# -----------------------------
# Datos para graficar
# -----------------------------
x_labels = ['prova PRE', 'prova POST']
x = [0, 1]

pos_means = [pre_pos_mean,  post_pos_mean]
pos_sems  = [pre_pos_sem,   post_pos_sem]

neg_means = [pre_neg_mean,  post_neg_mean]
neg_sems  = [pre_neg_sem,   post_neg_sem]

# -----------------------------
# Gráfico
# -----------------------------
plt.figure(figsize=(6.5, 5))

# Alumnes bons (naranja)
plt.errorbar(
    x, pos_means, yerr=pos_sems,
    fmt='-o', capsize=5, linewidth=3,
    label='alumnes bons', color='orange'
)

# Alumnes dolents (azul)
plt.errorbar(
    x, neg_means, yerr=neg_sems,
    fmt='-o', capsize=5, linewidth=3,
    label='alumnes dolents', color='royalblue'
)

# -----------------------------
# Asterisco de significancia
# -----------------------------
x_post = 1
y_post_pos = post_pos_mean + post_pos_sem
y_post_neg = post_neg_mean + post_neg_sem
y_bracket = max(y_post_pos, y_post_neg) + 0.25

plt.plot([x_post-0.08, x_post-0.08, x_post+0.08, x_post+0.08],
         [y_bracket-0.05, y_bracket, y_bracket, y_bracket-0.05],
         color='black', lw=1)
plt.text(x_post, y_bracket + 0.08, '*', ha='center', va='bottom', fontsize=18)

# -----------------------------
# Estética general
# -----------------------------
plt.title("Efecte Gòlem", fontsize=18, fontweight='bold')
plt.xticks(x, x_labels, fontsize=14)
plt.ylabel("Puntuació mitjana (test de lògica)", fontsize=14)
plt.legend(frameon=False, fontsize=14, loc=3)
plt.grid(alpha=0.2, axis='y')
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Márgenes laterales y rango Y
plt.xlim(-0.25, 1.25)
plt.ylim(8.5, 11.3)

plt.tight_layout()

# --- (Opcional) Guardar con fondo transparente ---
plt.savefig("Efete_Golem.png", dpi=300, transparent=True)


plt.show(block=False)



