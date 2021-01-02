# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 2021

@author: JI YIHONG
"""
import networkx as nx
import bellmanford as bf
import numpy as np
from os.path import dirname, join
project_root = dirname(dirname(__file__))
data_path = join(project_root, 'Data', '')
data_dir = data_path + 'p082_matrix.txt'



def readDataAsArray(file):
    content = []
    with open(file,'r') as f:
        for line in f:
            content.append(line.strip().split(","))
            
    matrix = np.array(content).astype(int)
    return matrix


class ShortestPath:
    def __init__(self, distArray):
        self.distArray = distArray

    def createGraph(self):

        nrows, ncols = self.distArray.shape

        G = nx.DiGraph()
        # Add nodes
        G.add_node(0)  # source node
        for row_ix in range(nrows):
            for col_ix in range(ncols):
                G.add_node((row_ix, col_ix))
        G.add_node(1)  # sink node

        # Add edges

        for row_ix in range(nrows):
            G.add_edge(0, (row_ix, 0), length=self.distArray[row_ix, 0])

            for col_ix in range(ncols):
                # up
                G.add_edge((row_ix, col_ix), (max(row_ix-1, 0), col_ix),
                           length=self.distArray[max(row_ix-1, 0), col_ix])

                # down
                G.add_edge((row_ix, col_ix), (min(row_ix + 1, nrows - 1), col_ix),
                           length=self.distArray[min(row_ix + 1, nrows - 1), col_ix])

                # right
                G.add_edge((row_ix, col_ix), (row_ix, min(col_ix+1, ncols-1)),
                           length=self.distArray[row_ix, min(col_ix+1, ncols-1)])

            G.add_edge((row_ix, ncols-1), 1, length=0)

        return G

    def solve(self):
        graph = self.createGraph()
        path_length, path_nodes, negative_cycle = bf.bellman_ford(graph, source=0, target=1, weight="length")
        print("Is there a negative cycle? {0}".format(negative_cycle))
        print("Shortest path length: {0}".format(path_length))
        print("Shortest path: {0}".format(path_nodes))
        return path_length


if __name__ == '__main__':
    data = readDataAsArray(data_dir)
    solver = ShortestPath(data)
    print(solver.solve())