

# The Sudoku board is a 9x9 grid, which is further divided into a 3x3 grid
# of 3x3 grids.  Each cell in the grid must take a value from 0 to 9.
# No two grid cells in the same row, column, or 3x3 subgrid may take the
# same value.
#
# In the MIP formulation, binary variables x[i,j,v] indicate whether
# cell <i,j> takes value 'v'.  The constraints are as follows:
#   1. Each cell must take exactly one value (sum_v x[i,j,v] = 1)
#   2. Each value is used exactly once per row (sum_i x[i,j,v] = 1)
#   3. Each value is used exactly once per column (sum_j x[i,j,v] = 1)
#   4. Each value is used exactly once per 3x3 subgrid (sum_grid x[i,j,v] = 1)
#
# Input datasets for this example can be found in examples/data/sudoku*.


from os.path import dirname, join
project_root = dirname(dirname(__file__))
data_path = join(project_root, 'Data', '')
import os
import math
import gurobipy as gp
from gurobipy import GRB
import numpy as np
from tqdm import tqdm
import multiprocessing

class SudokuSolver:
    def __init__(self, dir_path):
        self.dir = dir_path
        self.grid = []

    def loadTxt(self):
        file = open(self.dir, 'r')
        self.grid = np.array([ list(line.strip()) for line in file])
        return self.grid

    def solve(self):
        grid = self.loadTxt()

        n = len(grid[0])
        s = int(math.sqrt(n))

        # Create our 3-D array of model variables
        model = gp.Model('sudoku')
        vars = model.addVars(n, n, n, vtype=GRB.BINARY, name='G')

        model.setParam('OutputFlag', 0)
        # Fix variables associated with cells whose values are pre-specified

        for i in range(n):
            for j in range(n):
                if grid[i][j] != '0':
                    v = int(grid[i][j]) - 1
                    vars[i, j, v].LB = 1

        # Each cell must take one value

        model.addConstrs((vars.sum(i, j, '*') == 1
                         for i in range(n)
                         for j in range(n)), name='V')

        # Each value appears once per row

        model.addConstrs((vars.sum(i, '*', v) == 1
                         for i in range(n)
                         for v in range(n)), name='R')

        # Each value appears once per column

        model.addConstrs((vars.sum('*', j, v) == 1
                         for j in range(n)
                         for v in range(n)), name='C')


        # Each value appears once per subgrid

        model.addConstrs((
            gp.quicksum(vars[i, j, v] for i in range(i0*s, (i0+1)*s)
                        for j in range(j0*s, (j0+1)*s)) == 1
            for v in range(n)
            for i0 in range(s)
            for j0 in range(s)), name='Sub')

        model.optimize()


        # Retrieve optimization result

        solution = model.getAttr('X', vars)

        solutionGrid = np.zeros((n, n))

        for i in range(n):
            sol = ''
            for j in range(n):
                for v in range(n):
                    if solution[i, j, v] > 0.5:
                        sol += str(v+1)
                        solutionGrid[i,j] = v+1
            print(sol)

        return solutionGrid

def dataParser(dir):
    if len(os.listdir(data_path + 'p096_sudoku')) != 0:
        print('Folder exists.')
        return 'All file dispatched.'

    agrregateData = open(dir, 'r')
    for line in agrregateData:
        if line.startswith('Grid'):
            data_container = []
            output_name = line.strip()
        else:
            data_container.append(line.strip())

        if len(data_container) == 9:
            with open(data_path + 'p096_sudoku/'+ output_name + '.txt', "w") as outfile:
                outfile.write("\n".join(data_container))
    return 'All file dispatched.'

def main(dir):
    solver = SudokuSolver(data_path + 'p096_sudoku/' + dir )
    res = solver.solve().ravel()
    three_digit = ''.join([str(int(res[i])) for i in range(3)])
    return int(three_digit)

if __name__ == '__main__':
    data_dir = data_path + 'p096_sudoku.txt'
    dataParser(data_dir)
    files = os.listdir(data_path + 'p096_sudoku')

    res = 0
    for file in tqdm(files):
        res += main(file)
    print('Final result',res)

    # with multiprocessing.Pool(processes=os.cpu_count()//2) as p:
    #     MAX_COUNT = len(files)
    #     res = tqdm(p.imap(main, files), total=MAX_COUNT)
    # print(sum(res))