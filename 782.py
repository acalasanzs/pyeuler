"""
Made with love by Albert Calasanz Sallen in Python 3
"""
import math
import numpy as np

# Example binary matrices
A = np.array([
    [1,0,1],
    [0,0,0],
    [1,0,1]])
B = np.array([
    [0,0,0],
    [0,0,0],
    [1,1,1]])

# Complexity binary matrix calculator
def complexity(matrix):
    n = len(matrix)                                     #matrix size, as a 0-cube (square)

    #calculates if there is a match for arrays inside an array
    def setin(array,arr):
        for a in array:
            if np.array_equal(a,arr):
                return True
        return False
    
    #returns de columns as an 2d array (such as a rerversed 2D matrix)
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
class c:                                                #Create and object which will be used for contain all the values and its matrix in itself
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.matrix = np.zeros((self.n,self.n))         #Initialize the void (n, n) matrix
        for _ in range(self.k):                         #Add as ones as are required
            self.addOne()
    def addOne(self):
        class point:                                    #Make an object which contains the point of a posible combination with its matrix complexity
            def __init__(self, x, y, complex):
                self.x = x
                self.y = y
                self.complex = complex
        temp = []                                       #Actual matrix to be changed
        mininum = []                                    #list of all points wich will be tried
        #Array indices
        x = 0
        y = 0
        while True:
            temp = np.copy(self.matrix)                 #Actual matrix to be changed copied from the original matrix
            if x == self.n:                             #If x exceeds the last index, reset x and increase y if it's not the last index of y
                x = 0
                if y < self.n - 1:
                    y += 1
                else:
                    break                               #Break when it exceeds the last point of the matrix
            if temp[x][y] == 0:
                temp[x][y] = 1
                current_complexity = len(complexity(temp))
                point1 = point(x, y, current_complexity)
                mininum.append(point1)
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
        bin = c(n,a)
        print(bin.get_complexity())
        sum += bin.get_complexity()
    return sum

print(C(2))

print( complexity( np.array([
    [1, 0],
    [1, 1]
])))