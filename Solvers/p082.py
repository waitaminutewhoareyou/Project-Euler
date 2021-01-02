# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 18:00:09 2020

@author: JI YIHONG
"""

import numpy as np

file = "C:\\Users\\JI YIHONG\\Dropbox\\mathematica\\Project Euler\\trial.txt"
def minimal_path(file):
    content= []
    with open(file) as f:
        for line in f:
            content.append(line.strip().split(","))
            
    matrix = np.array(content).astype(int)
    
    table= np.zeros_like(matrix)
    table[:,0] = matrix[:,0]
    row_num, col_num = matrix.shape
    
    for j in range(col_num):
        for i in range(1,row_num):
            if j==0:
                table[:,j]=matrix[:,j]
                
    return table
print(minimal_path(file))