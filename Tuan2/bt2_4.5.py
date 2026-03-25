import numpy as np
import matplotlib.pyplot as plt

# Tham số
so_hat_ban_dau = 1000
hang_so_phan_ra = 0.1
buoc_thoi_gian = 0.1
xac_suat_phan_ra = hang_so_phan_ra * buoc_thoi_gian

so_hat = so_hat_ban_dau
thoi_gian = 0

ds_thoi_gian = []
ds_so_hat = []

while so_hat > 0:
    so_hat_phan_ra = 0
    
    for i in range(so_hat):
        if np.random.rand() < xac_suat_phan_ra:
            so_hat_phan_ra += 1

    so_hat -= so_hat_phan_ra
    thoi_gian += buoc_thoi_gian

    ds_thoi_gian.append(thoi_gian)
    ds_so_hat.append(so_hat)

# Nghiệm giải tích
thoi_gian_giai_tich = np.linspace(0, max(ds_thoi_gian), 100)
so_hat_giai_tich = so_hat_ban_dau * np.exp(-hang_so_phan_ra * thoi_gian_giai_tich)

# Vẽ đồ thị
plt.plot(ds_thoi_gian, ds_so_hat, 'o', label="Monte Carlo")
plt.plot(thoi_gian_giai_tich, so_hat_giai_tich, '-', label="Nghiem giai tich")

plt.xlabel("Thoi gian")
plt.ylabel("So hat con lai")
plt.legend()
plt.show()