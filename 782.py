import enum
from itertools import combinations
import numpy as np
A = np.array([
    [1,0,1],
    [0,1,0],
    [1,1,1]])
B = np.array([
    [0,0,0],
    [0,0,0],
    [1,1,1]])
def complexity(matrix, nx=3, ny=3):
    def tuplein(array,tup):
        def isall(a,b):
            for i,j in enumerate(a):
                if not(j == b[i]):
                    return False
            return True
        for i in array:
            if isall(i,tup):
                return True
        return False
    def columns(array):
        t = [[] for _ in array[0]]
        for column,i in enumerate(array[0]):
            for row in range(len(array)):
                t[column].append(array[row][column])
        return t
    if type(matrix) is np.ndarray:
        combinations = []
        if matrix.shape == (nx,ny):
            for nr in matrix:
                if not(tuplein(matrix,tuple(nr))):
                   combinations.append(nr)
            for nc in columns(matrix):
                print(nc)
                if not(tuplein(matrix,tuple(nc))):
                    combinations.append(nc)
            return len(combinations)
        else:
            return None
    else:
        raise "not ndarray"
print(complexity(A))