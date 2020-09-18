from sympy import isprime

class SpiralPrime():
    def __init__(self, n):
        self.n = n
    def GenerateLayer(self):
        width = self.n
        assert width % 2 == 1, "width must be odd"
        increment = 2
        diagonal = 1
        res = [1]
        period = (width + 1) / 2
        while len(res) < 2 * width - 1:
            for _ in range(4):
                diagonal += increment
                res.append(diagonal)
            increment += 2
        return res
    def count(self):
        res = list(map(isprime, self.GenerateLayer()))
        return sum(res)/len(res)
# test = SpiralPrime(7)
# print(test.count())

sidelength = 3
while  SpiralPrime(sidelength).count() >= 10/100:
    print("The density is {0} with sidelength {1}".format(SpiralPrime(sidelength).count(), sidelength))
    sidelength += 2
print(sidelength)
