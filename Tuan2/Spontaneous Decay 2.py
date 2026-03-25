import numpy as np
import matplotlib.pyplot as plt
import random

# Thong so co ban
lambda_hang_so = 0.01 
thoi_gian_max = 800
danh_sach_N0 = [10, 100, 1000, 10000, 100000]

plt.figure(figsize=(10, 6))

for n0 in danh_sach_N0:
    hien_tai = n0
    lich_su_n = []
    
    # Vong lap mo phong don gian
    for t in range(thoi_gian_max):
        lich_su_n.append(hien_tai)
        
        # Tinh so hat phan ra (ngau nhien)
        hat_phan_ra = 0
        for _ in range(int(hien_tai)):
            if random.random() < lambda_hang_so:
                hat_phan_ra += 1
        hien_tai -= hat_phan_ra
        
        if hien_tai < 0: hien_tai = 0

    # Chuyen sang mang de ve do thi
    n_mang = np.array(lich_su_n)
    t_mang = np.arange(thoi_gian_max)
    
    # Loc du lieu de ve log ko bi loi
    mask = n_mang > 0
    plt.plot(t_mang[mask], np.log10(n_mang[mask]), 
             label=f'N0 = {n0}', 
             drawstyle='steps-post')

plt.title('Yeu cau 2: Tinh ngau nhien (N nho) vs Ham mu (N lon)')
plt.xlabel('Thoi gian (t)')
plt.ylabel('log10[N(t)]')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()




