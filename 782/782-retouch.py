"""
Made with love by Albert Calasanz Sallen in Python 3
This time I'm going hard.
"""
from email.mime import base
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
# Complexity binary matrix calculator
def complexity(matrix):
    n = len(matrix)                                     #matrix size, as a 0-cube (square)

    #calculates if there is a match for arrays inside an array
    def setin(array,arr):
        for a in array:
            if np.array_equal(a,arr):
                return True
        return False
    
    #returns the columns as an 2d array (such as a rerversed 2D matrix)
    def columns(array):
        t = [[] for _ in array[0]]                      #Prepares a void 2d array
        for column,i in enumerate(array[0]):            #For each column index
            for row in range(len(array)):               #For each row
                t[column].append(array[row][column])    #Append to current value to the current column index
        return t

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
        self.d = d
        self.n = n
        self.pos = [0 for x in range(d)]
        self.start = False
        self._index = index if type(index) is int else 0
        #if index > 0: self.go_to(index)
        self.current = self.__getitem__(self._index)
    def __iter__(self):
        return self
    def __getitem__(self, item):
        result = self.convert_base(item, self.n)
        while len(result) < self.d:
            result.append(0)
        if len(result) > self.d:
            raise IndexError
        else:
            return result[::-1]
    def convert_base(self, num, base):
            last = num
            result = []
            while True:
                calc = int(last / base)
                result.append(last%base)
                last = calc
                if calc == 0:
                    break
            return result
    def go_to(self, to_arrive):
        current = int("".join([str(x) for x in self.current]), base = self.n)
        if to_arrive < 0:
            to_arrive = (self.n ** self.d) - to_arrive
        end = int("".join([str(x) for x in self.convert_base(to_arrive, self.n)[::-1]]), base=self.n) + current
        end = [int(x, base=self.n) for x in str(end)][::-1]
        while len(end) < self.d:
            end.append(0)
        return end[::-1]
    def __next__(self):
        if not self.start:
            self.start = True
            return self.current
        if self.x == self.n:                             #If x exceeds the last index, reset x and increase y if it's not the last index of y
            self.x = 0
            if self.y < self.n:
                self.y += 1
            else:
                raise StopIteration
        else:
            self.x += 1
        self._index += 1
        self.current = [self.x, self.y]
        return self.current


# For 0 <= k <= n^2, let c(n,k) be the minimum complexity of an n * n matrix with eactly k ones.
#def minimum(n, k):
    # TODO:
    # 

pos = DimensionalPosition(5,5)
pos.go_to(-5)
print(pos.current)