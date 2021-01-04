from itertools import product
import numpy as np
from tqdm import tqdm

def allWinningSituation(num_games):
    total_prob = 0
    for game in tqdm(list(product([0, 1], repeat=num_games)),desc='simulated'):
        game = list(map(int, game))
        if sum(game) > 1/2 * len(game):
            prob_ = 1
            for ix, outcome in enumerate(game):
               probability = 1/(2+ix) if outcome else 1-1/(2+ix)
               prob_ *= probability
            total_prob += prob_
    return total_prob

print(int(1/allWinningSituation(15)))