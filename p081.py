# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:58:08 2020

@author: JI YIHONG
"""
import numpy as np

file = "C:\\Users\\JI YIHONG\\Dropbox\\mathematica\\Project Euler\\p081_matrix.txt"
def minimal_path(file,i,j):
    content= []
    with open(file) as f:
        for line in f:
            content.append(line.strip().split(","))
            
    matrix = np.array(content).astype(int)
    
    table= np.zeros_like(matrix)

    row_num, col_num = table.shape
    for i in range(row_num):
        for j in range(row_num):
            if i==j==0:
                table[i,j]=matrix[i,j]
            elif i==0 and j!=0:
                table[i,j] = table[i,j-1]+ matrix[i,j]
            elif i!=0 and j==0:
                table[i,j] = table[i-1,j] + matrix[i,j]
            else:
                table[i,j] = min(table[i-1,j], table[i,j-1]) + matrix[i,j]
    return table[i,j]
print(minimal_path(file,79,79))