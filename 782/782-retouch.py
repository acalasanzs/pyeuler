"""
Made with love by Albert Calasanz Sallen in Python 3
This time I'm going hard.
"""
from heapq import nsmallest
import itertools
import math
from multiprocessing.dummy import Array
from turtle import goto
import numpy as np

class Recursive:
    class sequence:
        def __init__(self, *values):
            self.current = "0"
            self.len = 0
            if len([*values]) == 0:
                return
            elif len([*values]) == 1:
                for x in range(values[0]):
                    setattr(self, self.current, Recursive.sequence())
                    self.increase()
            else:
                self.push(*values)
        def increase(self):
            self.len = int(self.current) + 1
            self.current = str(self.len)
        def __setitem__(self, key, value):
            setattr(self, str(key), value)
        def __getitem__(self, item):
            current = self
            for idx in [x for x in (item if not type(item) == int else [item])]:
                current = getattr(current, str(idx))
                if not isinstance(current, Recursive.sequence):
                    return current
        def push(self, *values):
            for value in values:
                setattr(self, self.current, value)
                self.increase()
    @staticmethod
    def array(n,n2):
        temp = Recursive.sequence(n)
        for i in range(temp.len):
            count = (n2 | n) - 2
            temp[i] = Recursive.sequence()
            last = temp[i]
            while count > 0:
                count -= 1
                last[0] = Recursive.sequence()
                last = last[0]
        return temp
print(Recursive.array(2,4))
# Example binary matrices
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

print(complexity(example["B"]))
print(Recursive.array(4,2))