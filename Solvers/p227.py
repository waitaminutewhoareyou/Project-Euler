# simulation script
# see p227.nb for analytic solution

import numpy as np
from tqdm import tqdm
n = 100

class Roll:
    def __init__(self, position):
        # self.pos = position % n
        self.pos = self.loc(position)

    def roll(self):
        dx = np.random.choice([-1, 0, 1], p=[1/6, 2/3, 1/6])
        self.pos += dx
        self.pos = self.loc(self.pos)
        # return self.loc(self.pos)

    def loc(self,position):
        return position % n



def trial():

    count = 0
    rolls = [Roll(0), Roll(n // 2)]
    while True:
        for roll in rolls:
            roll.roll()
        if rolls[0].pos == rolls[1].pos:
            break
        count += 1
    return count


if __name__ == '__main__':

    num_simulations = 10**6
    pbar = tqdm(total=num_simulations, desc='simulated')
    success = 0
    for _ in range(1, num_simulations+1):
        success += trial()
        pbar.set_postfix(avegrageSteps = f'{success/_}')
        pbar.update()

    print(success/num_simulations)