import numpy as np
import os
import networkx as nx
from os.path import dirname, join
project_root = dirname(dirname(__file__))
data_path = join(project_root, 'Data', '')

class MinimalNetwork:
    def __init__(self, dir_path):
        self.dir = dir_path
        self.adjMat = []

    def loadGraph(self):
        ''':return
        [['-' '16' '12' '21' '-' '-' '-']
        ['16' '-' '-' '17' '20' '-' '-']
        ['12' '-' '-' '28' '-' '31' '-']
        ['21' '17' '28' '-' '18' '19' '23']
        ['-' '20' '-' '18' '-' '-' '11']
        ['-' '-' '31' '19' '-' '-' '27']
        ['-' '-' '-' '23' '11' '27' '-']]
        '''
        file = open(self.dir, 'r')
        self.adjMat = np.array([line.strip().split(',') for line in file])
        file.close()
        self.adjMat = np.where(self.adjMat == '-', 0, self.adjMat).astype(float)
        return self.adjMat


    def MST(self):
        A = self.loadGraph()
        original_weight = A.sum()/2
        G = nx.from_numpy_array(A)

        # Order the edges of G in increasing (non-decreasing) order of their weights
        sorted_edges = sorted(G.edges(data=True), key = lambda x : x[2].get('weight',1))
        # and set T to be an empty graph.
        T = nx.Graph()
        # Add the first edge from the ordering to T.
        T.add_edges_from(sorted_edges[0:1])
        # Consider the next edge in the ordering. If it produces a cycle in T with already
        # included edges, skip it. Otherwise, include it in T
        # Repeat
        for edge in sorted_edges[1:]:
            H = T.copy()
            H.add_edges_from([edge])
            try:
                nx.find_cycle(H)
                pass
            except nx.exception.NetworkXNoCycle:
                T.add_edges_from([edge])
                pass

        MST_weight = 0
        for u,v, attr in T.edges(data=True):
            MST_weight += sum(attr.values())

        return original_weight - MST_weight


if __name__ == '__main__':
    data_dir = data_path + 'p107_network.txt'
    network = MinimalNetwork(data_dir)

    print(network.MST())

