# -*- coding: utf-8 -*-
"""
TASCA CONTROL
@author: David Bestue | Open Brains
"""
import matplotlib.pyplot as plt
import numpy as np
import math

# ---------- Utilidad para marcar significancia ----------
def add_sig(ax, x1, x2, y, text="*", h=0.5, lw=1.5):
    ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color="black", linewidth=lw)
    ax.text((x1 + x2) / 2, y + h + (0.02 * (ax.get_ylim()[1]-ax.get_ylim()[0])),
            text, ha="center", va="bottom", fontsize=14, color="black")

# ---------- Gráfico 1: Percentatge ----------
labels = ["Poques opcions", "Moltes opcions"]
values_pct = [74, 60]  # en %

colors = ["darkorange", "blue"]

fig1, ax1 = plt.subplots(figsize=(6, 5))

# Centramos las posiciones de las barras y las acercamos
x = np.array([-0.25, 0.25])  # más juntas y centradas
bars1 = ax1.bar(x, values_pct, color=colors, width=0.4)

# Ejes y formato
ax1.set_ylabel("Percentatge")
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.set_ylim(0, 100)
ax1.set_yticks(np.arange(0, 101, 10))
ax1.set_yticklabels([f"{t}%" for t in np.arange(0, 101, 10)])
ax1.set_title('Entrega de la tasca')

# Valores encima
for b, v in zip(bars1, values_pct):
    ax1.text(b.get_x() + b.get_width()/2, v + 2, f"{v:.0f}%", ha="center", va="bottom")

# Significancia p<0.05 con asterisco
y_max = max(values_pct)
add_sig(ax1, x[0], x[1], y_max + 8, text="*", h=2)  # * representa p<0.05

# Estética
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# Ajustamos márgenes para centrado
ax1.set_xlim(-0.7, 0.7)

fig1.tight_layout()
fig1.savefig("grafic_percentatge.png", dpi=300, transparent=True)
plt.show(block=False)













# ---------- Utilidad para marcar significancia ----------
def add_sig(ax, x1, x2, y, text="*", h=0.5, lw=1.5):
    ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color="black", linewidth=lw)
    ax.text((x1 + x2) / 2, y + h + (0.02 * (ax.get_ylim()[1]-ax.get_ylim()[0])),
            text, ha="center", va="bottom", fontsize=14, color="black")

# ---------- Datos ----------
labels = ["Poques opcions", "Moltes opcions"]
colors = ["darkorange", "blue"]

means = [8.09, 7.69]
sd = [1.05, 0.82]
Ns = [70, 123]
sem = [sd[i] / math.sqrt(Ns[i]) for i in range(2)]

# ---------- Gráfico ----------
fig2, ax2 = plt.subplots(figsize=(6, 5))

# Posiciones centradas y más juntas
x = np.array([-0.25, 0.25])
bars2 = ax2.bar(x, means, yerr=sem, capsize=6, color=colors, width=0.4)

ax2.set_ylabel("Nota (1–10)")
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_ylim(0, 10)
ax2.set_xlim(-0.7, 0.7)
ax2.set_title('Qualitat de la tasca')

# Valores encima
for b, m, s in zip(bars2, means, sem):
    ax2.text(b.get_x() + b.get_width()/2, m + s + 0.15, f"{m:.2f}", ha="center", va="bottom")

# Significancia p<.02
y2 = 9
add_sig(ax2, x[0], x[1], y2, text="*", h=0.25)

# Estética
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

fig2.tight_layout()

# Guardar con fondo transparente
fig2.savefig("grafic_nota_sd.png", dpi=300, transparent=True)
plt.show(block=False)
