# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del ejemplo: caída con arrastre
g = 9.81          # m/s^2
rho = 1.225       # kg/m^3
Cd = 0.5
A = 0.5           # m^2
m = 100           # kg

def F(v, t):
    return -g + (rho * Cd * A) / (2 * m) * v**2

# Implementación de método de Euler
def euler(F, x0, t0, tf, N):
    h = (tf - t0) / N
    t = np.zeros(N + 1)
    x = np.zeros(N + 1)
    t[0], x[0] = t0, x0
    for n in range(N):
        x[n + 1] = x[n] + F(x[n], t[n]) * h
        t[n + 1] = t[n] + h
    return t, x

# Solución y escogencia del paso
t_exact, v_exact = euler(F, 0, 0, 10, 10000)

# Comparar distintos N (pasos)
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
steps = [5, 10, 40]

for ax, N in zip(axes, steps):
    t_e, v_e = euler(F, 0, 0, 10, N)

    ax.plot(t_exact, v_exact, 'k-', linewidth=1.5, label='Referencia')

    for n in range(N):
        ax.plot([t_e[n], t_e[n + 1]], [v_e[n], v_e[n + 1]],
                'o-', color='#e74c3c', markersize=4, linewidth=1.2)

    ax.set_title(f'$N = {N}$ pasos ($h = {10/N:.2f}$ s)', fontsize=14)
    ax.set_xlabel('$t$ [s]', fontsize=13)
    ax.legend(fontsize=11)
    ax.tick_params(axis='both', labelsize=12)
    ax.grid(True, alpha=0.3)

axes[0].set_ylabel('$v$ [m/s]', fontsize=13)
fig.suptitle('Método de Euler para caída con arrastre aerodinámico', fontsize=16, y=1.02)
plt.tight_layout()
plt.savefig('euler_pasos.png', dpi=200, bbox_inches='tight')
plt.show()

