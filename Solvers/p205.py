'''
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
'''

from tqdm import tqdm, trange
import numpy as np

num_iter = 10**7
pbar = tqdm(total=num_iter)

win = 0
for games in range(1, num_iter):
    result = (np.random.randint(1,5,size=9).sum() > np.random.randint(1,7,size=6).sum())
    if games > num_iter / 10:
        if np.abs((result + win)/games - prob) < 1e-7:
            break
    win += (np.random.randint(1,5,size=9).sum() > np.random.randint(1,7,size=6).sum())
    prob = win/games
    pbar.update()
    pbar.set_postfix(probability = f'{prob:.7f}')
print(prob)

