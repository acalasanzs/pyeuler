import enum
from itertools import combinations
import math
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
        raise "not a ndarray"
class c:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.matrix = np.zeros((self.n,self.n))
        for _ in range(self.k):
            self.addOne()
    def addOne(self):
        class point:
            def __init__(self, x, y, complex):
                self.x = x
                self.y = y
                self.complex = complex
        temp = []
        temp = np.copy(self.matrix)
        mininum = []
        x = 0
        y = 0
        while True:
            temp = np.copy(self.matrix)
            if x == self.n:
                x = 0
                if y < self.n - 1:
                    y += 1
            if temp[x][y] == 0:
                temp[x][y] = 1
                current_complexity = len(complexity(temp))
                point1 = point(x, y, current_complexity)
                mininum.append(point1)
            if x == (self.n - 1) and y == (self.n - 1):
                break
            x += 1
        mini = [co.complex for co in mininum]
        minI = mini.index(min(mini))
        mininum = mininum[minI]
        self.matrix[mininum.x][mininum.y] = 1
    def get_complexity(self):
        return len(complexity(self.matrix))

def C(n):
    sum = 0
    for a in range(int(math.pow(n,2)+1)):
        print("-")
        sum += c(n,a).get_complexity()
    return sum

print(C(2))