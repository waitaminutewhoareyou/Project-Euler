################################# Solve by intuition #################################################
'''
f(n):= Number of admissible strings of length n composed of 'L', 'O', and 'A'
g(n):= Number of admissible strings of length n composed of 'O' and 'A' only

Divide and Conquer
f(n) = # of strings with L + # of strings without L

# of strings without L =  g(n)
 = 2*g(n-1) - g(n-4)
 where we multiply g(n) by 2 because last digit can be either 'O' or 'A'
 Furthermore, we subtract g(n-4) because when we append 'A' at the end, those g(n-1) sequences ending
 with 'AA' must be removed, such removed sequence must therefore have 'O' at (n-3)th position, so the first
 (n-4) digits are unconstrained, yielding g(n-4).

# of strings without L
 = sum g(b-j)*g(j-4) from j=1 to j=n
where j represents the position where 'L' occurs. Occurrence of 'L' would partition the string into two independent
substrings.

'''

def f(n):
    countWithL = 0
    for j in range(1,n+1):
        countWithL += g(n-j)*g(j-1)
    return countWithL + g(n)

def g(n):
    if n in [0,1,2,3,4]:
        return [1,2,4,7,13][n]
    return 2*g(n-1) - g(n-4)

print(f(30))


################################# Brute force search #################################################
n = 30
def bruteForce(string, length):
    if length == 0:
        yield string

    elif 'L' in string:
        if len(string) >= 2 and string[-2:] == 'AA':
            yield from bruteForce(string + 'O', length - 1)
        else:
            yield from bruteForce(string + 'A', length-1)
            yield from bruteForce(string + 'O', length-1)

    elif len(string)>=2 and string[-2:] == 'AA':
        yield from bruteForce(string + 'O', length - 1)
        yield from bruteForce(string + 'L', length - 1)
    else:
        yield from bruteForce(string + 'O', length-1)
        yield from bruteForce(string + 'A', length-1)
        yield from bruteForce(string + 'L', length-1)

count = 0
for x in bruteForce('', 30):
    count += 1
print(count)

