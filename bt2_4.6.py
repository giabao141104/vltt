import numpy as np
import matplotlib.pyplot as plt

# Tham số
so_hat_ban_dau = 1000
hang_so_phan_ra = 0.1
buoc_thoi_gian = 0.1
xac_suat_phan_ra = hang_so_phan_ra * buoc_thoi_gian

so_lan_mo_phong = 50   # số lần chạy

# Trục thời gian cố định
so_buoc = 200
ds_thoi_gian = np.linspace(0, so_buoc * buoc_thoi_gian, so_buoc)

# Lưu kết quả trung bình
tong_so_hat = np.zeros(so_buoc)

# Lặp nhiều lần mô phỏng
for lan in range(so_lan_mo_phong):
    so_hat = so_hat_ban_dau
    ket_qua = []

    for buoc in range(so_buoc):
        so_hat_phan_ra = 0

        for i in range(so_hat):
            if np.random.rand() < xac_suat_phan_ra:
                so_hat_phan_ra += 1

        so_hat -= so_hat_phan_ra
        ket_qua.append(so_hat)

    tong_so_hat += np.array(ket_qua)

# Trung bình
so_hat_trung_binh = tong_so_hat / so_lan_mo_phong

# Nghiệm giải tích
so_hat_giai_tich = so_hat_ban_dau * np.exp(-hang_so_phan_ra * ds_thoi_gian)

# Vẽ
plt.plot(ds_thoi_gian, so_hat_trung_binh, label="Trung binh Monte Carlo")
plt.plot(ds_thoi_gian, so_hat_giai_tich, '--', label="Nghiem giai tich")

plt.xlabel("Thoi gian")
plt.ylabel("So hat con lai")
plt.legend()
plt.show()