"""
Made with love by Albert Calasanz Sallen in Python 3
This time I'm going hard.
"""
from email.mime import base
from time import struct_time
import numpy as np

example = {
    "A" : np.array([
        [1,0,1],
        [0,0,0],
        [1,0,1]]),
    "B" : np.array([
        [0,0,0],
        [0,0,0],
        [1,1,1]])
}
#returns the columns as an 2d array (such as a rerversed 2D matrix)
def columns(array):
    t = [[] for _ in array[0]]                      #Prepares a void 2d array
    for column,i in enumerate(array[0]):            #For each column index
        for row in range(len(array)):               #For each row
            t[column].append(array[row][column])    #Append to current value to the current column index
    return t

# Complexity binary matrix calculator
def complexity(matrix):
    n = len(matrix)                                     #matrix size, as a 0-cube (square)

    #calculates if there is a match for arrays inside an array
    def setin(array,arr):
        for a in array:
            if np.array_equal(a,arr):
                return True
        return False

    #Here comes the work
    if type(matrix) is np.ndarray:                      #check if It's a 2d np matrix
        combinations = []                               #Save a void combinations array
        if matrix.shape == (n, n):                      #check if is a square matrix
            for nr in matrix:                           #For each row
                if not(setin(combinations,nr)):         #If not a combination match in combiantions array for the current found combination
                   combinations.append(nr)              #Add combination to the list
            for nc in columns(matrix):                  #For each column
                if not(setin(combinations,nc)):         #If not a combination match in combiantions array for the current found combination
                    combinations.append(nc)             #Add combination to the list
            return combinations                         #When ends return the result
        else:
            raise "not a ndarray"
    else:
        raise "not a ndarray"

# print(complexity(example["A"]))

class DimensionalPosition:
    def __init__(self, d, n, index = 0):
        self.d = d                                                      #Dimension which defines the length of the index array
        self.n = n                                                      #Number base
        self.pos = [0 for x in range(d)]
        self.start = False
        self._index = index if type(index) is int else 0
        self.current = self.__getitem__(self._index)
    def __iter__(self):
        return self
    def __getitem__(self, item):
        result = DimensionalPosition.convert_base(item, self.n)
        while len(result) < self.d:
            result.append(0)
        if len(result) > self.d:
            raise IndexError
        else:
            return result[::-1]
    @staticmethod
    def convert_base(num, base):
        if type(num) is int:
            last = num
            result = []
            while True:
                calc = int(last / base)
                result.append(last%base)
                last = calc
                if calc == 0:
                    break
            return result
        elif type(num) is list:
            temp = 0
            for i, x in enumerate(num[::-1]):
                temp += x * (base ** i)
            return temp
    def go_to(self, to_arrive):
        if self.n < 10:
            current = int("".join([str(x) for x in self.current]), base = self.n)
            end = DimensionalPosition.convert_base(to_arrive + current, self.n)
        else:
            current = current
            if to_arrive < 0:
                end = DimensionalPosition.convert_base(DimensionalPosition.convert_base(current, self.n) + to_arrive, self.n)
            else:
                #Convert from base >10 to base 10, sum, and then convert to base >10 again
                end = DimensionalPosition.convert_base(
                    DimensionalPosition.convert_base(current, self.n) + to_arrive,
                    self.n
                )
        if len(end) > self.d:
            raise StopIteration
        while len(end) < self.d:
            end.append(0)
        self.current = end[::-1]
        return self.current
    def __next__(self):
        if not self.start:
            self.start = True
            return self.current
        else:
            return self.go_to(1)


# For 0 <= k <= n^2, let c(n,k) be the minimum complexity of an n * n matrix with eactly k ones.
def minimum(n, k):
    # TODO:
    # 
    void = np.empty([n, n])
    matrix_position = DimensionalPosition(2, n)
    matrix_max = DimensionalPosition(2, n, n * n - 1)
    one_position = []
    for x in matrix_position:
        print(x)
    for one in range(k):
        one_position.append(matrix_max.go_to(-1))
    print(one_position)
minimum(5,3)