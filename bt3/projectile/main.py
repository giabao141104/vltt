import numpy as np

def rk4(fp,filenames,a,b,N,alpha):
    h = (b - a)/N
    x = a
    y = np.array(alpha)
    m = len(y)

    results = []
    results.append(list(y))

    files = []
    for f in filenames:
        files.append(open(f, "w"))

    for i in range (1,N+1):
        k1 = h*np.array(fp(x,y))
        k2 = h*np.array(fp(x + h/2,y + k1/2))
        k3 = h*np.array(fp(x + h/2,y + k2/2))
        k4 = h*np.array(fp(x + h,y + k3))
        y = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        for j in range(0,m):
            files[j].write(f"{x} {y[j]}\n")
        x = x + h
        results.append(list(y))

    for f in files:
        f.close()

    return results
