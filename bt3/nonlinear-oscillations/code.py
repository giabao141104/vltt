import numpy as np

def rk4(f, a, b, N, y0):
    h = (b - a)/N
    t = a
    y = [np.array(y0)]

    for i in range(1, N+1):
        k1 = h*f(t,       y[-1])
        k2 = h*f(t + h/2, y[-1] + k1/2)
        k3 = h*f(t + h/2, y[-1] + k2/2)
        k4 = h*f(t + h,   y[-1] + k3)
        yi = y[-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        y.append(yi)
        t = t + h

    return np.array(y)

def f_oscillator(t, y, m, k, alpha,b_damp, F0, omega, k_fric, n):
    x, v = y
    f_elastic = -k * x + k * alpha * (x**2)
    f_viscous = -b_damp*v

    if v == 0:
        f_kinetic = 0
    else:
        f_kinetic = -k_fric * m * (np.abs(v)**n) * np.sign(v)
    
    f_ext = F0 * np.sin(omega * t)
    dvdt = (f_elastic + f_viscous + f_kinetic + f_ext) / m
    return np.array([v, dvdt])

a = 0
b = 50
N = 5000
t_arr = np.linspace(a, b, N + 1)

m = 1.0
k = 1.0
omega_0 = np.sqrt(k/m)

y0 = [1.0, 0.0] 

import matplotlib.pyplot as plt

# Figure 1: Ảnh hưởng của tính phi tuyến (thay đổi alpha)
# Slide yêu cầu khảo sát V(x) có thêm số hạng bậc 3 (alpha)
plt.figure(figsize=(8,5))

# 1.1: alpha = 0
res_linear = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0, b_damp=0, F0=0, omega=0, k_fric=0, n=0), a, b, N, y0)
plt.plot(t_arr, res_linear[:, 0], "black", label=r"$\alpha = 0$")

# 1.2: alpha = 0.5
res_nonlin1 = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0.5, b_damp=0, F0=0, omega=0, k_fric=0, n=0), a, b, N, y0)
plt.plot(t_arr, res_nonlin1[:, 0], "b", label=r"$\alpha = 0.5$")

# 1.3: alpha = 0.9
res_nonlin2 = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0.9, b_damp=0, F0=0, omega=0, k_fric=0, n=0), a, b, N, y0)
plt.plot(t_arr, res_nonlin2[:, 0], "r", label=r"$\alpha = 0.9$")

plt.legend()
# plt.title("Figure 1: Free Oscillation - Linear vs Nonlinear (No damping, No forcing)")
plt.xlabel("Time $t$ (s)")
plt.ylabel("Position $x$ (m)")
plt.grid(True)
plt.savefig("images/osc_alpha.png", dpi=300)


# Figure 2: Hiện tượng cộng hưởng (thay đổi omega của ngoại lực)
plt.figure(figsize=(8,5))
F0_val = 0.5
b_small = 0.1

# 2.1: w = 0.5 * w0
res_w1 = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0, b_damp=b_small, F0=F0_val, omega=0.5*omega_0, k_fric=0, n=0), a, b, N, [0,0])
plt.plot(t_arr, res_w1[:, 0], "g", label=r"$\omega = 0.5\omega_0$")

# 2.2: w = w0
res_w2 = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0, b_damp=b_small, F0=F0_val, omega=omega_0, k_fric=0, n=0), a, b, N, [0,0])
plt.plot(t_arr, res_w2[:, 0], "r", label=r"Resonance: $\omega = \omega_0$")

# 2.3: w = 2.0 * w0
res_w3 = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0, b_damp=b_small, F0=F0_val, omega=2.0*omega_0, k_fric=0, n=0), a, b, N, [0,0])
plt.plot(t_arr, res_w3[:, 0], "b", label=r"$\omega = 2.0\omega_0$")

plt.legend()
# plt.title("Figure 2: Forced Oscillation & Resonance ($F_0=0.5$, small damping)")
plt.xlabel("Time $t$ (s)")
plt.ylabel("Position $x$ (m)")
plt.grid(True)
plt.savefig("images/osc_omega.png", dpi=300)

# Figure 3: Khảo sát ma sát nhớt (Viscous friction)
plt.figure(figsize=(8,5))
b_crit = 2 * m * omega_0

# 3.1: Underdamped (b < b_crit)
res_under = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0, b_damp=0.2*b_crit, F0=0, omega=0, k_fric=0, n=0), a, b, N, y0)
plt.plot(t_arr, res_under[:, 0], "b", label=r"Underdamped ($b < 2m\omega_0$)")

# 3.2: Critically (b = b_crit)
res_crit = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0, b_damp=b_crit, F0=0, omega=0, k_fric=0, n=0), a, b, N, y0)
plt.plot(t_arr, res_crit[:, 0], "r", label=r"Critically damped ($b = 2m\omega_0$)")

# 3.3: Overdamped (b > b_crit)
res_over = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0, b_damp=2.0*b_crit, F0=0, omega=0, k_fric=0, n=0), a, b, N, y0)
plt.plot(t_arr, res_over[:, 0], "g", label=r"Overdamped ($b > 2m\omega_0$)")

plt.legend()
# plt.title("Figure 3: Viscous Damping Effects (Free oscillation)")
plt.xlabel("Time $t$ (s)")
plt.ylabel("Position $x$ (m)")
plt.grid(True)
plt.xlim(0, 25)
plt.savefig("images/osc_viscous.png", dpi=300)

# Figure 3: Khảo sát ma sát (Kinetic friction)
plt.figure(figsize=(8,5))

res_nofric = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0, b_damp=0, F0=0, omega=0, k_fric=0, n=0), a, b, N, y0)
plt.plot(t_arr, res_nofric[:, 0], "b", label=r"$k = 0, n = 0$")

res_fric = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0, b_damp=0, F0=0, omega=0, k_fric=0.5, n=1.5), a, b, N, y0)
plt.plot(t_arr, res_fric[:, 0], "r", label=r"$k = 0.8, n = 1.5$")

plt.legend()
plt.xlabel("Time $t$ (s)")
plt.ylabel("Position $x$ (m)")
plt.grid(True)
plt.xlim(0, 25)
plt.savefig("images/osc_kinetic.png", dpi=300)

# Figure 5: Bài toán tổng hợp (Nonlinear + Damped + Forced)
plt.figure(figsize=(8,5))

res_full = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0.1, b_damp=0.2, F0=1.0, omega=1.2, k_fric=0.5, n=1.5), a, b, N, y0)
t_full = np.linspace(a, b, N+1)
plt.plot(t_full, res_full[:, 0], "g", label=r"$\alpha=0.1, b=0.2, F_0=1.0, \omega=1.2, k=0.5, n=1.5$")

res_full = rk4(lambda t, y: f_oscillator(t, y, m, k, alpha=0.3, b_damp=0.1, F0=2.0, omega=3, k_fric=0.5, n=1.5), a, b, N, y0)
t_full = np.linspace(a, b, N+1)
plt.plot(t_full, res_full[:, 0], "r", label=r"$\alpha=0.3, b=0.1, F_0=2.0, \omega=1.2, k=0.2, n=1.5$")

plt.legend()
plt.xlabel("Time $t$ (s)")
plt.ylabel("Position $x$ (m)")
plt.grid(True)
plt.savefig("images/osc_full.png", dpi=300)
