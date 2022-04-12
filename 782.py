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
        self.matrix = np.zeros((self.n,self.n))
        for _ in range(self.k):
            self.addOne()
        print(self.matrix)
    def addOne(self):
        print("yey")
        temp = []
        temp = np.copy(self.matrix)
        for column in range(self.n):
            for row in range(self.n):
                if temp[column][row] == 0:
                    temp[column][row] = 1
                    current_complexity = len(complexity(temp))
                    if current_complexity > len(complexity(self.matrix)):
                        if row < self.n-1:
                            if temp[column][row+1] == 1:
                                self.matrix[column][row] = 1
                                temp = np.copy(self.matrix)
                                break
                            else:
                                if column == 0 and row == 0:
                                    self.matrix[column][row] = 1
                                    temp = np.copy(self.matrix)
                                    return
                            #   self.matrix[column][row] = 0
                        else:
                            self.matrix[column][row] = 1
                            temp = np.copy(self.matrix)
                            return
                        continue
                else:
                    self.matrix[column][row] = 1
                    temp = np.copy(self.matrix)
                    return

a = c(2,1)