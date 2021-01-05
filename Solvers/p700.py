import numpy as np
'''
With Mathematica
FindInstance[
 Mod[1504170715041707*n, 4503599627370517] == 0, n, PositiveIntegers]
 {{n -> 9007199254741034}}
'''


def fastlinearcongruence(powx, divmodx, N, withstats=False):
    x, y, z = egcditer(powx, N, withstats)
    answer = (y * divmodx) % N

    if x > 1:
        powx //= x
        divmodx //= x
        N //= x
    answer = (y * divmodx) % N
    return answer


def egcditer(a, b, withstats=False):
    s = 0
    r = b
    old_s = 1
    old_r = a
    quotient = 0

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    if b != 0:
        bezout_t = quotient = (old_r - old_s * a) // b

    else:
        bezout_t = 0
    return old_r, old_s, bezout_t

forward_n = 1
for_min = 1504170715041707
backward_val = 1
backward_n = 3451657199285664
back_max = np.inf
res = for_min
sanity = [np.inf]
while backward_n > forward_n:
    # forward
    for_val = (1504170715041707*forward_n) % 4503599627370517
    if for_val < for_min:
        for_min = for_val
        res += for_min
    forward_n += 1

    # backward
    backward_n = fastlinearcongruence(1504170715041707, backward_val,  4503599627370517)
    if backward_n < back_max:
        back_max = backward_n
        res += backward_val
    else:
        backward_n = back_max

    backward_val += 1

    diff = backward_n-forward_n
    assert diff < sanity[-1]
    sanity.append(diff)
    # print('diff', diff)

print(res)