import gurobipy as gp
from gurobipy import GRB
import sys
class EfficientExponentiation:
    def __init__(self, target):
        self.target = target

    def solve(self):
        n = self.target
        val = range(1, n+1)

        model = gp.Model('EfficientExponentiation')
        vars = model.addVars(n, n, vtype=GRB.BINARY, obj=1, name='decision variable')

        model.addConstr(vars[0, 0] == 1)
        # Each step we can use at most one edge
        model.addConstrs(
            (vars.sum('*', j) <= 1 for j in range(n)), name='V'
        )

        # The target must be met exactly
        model.addConstr(gp.quicksum(val[i] * vars[i, j] for i in range(n) for j in range(n)) == n-1)

        # Each step can only select used edge
        model.addConstrs(
            ( gp.quicksum(vars[i, k] for k in range(j)) >= vars[i, j] + 1 for i in range(n) for j in range(n))
        )

        model.modelSense = GRB.MINIMIZE
        model.optimize()
        status = model.status
        if status == GRB.UNBOUNDED:
            print('The model cannot be solved because it is unbounded')
            sys.exit(0)
        if status == GRB.OPTIMAL:
            print('The optimal objective is %g' % model.objVal)
            sys.exit(0)
        if status != GRB.INF_OR_UNBD and status != GRB.INFEASIBLE:
            print('Optimization was stopped with status %d' % status)
            sys.exit(0)
        return model.objVal
    
if __name__ == '__main__':
    solver = EfficientExponentiation(15)
    print(solver.solve())