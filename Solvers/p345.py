from os.path import  dirname, join
PROJECT_ROOT = dirname(dirname(__file__))
data_path = join(PROJECT_ROOT, 'Data', '')
import numpy as np
import gurobipy as gp
from gurobipy import GRB


class MatrixSum:
    def __init__(self, dir_path):
        """

        :type dir_path: string
        """
        f = open(dir_path, 'r')
        self.mat = []
        for line in f:
            self.mat.append(line.strip().split())
        f.close()
        self.mat = np.array(self.mat).astype(np.float)


    def solve(self):
        m,n = self.mat.shape

        model = gp.Model('MatrixSum')
        vars = model.addVars(m, n, vtype=GRB.BINARY,name='vars')
        total_sum = gp.quicksum(self.mat[i, j] * vars[i, j] for i in range(m) for j in range(n))
        model.setObjective(total_sum, GRB.MAXIMIZE)
        model.addConstrs(
            (gp.quicksum(vars[i, j] for j in range(n)) <= 1 for i in range(m))
             )

        model.addConstrs(
            (gp.quicksum(vars[i, j] for i in range(m)) <= 1 for j in range(n))
             )
        model.optimize()

        return model.getObjective().getValue()


if __name__ == '__main__':
    solver = MatrixSum(data_path + 'p345.txt')
    print('best obj is', solver.solve())