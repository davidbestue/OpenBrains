# -*- coding: utf-8 -*-
"""
TASCA CONTROL
@author: David Bestue | Open Brains
"""


import matplotlib.pyplot as plt

# Datos (en %)
labels = ["predicció dels mentiders", "realitat"]
labels = ["Què crec que saben els altres", "El que saben en realitat"]
labels = ["El que crec que sé dels altres", "El que sé en realitat"]
values = [27.2, 20]

# Colores: 1ª naranja, 2ª azul
colors = ["#F28E2B", "#4E79A7"]
colors = ["darkorange", "blue"]

fig, ax = plt.subplots(figsize=(7.5, 4.5))

# Barras
bars = ax.bar(labels, values, color=colors, width=0.6)


def add_sig(ax, x1, x2, y, text="*", h=0.5, lw=1.5):
    ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color="black", linewidth=lw)
    ax.text((x1 + x2) / 2, y + h + (0.02 * (ax.get_ylim()[1]-ax.get_ylim()[0])),
            text, ha="center", va="bottom", fontsize=14, color="black")


add_sig(ax, 0, 1, y=30, text="*", h=0.5)  # * representa p<0.05




# Línea de atzar (20%)
ax.axhline(20, linestyle="--", linewidth=1.5, color="k")
ax.text(
    1.02, 20, "atzar", va="center", ha="left",
    color="k", fontsize=11, transform=ax.get_yaxis_transform()
)

# Formato del eje Y en porcentaje
ax.set_ylim(15, 35)
ax.set_ylabel("Percentatge")
ax.set_yticks(range(5, 36, 5))
ax.set_yticklabels([f"{y}%" for y in range(5, 36, 5)])

# Valores encima de cada barra
for b, v in zip(bars, values):
    ax.text(
        b.get_x() + b.get_width()/2, v + 1,
        f"{v:.1f}%", ha="center", va="bottom", fontsize=11
    )

# Estética
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(axis='x', labelrotation=0)

plt.title("Il·lusió de transparència", fontsize=14, fontweight='bold')


plt.ylim(15,35)
plt.tight_layout()
plt.savefig("il_transparencia.png", dpi=300, transparent=True)


plt.show(block=False)
