from itertools import permutations
from tqdm import tqdm


def partitions(s):
    if len(s) > 0:
        for i in range(1, len(s)+1):
            first, rest = s[:i], s[i:]
            for p in partitions(rest):
                yield [first] + p
    else:
        yield []

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

count = 0
record = []
for permu_str in tqdm(list(permutations(''.join(map(str,range(1,10)))))):
    for result in partitions(''.join(permu_str)):
        if all(map(lambda x: is_prime(int(x)), result)):
            if set(result) not in record:
                count += 1
                record.append(set(result))

print(count)