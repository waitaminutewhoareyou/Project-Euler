from tqdm import tqdm
from time import sleep
import sys

'''
Key Observation:
a hyper n (mod m)
    =
a hyper ( a hyper n-1 (mod m)) (mod m)

by induction
'''
def hyperMod(base, n, m):
    pbar.update(1)
    sleep(0.01)
    if n==1:
        return base % m

    return pow(base, hyperMod(base,n-1,m) ,m)

base = 1777
power = 1855
mod = int(10**8)
pbar = tqdm(total=power)
if sys.getrecursionlimit() < power:
    sys.setrecursionlimit(power*3)
print('result', hyperMod(base, power, mod))