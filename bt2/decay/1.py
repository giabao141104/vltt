import numpy as np
import matplotlib.pyplot as plt

# Thiet lap cac thong so ban dau
so_hat_ban_dau = 100000
hang_so_phan_ra = 0.005
tong_thoi_gian = 500

thoi_gian = np.arange(0, tong_thoi_gian + 1)
so_hat_con_lai = np.zeros(len(thoi_gian))
toc_do_phan_ra = np.zeros(len(thoi_gian))
hat_hien_tai = so_hat_ban_dau

for t in thoi_gian:
    so_hat_con_lai[t] = hat_hien_tai
    
    # Tinh so hat phan ra trong buoc thoi gian nay
    hat_phan_ra = 0
    for _ in range(int(hat_hien_tai)):
        if np.random.random() < hang_so_phan_ra:
            hat_phan_ra += 1
    
    toc_do_phan_ra[t] = hat_phan_ra
    hat_hien_tai -= hat_phan_ra

# Ve do thi
plt.figure(figsize=(10, 5))
plt.plot(thoi_gian, np.log(so_hat_con_lai), label='ln(N(t))')
# Tranh log(0) neu toc do phan ra bang 0
plt.plot(thoi_gian, np.log(toc_do_phan_ra + 1e-9), label='ln(Delta N / Delta t)', alpha=0.7)
plt.xlabel('Thoi gian (t)')
plt.ylabel('Gia tri Logarit')
plt.title('Do thi Logarit cua so hat va toc do phan ra')
plt.legend()
plt.grid(True)
plt.show()

# Xuất dữ liệu ra file
data_file = "phong_xa_data.dat"
data_to_save = np.column_stack((thoi_gian, so_hat_con_lai, toc_do_phan_ra))
np.savetxt(data_file, data_to_save, header="Thoi_gian N_t Toc_do", comments='')

# Tạo file script cho gnuplot
gnuplot_script = "plot_script.gp"
with open(gnuplot_script, "w") as f:
    f.write(f"""
set title "Do thi Logarit cua so hat va toc do phan ra (Gnuplot)"
set xlabel "Thoi gian (t)"
set ylabel "Gia tri Logarit"
set grid
set key outside

plot "{data_file}" u 1:(log($2)) with lines title "ln(N(t))" lw 2, \\
     "{data_file}" u 1:(log($3 + 1e-9)) with lines title "ln(Delta N / Delta t)" lw 1.5
    """)
print(f"Da xuat file du lieu: {data_file}")
print(f"Da tao script gnuplot: {gnuplot_script}")