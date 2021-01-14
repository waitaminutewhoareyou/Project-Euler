import numpy
from tqdm import trange
def countSum(n, threshold=5000):
    f = {0: [[]]}

    prime_ls = primesfrom2to(n)
    for num in trange(2,n+1):
        val = []
        for predecessor in prime_ls:
            if predecessor > num:
                break
            if num-predecessor not in f:
                continue
            pre_sols = [sol[:] for sol in  f[num-predecessor]]
            for sol in pre_sols:
                sol.append(predecessor)
                sol.sort()
                if sol not in val:
                    val.append(sol)
        f[num] = val
        if len(val)>threshold:
            print(f'Found {num}.')
            return
    return len(f[n])

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

if __name__ == '__main__':
    print(countSum(80))

