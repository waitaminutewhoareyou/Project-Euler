import numpy as np

class LargestProduct:
    def __init__(self, dir):
        self.array = []
        f = open(dir, 'r')
        self.array = np.array([line.strip().split() for line in f]).astype(float)
        self.curmax = 0


    def main(self):
        row_num, col_num = self.array.shape
        for row_ix in range(row_num):
            for col_ix in range(col_num):
                right = np.prod(self.array[row_ix, col_ix:min(col_num-1, col_ix+4)])
                down = np.prod(self.array[row_ix:min(row_num-1, row_ix+4), col_ix])
                right_up = np.prod([self.array[max(row_ix-i, 0), min(col_ix+i, col_num-1)] for i in range(4)])
                right_down = np.prod([self.array[min(row_ix+i, row_num-1), min(col_ix+i, col_num-1)] for i in range(4)])
                self.curmax = max(self.curmax, right, down, right_up, right_down)
        return self.curmax


if __name__ == '__main__':
    instance = LargestProduct('p011.txt')
    print(instance.main())