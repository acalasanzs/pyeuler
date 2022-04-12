import enum
from itertools import combinations
import numpy as np
A = np.array([
    [1,0,1],
    [0,0,0],
    [1,0,1]])
B = np.array([
    [0,0,0],
    [0,0,0],
    [1,1,1]])
def complexity(matrix):
    nx = len(matrix[0])
    ny = len(matrix)
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
                if not(tuplein(combinations,tuple(nr))):
                   combinations.append(nr)
            for nc in columns(matrix):
                if not(tuplein(combinations,tuple(nc))):
                    combinations.append(nc)
            return combinations
        else:
            return None
    else:
        raise "not ndarray"
class c:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.matrix = np.zeros(self.n,self.n)
        for one in range(self.k):
            self.addOne()
    def addOne(self):
        temp = []
        begin = False
        for column in self.n:
            for row in self.n:
                if not begin:
                    temp = np.copy(self.matrix)
                    temp[column][row] == 1
                    self.matrix[column][row] == 1
                    begin = True
                else:
                    temp[column][row] == 1
                    if complexity(temp) > complexity(self.matrix)