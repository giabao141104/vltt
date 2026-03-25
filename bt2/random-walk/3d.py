import numpy as np
import matplotlib.pyplot as plt
import random

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['font.family'] = 'serif'

def random_walk_3D(n_values):
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
        dz_p = np.random.uniform(-1, 1, (K, N))
        
        L = np.sqrt(dx_p**2 + dy_p**2 + dz_p**2)
        dx = dx_p/L
        dy = dy_p/L
        dz = dz_p/L

        x_final = np.sum(dx, axis=1)
        y_final = np.sum(dy, axis=1)
        z_final = np.sum(dz, axis=1)

        r2_mean = np.mean(x_final**2 + y_final**2 + z_final**2)
        rw_results.append(np.sqrt(r2_mean))
        
        if N == n_values[-1]:
            term_xx = (np.mean(x_final**2) - np.mean(np.sum(dx**2, axis=1))) / r2_mean
            term_xy = np.mean(x_final * y_final) / r2_mean
            term_xz = np.mean(x_final * z_final) / r2_mean
            term_yz = np.mean(y_final * z_final) / r2_mean
            
            print(f"Same-axis correlation: {term_xx:.6f}")
            print(f"Cross-axis correlation: {term_xy:.6f}")
            print(f"Cross-axis correlation: {term_xz:.6f}")
            print(f"Cross-axis correlation: {term_yz:.6f}")
            
    return rw_results

N_max = 90000 
N_vals = np.linspace(0, N_max, 100).astype(int) 
sqrt_N_vals = np.sqrt(N_vals)
rw_results = random_walk_3D(N_vals)

fig = plt.figure(figsize=(13, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

#(a)
for _ in range(7):
    x_w, y_w, z_w = [0.0], [0.0], [0.0]
    for _ in range(1000):
        dx_p, dy_p, dz_p = random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)
        dist = np.sqrt(dx_p**2 + dy_p**2 + dz_p**2)
        x_w.append(x_w[-1] + dx_p/dist)
        y_w.append(y_w[-1] + dy_p/dist)
        z_w.append(z_w[-1] + dz_p/dist)
    ax1.plot(x_w, y_w, z_w, lw=0.8)

ax1.set_title("7 Random Walks (3D)", fontsize=13)
ax1.set_xlim(-40, 40)
ax1.set_ylim(-40, 40)
ax1.set_zlim(-40, 40)

#(b)
ax2.plot(sqrt_N_vals, rw_results, 'r-', lw=1.2, label='Simulation')
ax2.plot([0, 300], [0, 300], color='blue', lw=4, label='Theory', alpha=0.3)

ax2.set_title("Distance vs. Steps", fontsize=13)
ax2.set_xlim(0, 300)
ax2.set_ylim(0, 300)
ax2.set_xlabel(r"$\sqrt{N}$")
ax2.set_ylabel(r"$R$")
ax2.legend()

plt.tight_layout()
plt.savefig("images/3d.png", dpi=300)

with open("data/3d-steps.dat", "w") as f:
    for _ in range(7):
        x, y, z = 0.0, 0.0, 0.0
        f.write(f"{x} {y} {z}\n")
        for _ in range(1000):
            dx_p, dy_p, dz_p = random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)
            dist = np.sqrt(dx_p**2 + dy_p**2 + dz_p**2)
            x += dx_p/dist; y += dy_p/dist; z += dz_p/dist
            f.write(f"{x:.4f} {y:.4f} {z:.4f}\n")
        f.write("\n\n")

data_b = np.column_stack((sqrt_N_vals, rw_results))
np.savetxt("data/3d-distance.dat", data_b, header="sqrtN R")
