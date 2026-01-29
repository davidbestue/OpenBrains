# -*- coding: utf-8 -*-
"""
TASCA CONTROL
@author: David Bestue | Open Brains
"""


# Construimos tabla con los datos EXACTOS de Rosenthal & Jacobson (1968), Tabla 1 (Total IQ)
# y añadimos: (a) columna de colapso (1–2 vs 3–6) y (b) significancia aprox. con MSW=164.24
# Fuente: Rosenthal & Jacobson (1968) The Urban Review, p. 17 (Tabla 1).

import math
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean

rows = [
    {"grado": 1, "N_control": 48, "gain_control": 12.0, "N_exp": 7,  "gain_exp": 27.4},
    {"grado": 2, "N_control": 47, "gain_control": 7.0,  "N_exp": 12, "gain_exp": 16.5},
    {"grado": 3, "N_control": 40, "gain_control": 5.0,  "N_exp": 14, "gain_exp": 5.0},
    {"grado": 4, "N_control": 49, "gain_control": 2.2,  "N_exp": 12, "gain_exp": 5.6},
    {"grado": 5, "N_control": 26, "gain_control": 17.5, "N_exp": 9,  "gain_exp": 17.4},
    {"grado": 6, "N_control": 45, "gain_control": 10.7, "N_exp": 11, "gain_exp": 10.0},
]
df = pd.DataFrame(rows)
df["grupo_grados"] = df["grado"].apply(lambda g: "1–2" if g in (1,2) else "3–6")

MSW = 164.24

def se_diff(msw, n_c, n_e):
    return math.sqrt(msw * (1.0/n_c + 1.0/n_e))

def z_to_p_two_sided(z):
    Phi = 0.5*(1.0 + math.erf(abs(z)/math.sqrt(2.0)))
    return 2.0*(1.0 - Phi)

def compute_stats_row(nc, gc, ne, ge):
    diff = ge - gc
    se = se_diff(MSW, nc, ne)
    z = diff / se if se > 0 else float('nan')
    p = z_to_p_two_sided(z)
    return diff, z, p

stats = df.apply(lambda r: compute_stats_row(r["N_control"], r["gain_control"], r["N_exp"], r["gain_exp"]), axis=1)
df["diff_exp_minus_ctrl"] = [s[0] for s in stats]
df["z_approx"] = [s[1] for s in stats]
df["p_two_tailed_approx"] = [s[2] for s in stats]

def weighted_mean_gain(sub, col_gain, col_n):
    return (sub[col_gain] * sub[col_n]).sum() / sub[col_n].sum()

def summary_block(sub):
    Nc = sub["N_control"].sum()
    Ne = sub["N_exp"].sum()
    gc_bar = weighted_mean_gain(sub, "gain_control", "N_control")
    ge_bar = weighted_mean_gain(sub, "gain_exp", "N_exp")
    diff, z, p = compute_stats_row(Nc, gc_bar, Ne, ge_bar)
    return {
        "N_control": Nc, "gain_control_media_ponderada": gc_bar,
        "N_exp": Ne, "gain_exp_media_ponderada": ge_bar,
        "diff_exp_minus_ctrl": diff, "z_approx": z, "p_two_tailed_approx": p
    }

total_summary = summary_block(df)
low_summary   = summary_block(df[df["grupo_grados"]=="1–2"])
high_summary  = summary_block(df[df["grupo_grados"]=="3–6"])

# Gráfico por grados (líneas)
plt.figure(figsize=(8,5))
plt.plot(df["grado"], df["gain_control"], marker='o', linestyle='--', label='Control')
plt.plot(df["grado"], df["gain_exp"], marker='o', label='Experimental (“spurters”)')
plt.title("Ganancia media de CI tras un año (Total IQ) – Rosenthal & Jacobson, 1968")
plt.xlabel("Grado escolar")
plt.ylabel("Ganancia media de CI (puntos)")
plt.xticks(df["grado"])
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show(block=False)

print("=== Estadística (aprox. normal bilateral) basada en MSW=164.24 ===")
for name, S in [("Total (1–6)", total_summary), ("Colapso 1–2", low_summary), ("Colapso 3–6", high_summary)]:
    print(f"{name}: N_control={S['N_control']}, media_ctrl={S['gain_control_media_ponderada']:.2f} | "
          f"N_exp={S['N_exp']}, media_exp={S['gain_exp_media_ponderada']:.2f} | "
          f"Dif={S['diff_exp_minus_ctrl']:.2f} | z≈{S['z_approx']:.2f} | p≈{S['p_two_tailed_approx']:.3f}")






# Gráfico de barras colapsando grados 1–6 (Total IQ)
# Significancia con MSW=164.24 (Tabla 1). Barras de error = EE ≈ sqrt(MSW/N).

import math
import matplotlib.pyplot as plt
import pandas as pd

rows = [
    {"grado": 1, "N_control": 48, "gain_control": 12.0, "N_exp": 7,  "gain_exp": 27.4},
    {"grado": 2, "N_control": 47, "gain_control": 7.0,  "N_exp": 12, "gain_exp": 16.5},
    {"grado": 3, "N_control": 40, "gain_control": 5.0,  "N_exp": 14, "gain_exp": 5.0},
    {"grado": 4, "N_control": 49, "gain_control": 2.2,  "N_exp": 12, "gain_exp": 5.6},
    {"grado": 5, "N_control": 26, "gain_control": 17.5, "N_exp": 9,  "gain_exp": 17.4},
    {"grado": 6, "N_control": 45, "gain_control": 10.7, "N_exp": 11, "gain_exp": 10.0},
]
df = pd.DataFrame(rows)

MSW = 164.24

Nc = df["N_control"].sum()
Ne = df["N_exp"].sum()
mean_ctrl = (df["N_control"] * df["gain_control"]).sum() / Nc
mean_exp  = (df["N_exp"] * df["gain_exp"]).sum() / Ne

se_ctrl = math.sqrt(MSW / Nc)
se_exp  = math.sqrt(MSW / Ne)

se_diff = math.sqrt(MSW * (1.0/Nc + 1.0/Ne))
z = (mean_exp - mean_ctrl) / se_diff
Phi = 0.5*(1.0 + math.erf(abs(z)/math.sqrt(2.0)))
p_two_sided = 2.0*(1.0 - Phi)

labels = ["Control", "Experimental"]
means = [mean_ctrl, mean_exp]
errors = [se_ctrl, se_exp]

plt.figure(figsize=(6,5))
plt.bar(labels, means, yerr=errors, capsize=6)
plt.title("Ganancia media de CI tras un año (Total IQ)\nPygmalion in the Classroom – Colapso grados 1–6")
plt.ylabel("Ganancia media de CI (puntos)")
plt.text(0.5, max(means)+max(errors)*1.2,
         f"Dif = {mean_exp - mean_ctrl:.2f} puntos\nz ≈ {z:.2f}  |  p ≈ {p_two_sided:.3f}",
         ha='center')
plt.tight_layout()
plt.show(block=False)

print("=== Resumen colapsado (grados 1–6) ===")
print(f"N_control = {Nc}, media_control = {mean_ctrl:.2f}, EE_control ≈ {se_ctrl:.2f}")
print(f"N_experimental = {Ne}, media_experimental = {mean_exp:.2f}, EE_experimental ≈ {se_exp:.2f}")
print(f"Diferencia (exp - ctrl) = {mean_exp - mean_ctrl:.2f} puntos")
print(f"z ≈ {z:.2f}  |  p (bilateral, normal aprox.) ≈ {p_two_sided:.3f}")



#####

import math
import matplotlib.pyplot as plt
import pandas as pd

# Dades originals de la Taula 1 (Total IQ)
rows = [
    {"grado": 1, "N_control": 48, "gain_control": 12.0, "N_exp": 7,  "gain_exp": 27.4},
    {"grado": 2, "N_control": 47, "gain_control": 7.0,  "N_exp": 12, "gain_exp": 16.5},
    {"grado": 3, "N_control": 40, "gain_control": 5.0,  "N_exp": 14, "gain_exp": 5.0},
    {"grado": 4, "N_control": 49, "gain_control": 2.2,  "N_exp": 12, "gain_exp": 5.6},
    {"grado": 5, "N_control": 26, "gain_control": 17.5, "N_exp": 9,  "gain_exp": 17.4},
    {"grado": 6, "N_control": 45, "gain_control": 10.7, "N_exp": 11, "gain_exp": 10.0},
]
df = pd.DataFrame(rows)

# MSW reportat a la Taula 1
MSW = 164.24

# Mitjanes ponderades
Nc = df["N_control"].sum()
Ne = df["N_exp"].sum()
mean_ctrl = (df["N_control"] * df["gain_control"]).sum() / Nc
mean_exp  = (df["N_exp"] * df["gain_exp"]).sum() / Ne

# Error estàndard i estadística z
se_ctrl = math.sqrt(MSW / Nc)
se_exp  = math.sqrt(MSW / Ne)
se_diff = math.sqrt(MSW * (1.0/Nc + 1.0/Ne))
z = (mean_exp - mean_ctrl) / se_diff
Phi = 0.5*(1.0 + math.erf(abs(z)/math.sqrt(2.0)))
p_two_sided = 2.0*(1.0 - Phi)

# Gràfic millorat
labels = ["Alumnes bons", "Control"]
means = [mean_exp, mean_ctrl]
errors = [se_exp, se_ctrl]
colors = ["#f28e2b", "#4e79a7"]  # taronja i blau suau

plt.figure(figsize=(6,5))
bars = plt.bar(labels, means, yerr=errors, capsize=6, color=colors, edgecolor="none")

# Títol i eixos
plt.title("Efecte Pygmalió a l'aula", fontsize=14, fontweight='bold')
plt.ylabel("Guany promig de CI per curs de 1r a 6è", fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=10)

# Elimina els eixos superior i dret
for spine in ["top", "right"]:
    plt.gca().spines[spine].set_visible(False)

# Línia base i anotació estadística
plt.axhline(0, color="gray", linewidth=0.8)
plt.text(0.5, max(means)+max(errors)*1.25,
         f"Dif = {mean_exp - mean_ctrl:.2f} punts\nz ≈ {z:.2f}  |  p ≈ {p_two_sided:.3f}",
         ha='center', fontsize=11)

plt.ylim(4,16)
plt.tight_layout()
plt.savefig("efecte_pygmalio.png", dpi=300, bbox_inches="tight", transparent=True)
plt.show(block=False)
