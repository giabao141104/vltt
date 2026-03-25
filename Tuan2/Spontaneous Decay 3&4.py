import numpy as np
import matplotlib.pyplot as plt
import random

# Ham mo phong loi
def mo_phong(n0, lambda_val, t_max=1000):
    t_list = []
    n_list = []
    dn_list = [] # So hat phan ra tai moi buoc (delta N)
    
    n_hien_tai = n0
    for t in range(t_max):
        t_list.append(t)
        n_list.append(n_hien_tai)
        
        # Stochastic: xac dinh so hat phan ra
        hat_phan_ra = 0
        if n_hien_tai > 0:
            # Dung binomial distribution de mo phong nhanh va chinh xac tinh ngau nhien
            hat_phan_ra = np.random.binomial(int(n_hien_tai), lambda_val)
        
        dn_list.append(hat_phan_ra)
        n_hien_tai -= hat_phan_ra
        if n_hien_tai < 0: n_hien_tai = 0         
    return np.array(t_list), np.array(n_list), np.array(dn_list)

# YEU CAU 3:
# Hinh 3a: Do doc doc lap voi N(0)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
n0_list = [5000, 10000, 20000]
lam = 0.005
for n0 in n0_list:
    t, n, dn = mo_phong(n0, lam)
    mask = n > 10 # Tranh nhieu khi n qua nho
    plt.plot(t[mask], np.log(n[mask]), label=f'N0={n0}')
plt.title('3a. Do doc khong doi voi N0 khac nhau')
plt.xlabel('Thoi gian'); plt.ylabel('ln(N)')
plt.legend()

# Hinh 3b: Do doc ti le thuan voi Lambda
plt.subplot(1, 2, 2)
lambda_list = [0.005, 0.01, 0.015]
n0_fixed = 10000
for l in lambda_list:
    t, n, dn = mo_phong(n0_fixed, l)
    mask = n > 10
    plt.plot(t[mask], np.log(n[mask]), label=f'lambda={l}')
plt.title('3b. Do doc thay doi theo Lambda')
plt.xlabel('Thoi gian'); plt.ylabel('ln(N)')
plt.legend()
plt.tight_layout()
plt.show()

# YEU CAU 4: ln(N) VA ln(delta N) TY LE THUAN
plt.figure(figsize=(7, 6))
t, n, dn = mo_phong(100000, 0.005, t_max=800)

# Loc cac diem ma delta N > 0 de ve logarit
mask = (n > 0) & (dn > 0)
ln_n = np.log(n[mask])
ln_dn = np.log(dn[mask])

plt.scatter(ln_n, ln_dn, s=1, alpha=0.5, color='red')
plt.title('Yeu cau 4: ln(delta N) ti le thuan voi ln(N)')
plt.xlabel('ln(N)')
plt.ylabel('ln(delta N)')
plt.grid(True, linestyle='--')

# Ve duong xu huong ly thuyet de kiem chung
plt.plot(ln_n, ln_n + np.log(0.005), color='black', linestyle='--', label='Ly thuyet (Slope=1)')
plt.legend()
plt.show()

for n0 in n0_list:
    t, n, dn = mo_phong(n0, lam)
    data = np.column_stack((t, n))
    np.savetxt(f"data_3a_N0_{n0}.dat", data, header="t N", comments='')

for l in lambda_list:
    t, n, dn = mo_phong(n0_fixed, l)
    data = np.column_stack((t, n))
    np.savetxt(f"data_3b_lambda_{l}.dat", data, header="t N", comments='')

data4 = np.column_stack((ln_n, ln_dn))
np.savetxt("data_4_lnN_lnDN.dat", data4, header="lnN lnDN", comments='')
print("Da xuat file .dat xong!")