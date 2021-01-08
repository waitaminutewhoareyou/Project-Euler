import gurobipy as gp
from gurobipy import  GRB


def expectedRoundS(n):
    def ix(k):
        if k < 0:
            return -k
        elif 0 <= k <= n//2:
            return k
        else:
            return n - k

    model = gp.Model('p683')

    mu = model.addVars(n//2+1, ub=1, vtype=GRB.CONTINUOUS)

    model.addConstr(mu[0] == 0, name='boundary')
    model.addConstrs(
        (mu[ix(i)] ==
         1 + 1/2*mu[ix(i)] +
         2/9*mu[ix(i-1)] +
         2/9*mu[ix(i+1)] +
         1/36*mu[ix(i-2)] +
         1/36*mu[ix(i+2)]) for i in range(1, n//2+1))
    for i in range(1, n//2+1):
        print(f'mu{[ix(i)]} == 1 + 1/2*mu{[ix(i)]} + 2/9*mu{[ix(i-1)]} + 2/9*mu{[ix(i+1)]} +1/36*mu{[ix(i-2)]} +1/36*mu{[ix(i+2)]}')
    model.optimize()
    print(model.STATUS)
    
    sol = []
    for vars in model.getVars():
        sol.append(vars.x)
    return sol


if __name__ == '__main__':
    print(expectedRoundS(100))