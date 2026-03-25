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
plt.savefig("images/1.png", dpi=300)

# Xuất dữ liệu ra file
data_file = "data/phong_xa_data.dat"
data_to_save = np.column_stack((thoi_gian, so_hat_con_lai, toc_do_phan_ra))
np.savetxt(data_file, data_to_save, header="Thoi_gian N_t Toc_do", comments='')
