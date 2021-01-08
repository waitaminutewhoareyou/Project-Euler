import gurobipy as gp
from gurobipy import GRB
import numpy as np

def game(n, T):
    # Construct state space
    states_i = list(range(n+1))
    states_j = [0]

    while True:
        new_state = states_j[-1] + 2**(T-1)
        states_j.append(new_state)
        if new_state >= n:
            break

    num_i = len(states_i)
    num_j = len(states_j)

    model = gp.Model('prod')
    states = model.addVars(num_i, num_j, ub=1, vtype= GRB.CONTINUOUS)
    # Define absorption states
    model.addConstrs(
        (states[num_i-1, j] == 0) for j in range(num_j)
                    )

    # Define terminal states
    model.addConstrs(
        (states[i, num_j-1] == 1) for i in range(num_i-1)
    )

    # Define transition states
    model.addConstrs(
        (states[i, j] ==
            1/2 * (1-1/2**T)*states[i,j]
            + 1/2 * (1-1/2**T)*states[i+1, j]
            + 1/2 * (1/2**T)*states[i, j+1]
            + 1/2 * (1/2**T)*states[i+1, j+1])
        for i in range(num_i-2) for j in range(num_j-1)
    )


    # Define penultimate states for player 1 because player 1 has first hand advantages
    model.addConstrs(
        (states[num_i-2, j] ==
         1/2 * 0
         + 1/2*(1/2**T)*states[num_i-2, j+1]
         + 1/2*(1-1/2**T)*states[num_i-2, j])
        for j in range(num_j-1)
    )


    model.optimize()
    sol = np.zeros(shape=(num_i, num_j))
    for i in range(num_i):
        for j in range(num_j):
            sol[i,j] = states[i,j].x

    print(sol)
    return states[0,0].x


if __name__ == '__main__':
    n = 50
    T = 4 # maximum 7
    print(game(n, T))