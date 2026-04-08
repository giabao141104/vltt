import numpy as np

def rk4(f,a,b,N,y0):
    h = (b - a)/N
    t = a
    y = [np.array(y0)]

    for i in range(1,N+1):
        k1 = h*f(t,       y[-1])
        k2 = h*f(t + h/2, y[-1] + k1/2)
        k3 = h*f(t + h/2, y[-1] + k2/2)
        k4 = h*f(t + h,   y[-1] + k3)
        yi = y[-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        y.append(yi)
        t = t + h

    return np.array(y)
def f_nodrag(t,y):
    g = 9.81
    coord_x, coord_y, vx, vy = y
    return np.array([vx, vy, 0, -g])
def y_ideal(x,y0):
    g = 9.81
    coord_x0, coord_y0, vx0, vy0 = y0
    return (vy0/vx0)*x - (g/(2*(vx0**2)))*(x**2)

def get_H(init):
    g = 9.81
    v0, angle, coord_x0, coord_y0 = init
    theta = np.radians(angle)
    H = (v0**2)*(np.sin(theta)**2)/(2*g)
    return H

def get_R(init):
    g = 9.81
    v0, angle, coord_x0, coord_y0 = init
    theta = np.radians(angle)
    R = 2*(v0**2)*np.cos(theta)*np.sin(theta)/g
    return R
def f_drag_total(t,y,n=1):
    g = 9.81
    k = 0.8
    coord_x, coord_y, vx, vy = y
    vxp = -k * ((vx**2 + vy**2)**((n - 1)/2)) * vx
    vyp = -k * ((vx**2 + vy**2)**((n - 1)/2)) * vy - g
    return np.array([vx, vy, vxp, vyp])
def f_drag_comp(t,y):
    g = 9.81
    k = 0.8
    n = 1
    coord_x, coord_y, vx, vy = y
    vxp = -k * vx**(n + 1)/np.sqrt(vx**2 + vy**2)
    vyp = -k * vy**(n + 1)/np.sqrt(vx**2 + vy**2) - g
    return np.array([vx, vy, vxp, vyp])

def init_setup(init):
    v0, angle, coord_x0, coord_y0 = init
    theta = np.radians(angle)
    vx0 = v0*np.cos(theta)
    vy0 = v0*np.sin(theta)
    y0 = [coord_x0, coord_y0, vx0, vy0]
    return y0

a = 0
b = 10
N = 5000

def print_range_height(data,init,e=1):
    Hi = np.argmax(data[:, 1])
    Ha = data[Hi, 1]
    He = get_H(init)
    Herr = Ha/He
    Ri = np.abs(data[Hi:, 1]).argmin()
    Ra = data[Ri + Hi, 0]
    Re = get_R(init)
    Rerr = Ra/Re
    print("H = ", Ha, "(appr.)")
    if (e == 1):
        print("H = ", He, "(exact)")
        print("err = ", Herr)
    print("R = ", Ra, "(appr.)")
    if (e == 1):
        print("R = ", Re, "(exact)")
        print("err = ", Rerr,)
    return [Ha, He, Herr, Ra, Re, Rerr]

import matplotlib.pyplot as plt

# Figure 1: So sánh quỹ đạo trong chân không và quỹ đạo khi có lực cản không khí
plt.figure(figsize=(8,5))

results_nodrag_ideal = np.zeros((5000, 2))
results_nodrag_ideal[:, 0] = np.linspace(0,230,5000)
init = [50,60,0,0]
y0 = init_setup(init)

results_nodrag_ideal[:, 1] = y_ideal(results_nodrag_ideal[:, 0], y0)
plt.plot(results_nodrag_ideal[:,0], results_nodrag_ideal[:,1], "b",
         label=r"$\alpha = 60, k = 0, n = 0$")
results_drag_total = rk4(lambda t,y: f_drag_total(t,y,n=1),a,b,N,y0)
plt.plot(results_drag_total[:,0], results_drag_total[:,1], "r",
         label=r"$\alpha = 60, k = 0.8, n = 1$")
plt.legend()
plt.title(r"$v_0 = 50$")
plt.xlim(0)
plt.ylim(0)
plt.xlabel(r"$x$ (m)")
plt.ylabel(r"$y$ (m)")
plt.savefig("images/drag_vs_nodrag.png", dpi = 300)

# Figure 2: Ảnh hưởng của góc bắn tới tầm xa
plt.figure(figsize=(8,5))

results_nodrag_ideal = np.zeros((10000, 2))
results_nodrag_ideal[:, 0] = np.linspace(0,5000,10000)

print("v0 = 200, alpha = 30")
init = [200,30,0,0]
y0 = init_setup(init)
results_drag_total = rk4(lambda t,y: f_drag_total(t,y,n=2),a,b,N,y0)
plt.plot(results_drag_total[:,0], results_drag_total[:,1],
         "r", label=r"$\alpha = 30, k = 0.8, n = 2$")
results_nodrag_ideal[:, 1] = y_ideal(results_nodrag_ideal[:, 0], y0)
plt.plot(results_nodrag_ideal[:,0], results_nodrag_ideal[:,1],
         "r", ls = "--", label=r"$\alpha = 30, k = 0, n = 0$")
R30 = print_range_height(results_nodrag_ideal,init)

print("v0 = 200, alpha = 45")
init = [200,45,0,0]
y0 = init_setup(init)
results_drag_total = rk4(lambda t,y: f_drag_total(t,y,n=2),a,b,N,y0)
plt.plot(results_drag_total[:,0], results_drag_total[:,1],
         "g", label=r"$\alpha = 45, k = 0.8, n = 2$")
results_nodrag_ideal[:, 1] = y_ideal(results_nodrag_ideal[:, 0], y0)
plt.plot(results_nodrag_ideal[:,0], results_nodrag_ideal[:,1],
         "g", ls = "--", label=r"$\alpha = 45, k = 0, n = 0$")
R45 = print_range_height(results_nodrag_ideal,init)

print("v0 = 200, alpha = 60")
init = [200,60,0,0]
y0 = init_setup(init)
results_drag_total = rk4(lambda t,y: f_drag_total(t,y,n=2),a,b,N,y0)
plt.plot(results_drag_total[:,0], results_drag_total[:,1],
         "b", label=r"$\alpha = 60, k = 0.8, n = 2$")
results_nodrag_ideal[:, 1] = y_ideal(results_nodrag_ideal[:, 0], y0)
plt.plot(results_nodrag_ideal[:,0], results_nodrag_ideal[:,1],
         "b", ls = "--", label=r"$\alpha = 60, k = 0, n = 0$")
R60 = print_range_height(results_nodrag_ideal,init)

f = open("data/latex_table.tex", "w")
f.write(r"\multirow{3}{*}{\(H_{\max}\) (\unit{\meter})}")
f.write("\n")
f.write("& Kết quả RK4   & \\num{{{:.6f}}}  & \\num{{{:.6f}}}  & \\num{{{:.6f}}} \\\\\n".format(R30[0], R45[0], R60[0]))
f.write("& Lý thuyết     & \\num{{{:.6f}}}  & \\num{{{:.6f}}}  & \\num{{{:.6f}}} \\\\\n".format(R30[1], R45[1], R60[1]))
f.write("& Sai số tỷ đối & \\num{{{:.6f}}}  & \\num{{{:.6f}}}  & \\num{{{:.6f}}} \\\\\n".format(R30[2], R45[2], R60[2]))
f.write(r"\midrule")
f.write("\n")
f.write(r"\multirow{3}{*}{\(R\) (\unit{\meter})}")
f.write("\n")
f.write("& Kết quả RK4   & \\num{{{:.6f}}}  & \\num{{{:.6f}}}  & \\num{{{:.6f}}} \\\\\n".format(R30[3], R45[3], R60[3]))
f.write("& Lý thuyết     & \\num{{{:.6f}}}  & \\num{{{:.6f}}}  & \\num{{{:.6f}}} \\\\\n".format(R30[4], R45[4], R60[4]))
f.write("& Sai số tỷ đối & \\num{{{:.6f}}}  & \\num{{{:.6f}}}  & \\num{{{:.6f}}} \\\\\n".format(R30[5], R45[5], R60[5]))
f.close()

plt.legend()
plt.title(r"$v_0 = 200$")
plt.xlim(0,6)
plt.ylim(0,5)
plt.xlabel(r"$x$ (m)")
plt.ylabel(r"$y$ (m)")
plt.savefig("images/drag_angle.png", dpi = 300)

# Figure 3: Ảnh hưởng của số mũ lực cản đến hình dạng quỹ đạo
plt.figure(figsize=(8,5))

init = [50,45,0,0]
y0 = init_setup(init)
results_drag_total = rk4(lambda t,y: f_drag_total(t,y,n=1),a,b,N,y0)
plt.plot(results_drag_total[:,0], results_drag_total[:,1],
         "b", label=r"$n = 1$")
print_range_height(results_drag_total,init,e=0)

results_drag_total = rk4(lambda t,y: f_drag_total(t,y,n=1.5),a,b,N,y0)
plt.plot(results_drag_total[:,0], results_drag_total[:,1],
         "g", label=r"$n = 1.5$")
print_range_height(results_drag_total,init,e=0)

results_drag_total = rk4(lambda t,y: f_drag_total(t,y,n=2),a,b,N,y0)
plt.plot(results_drag_total[:,0], results_drag_total[:,1],
         "r", label=r"$n = 2$")
print_range_height(results_drag_total,init,e=0)

plt.legend()
plt.title(r"$v_0 = 50, \alpha = 45, k = 0.8$")
plt.xlim(0)
plt.ylim(0)
plt.xlabel(r"$x$ (m)")
plt.ylabel(r"$y$ (m)")
plt.savefig("images/drag_exponent.png", dpi = 300)

# Figure 4: Khảo sát sự phụ thuộc của quỹ đạo vào vận tốc đầu
plt.figure(figsize=(8,5))

init = [50,45,0,0]
y0 = init_setup(init)
results_drag_total = rk4(lambda t,y: f_drag_total(t,y,n=2),a,b,N,y0)
plt.plot(results_drag_total[:,0], results_drag_total[:,1],
         "black", label=r"$v_0 = 50$")

init = [100,45,0,0]
y0 = init_setup(init)
results_drag_total = rk4(lambda t,y: f_drag_total(t,y,n=2),a,b,N,y0)
plt.plot(results_drag_total[:,0], results_drag_total[:,1],
         "r", label=r"$v_0 = 100$")

init = [200,45,0,0]
y0 = init_setup(init)
results_drag_total = rk4(lambda t,y: f_drag_total(t,y,n=2),a,b,N,y0)
plt.plot(results_drag_total[:,0], results_drag_total[:,1],
         "g", label=r"$v_0 = 200$")

init = [300,45,0,0]
y0 = init_setup(init)
results_drag_total = rk4(lambda t,y: f_drag_total(t,y,n=2),a,b,N,y0)
plt.plot(results_drag_total[:,0], results_drag_total[:,1],
         "b", label=r"$v_0 = 300$")
plt.legend()
plt.title(r"$\alpha = 45, k = 0.8, n = 2$")
plt.xlim(0)
plt.ylim(0)
plt.xlabel(r"$x$ (m)")
plt.ylabel(r"$y$ (m)")
plt.savefig("images/drag_velocity.png", dpi = 300)
