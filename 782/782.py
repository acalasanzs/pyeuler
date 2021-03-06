"""
Made with love by Albert Calasanz Sallen in Python 3
I did it like if had being trying hard all at the same time i wasn't
"""
import itertools
import math
import numpy as np

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
class BiPosition:
    def __init__(self, n, index = 0):
        self.n = n
        self.x = 0
        self.y = 0
        self.start = False
        self._index = index if type(index) is int else 0
        if index > 0: self.go_to(index)
        self.current = self.__getitem__(self._index)
    def __iter__(self):
        return self
    def __getitem__(self, item):
        if item < 0:
            item = (self.n + self.n*self.n) - -(item + 1)
        if item >= self._index:
            to_arrive = item - (self.x + self.y*self.n)
            self.go_to(to_arrive)
        else:
            while item < self._index:
                self.x -= 1
                self._index -= 1
                if self.y > 0:
                    self.y -= 1
                    self.x = 5
                elif self.y == 0 and self.x == 0:
                    break
                
        self.current = [self.x, self.y]
        return self.current
    def go_to(self, to_arrive):
        while to_arrive > 0:
            if self.x == self.n:                             #If x exceeds the last index, reset x and increase y if it's not the last index of y
                self.x = 0
                if self.y < self.n:
                    self.y += 1
                else:
                    raise StopIteration
            self.x += 1
            self._index += 1
            to_arrive -= 1
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
class MatrixIterator:
    def __init__(self, n, k):
        self.n = n                                      #B-Matrix's size
        self.k = k                                      #B-Matrix's ones
        self.matrix = np.zeros((self.n, self.n))         #Void (n, n) matrix
        self.cpositions = [BiPosition(self.n - 1, i) for i in range(self.k)]
        self._current_position = 0
        self._index = 0
    def __next__(self):
        def update():
            for idx in range(len(self.cpositions)):
                x, y = self.cpositions[idx].current
                self.matrix[x][y] = 1
        def next_occurence(o):
            x = 0
            y = 0
            counter = 0
            while True:
                if x == self.n:                             #If x exceeds the last index, reset x and increase y if it's not the last index of y
                    x = 0
                    if y < self.n - 1:
                        y += 1
                    else:
                        break 
                #The code
                if self.matrix[x][y] == o:
                    return counter
                counter += 1
                x += 1
        if self._index == 0:
            update()
        else:
            last = self.cpositions[self._current_position]
            x, y = last.current
            while next_occurence(0) == last._index:
                print(next_occurence(0),last._index) 
                next(last)
            self.matrix[x][y] = 2
            lx, ly = last.current

            self.matrix[lx][ly] = 1
        self._index += 1
        return self.matrix
    def __iter__(self):
        return self


proof = MatrixIterator(5,3)
proof_counter = 0
for i in proof:
    print("_____________")
    if proof_counter > 20:
        break
    proof_counter += 1
class c:                                                #Create and object which will be used for contain all the values and its matrix in itself
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.matrix = np.zeros((self.n,self.n))         #Initialize the void (n, n) matrix
        self.draw()
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
    def draw(self):
        cx = [0 for _ in range(self.k)]
        cy = [0 for _ in range(self.k)]
        mininum = []
        class matrix:
            def __init__(self, matrix):
                self.matrix = matrix
                self.complexity = len(complexity(matrix))
        # Get Positions
        posible_permutations = itertools.permutations(range(self.n), 2)         #All permutations without repeated numbers
        r_tuples = []
        for i in range(self.n):
            r_tuples.append(tuple([i for _ in range(2)]))
        posible_permutations = itertools.chain(r_tuples,posible_permutations)
        #Update positions
        def updatePositions():
            self.matrix = np.zeros((self.n,self.n))         #Void (n, n) matrix
            for idx in range(len(cx)):
                self.matrix[cx[idx]][cy[idx]] = 1
        
        def updateCxCy(permutation):
            idx = 0
            for position in permutation:
                cx[idx] = position[0]
                cy[idx] = position[1]
                idx +=1
        def void_finder():
            voids = []
            x = 0
            y = 0
            while True:
                if x == self.n:                             #If x exceeds the last index, reset x and increase y if it's not the last index of y
                    x = 0
                    if y < self.n - 1:
                        y += 1
                    else:
                        break 
                #The code
                if self.matrix[x][y] == 0:
                    voids.append([x,y])
                x += 1
            return voids
        def change_position():
            x = 0
            y = 0
            for _ in range(self.k):
                self.addOne()
                print(self.matrix,len(complexity(self.matrix)))
            while True:
                if x == self.n:
                    x = 0
                    if y < self.n - 1:
                        y += 1
                    else:
                        break 
                x += 1
        change_position()
            

""" def C(n):
    sum = 0
    for a in range(int(math.pow(n,2)+1)):
        print(a, int(math.pow(n,2)+1))
        bin_m = c(n,a)
        sum += bin_m.complexity
    return sum

print(C(5)) """
# a = c(5,3)

"""
print( complexity( np.array([
    [1, 0],
    [1, 1]
])))
"""