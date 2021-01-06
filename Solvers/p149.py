import numpy as np
import scipy.signal
from multiprocessing import Pool
from tqdm import tqdm
import os
# D = np.array([[-2,5,3,2],
#               [9,-6,5,1],
#               [3,2,7,3],
#               [-1,8,-4,8]]
#              )

# D = np.random.randint(20,size=(2000, 2000))

def s(k):
    if 1 <= k <=55:
        q, r = divmod(100003 - 200003*k + 300007 * k**3, 1000000)
        return r - 500000
    else:
        f = [0] + [s(k) for k in range(1, 56)]
        ix = 56
        while ix <= k:
            q, r = divmod(f[ix - 24] + f[ix - 55] + 1000000, 1000000)
            f.append(r - 500000)
            ix += 1

        D = np.array(f[1:]).reshape((2000, 2000))
        return f[-1], D

x, D = s(4000000)


# filter_horizontal = np.array([[0,0,0],[1,1,1],[0,0,0]])
filter_horizontal = np.ones((1, 2000))
filter_vertical = np.ones((2000, 1))
filter_diagonal = np.eye(2000)
filter_antidiagonal = filter_diagonal[::-1]

def applyFilter(filter):
    return scipy.signal.convolve2d(D, filter, mode='same').max()


# print(max(map(applyFilter, [filter_horizontal, filter_vertical, filter_diagonal, filter_antidiagonal])))

if __name__ == '__main__':
    with Pool(os.cpu_count()-3) as p:
        r= list(tqdm(p.imap(applyFilter, [filter_horizontal, filter_vertical, filter_diagonal, filter_antidiagonal]),total = 4 ))
        print(max(r))
        p.close()
        p.join()