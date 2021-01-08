'''


A 30×30 grid of squares contains 900 fleas, initially one flea per square.
When a bell is rung, each flea jumps to an adjacent square at random (usually 4 possibilities, except for fleas on the edge of the grid or at the corners).

What is the expected number of unoccupied squares after 50 rings of the bell? Give your answer rounded to six decimal places.
'''

import numpy as np
from tqdm import tqdm
from multiprocessing import Pool

class Flea:
    def __init__(self, position, shape):
        self.shape = shape
        self.max_x, self.max_y = shape
        self.position = position
        self.x, self.y = position
        self.valid_postions = [(x, y) for x in range(self.max_x) for y in range(self.max_y)]

    def adjacentPosition(self):
        potential_positions = [(self.x + dx, self.y + dy) for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        adj = [position for position in potential_positions if position in self.valid_postions]
        return adj

    def jump(self):
        adj_pos = self.adjacentPosition()
        # np.random.randint(len(adj_pos))
        next_pos = adj_pos[np.random.randint(len(adj_pos))]
        # next_pos = np.random.choice(adj_pos)
        assert next_pos in self.valid_postions, f'{next_pos} is not valid.'
        return next_pos


class FleaCircus:
    def __init__(self, shape = (30, 30)):
        self.shape = shape
        self.max_x, self.max_y = shape
        self.num_fleas = np.prod(shape)
        self.fleas = [Flea((x,y), self.shape) for x in range(self.max_x) for y in range(self.max_y)]
        self.valid_postions = [(x, y) for x in range(self.max_x) for y in range(self.max_y)]

    def bellRing(self, iter_nums=50):
        for iteration in range(iter_nums):
            new_config = [flea.jump() for flea in self.fleas]
            self.fleas = [Flea(pos, self.shape) for pos in new_config]
        return new_config

    def countEmptySquares(self):
        final_config = self.bellRing()
        # count_empty = 0
        # for x in range(self.max_x):
        #     for y in range(self.max_y):
        #         if [x,y] not in final_config:
        #             count_empty += 1
        count_empty = len(set(self.valid_postions) - set(final_config))
        return count_empty

if __name__ == '__main__':
    board_shape = (30, 30)
    num_simulations = 10**6
    pbar = tqdm(total=num_simulations, desc='simulated')
    empty = 0
    for _ in range(1, num_simulations+1):
        instance = FleaCircus(board_shape)
        empty += instance.countEmptySquares()
        pbar.set_postfix(expectedEmpty = f'{empty/_}')
        pbar.update()

    print(empty/num_simulations)