import numpy as np
import matplotlib.pyplot as plt
import random

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['font.family'] = 'serif'

def random_walk_2D(n_values):
    rw_results = []
    for N in n_values:
        if N == 0:
            rw_results.append(0)
            continue
    
        K = int(np.sqrt(N))
        if K < 1: 
            K = 1

        dx_p = np.random.uniform(-1, 1, (K, N))
        dy_p = np.random.uniform(-1, 1, (K, N))
        L = np.sqrt(dx_p**2 + dy_p**2)
        dx = dx_p/L
        dy = dy_p/L

        x_final = np.sum(dx, axis=1)
        y_final = np.sum(dy, axis=1)

        r2_mean = np.mean(x_final**2 + y_final**2)
        rw_results.append(np.sqrt(r2_mean))
        
        #Kiểm tra tính độc lập của các bước
        if N == n_values[-1]:
            term_xx = (np.mean(x_final**2) - np.mean(np.sum(dx**2, axis=1))) / r2_mean
            term_xy = np.mean(x_final * y_final) / r2_mean
            print(f"Same-axis correlation <Δxi.Δxj>/R2: {term_xx:.6f}")
            print(f"Cross-axis correlation <Δxi.Δyj>/R2: {term_xy:.6f}")
    return rw_results

N_max = 90000 
N_vals = np.linspace(0, N_max, 100).astype(int) 
sqrt_N_vals = np.sqrt(N_vals)
rw_results = random_walk_2D(N_vals)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

#(a)
for _ in range(7):
    x_w = [0.0]
    y_w = [0.0]
    for _ in range(1000):
        dx_p, dy_p = random.uniform(-1, 1), random.uniform(-1, 1)
        dist = np.sqrt(dx_p**2 + dy_p**2)
        x_w.append(x_w[-1] + dx_p/dist)
        y_w.append(y_w[-1] + dy_p/dist)
    ax1.plot(x_w, y_w, lw=0.8)

ax1.set_title("7 Random Walks", fontsize=13)
ax1.set_xlim(-40, 40)
ax1.set_ylim(-40, 40)
ax1.set_aspect('equal')
ax1.axhline(0, color='black', lw=0.8)
ax1.axvline(0, color='black', lw=0.8)

#(b)
ax2.plot(sqrt_N_vals, rw_results, 'r-', lw=1.2, label='Simulation')
ax2.plot([0, 300], [0, 300], color='blue', lw=4, label='Theory', alpha=0.3)

ax2.set_title("Distance vs. Steps", fontsize=13)
ax2.set_xlim(0, 300)
ax2.set_ylim(0, 300)
ax2.set_xlabel(r"$\sqrt{N}$")
ax2.set_ylabel(r"$R$")
ax2.set_aspect('equal')
ax2.legend()

plt.tight_layout()
plt.show()
