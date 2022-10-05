"""
Made with love by Albert Calasanz Sallen in Python 3
This time I'm going hard.
"""
import os
import time
from turtle import pos
import numpy as np

class Recursive:
    @staticmethod
    def set_item(obj, indices, new):
        if not type(obj).__module__ == 'numpy':
            raise "Not a NumPy Array"
        
        index = 0
        last = obj
        while index < len(indices) - 1:
            last = last[indices[index]]
            index += 1
        last[indices[-1]] = new
    @staticmethod
    def get_item(obj, indices):
        if not type(obj).__module__ == 'numpy':
            raise "Not a NumPy Array"
        
        index = 0
        last = obj
        while index < len(indices):
            last = last[indices[index]]
            index += 1
        return last



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
#calculates if there is a match for arrays inside an array
def setin(array,arr):
    for a in array:
        if np.array_equal(a,arr) or np.array_equal(a[::-1],arr):
            return True
    return False
# Complexity binary matrix calculator
def complexity(matrix):
    n = len(matrix)                                     #matrix size, as a 0-cube (square)

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
class Map:
    def __init__(self, **variables):
        self.keys = np.array([x for x in range(len(variables.items()))], dtype=np.dtype('U50'))
        self.values = np.array([None for x in range(len(variables.items()))])
        self.index = -1
        i = 0
        for key, value in variables.items():
            self.keys[i] = key
            self.values[i] = value
            i += 1
    def append(self, **values):
        for key, value in values.items():
            self.values[np.where(self.keys == key)][0].append(value)
    def pop(self, **values):
        for key, index in values.items():
            self.values[np.where(self.keys == key)][0].pop(index)
    def __iter__(self):
        return self
    def __len__(self):
        return self.keys.size[0]
    def __next__(self):
        self.index += 1
        return self.__getitem__(self.index)
    def __getitem__(self, item):
        total = {}
        try:
            for i, key in enumerate(self.keys):
                total[key] = self.values[i][item]
            return total
        except IndexError:
            raise StopIteration
    def __setitem__(self, item, value):
        self.values[np.where(self.keys == item)][0] = value
    @property
    def data(self):
        for i, key in enumerate(self.keys):
            print(key, end="\n")
            print(", ".join(self.values[i][0]), end="\n\n")
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
    def go_to_d(self, d , to_arrive):
        if to_arrive > 0:
            self.go_to((self.n**d)*(to_arrive + 1))
            return self.go_to(-1)
        else:
            return self.go_to(-(self.n**d)*abs(to_arrive))
        
    def __next__(self):
        if not self.start:
            self.start = True
            return self.current
        else:
            return self.go_to(1)

#returns the chess value of a n-matrix
def chess_position(position, n):
    paridad = n % 2 == 0
    condition = (DimensionalPosition.convert_base(position, n) + 2) % 2 == 0
    if paridad:
        return condition
    else:
        return not condition

# For 0 <= k <= n^2, let c(n,k) be the minimum complexity of an n * n matrix with eactly k ones.
def minimum(n, k):
    void = np.zeros([n, n])
    matrix_position = DimensionalPosition(2, n, 0)
    matrix_max = DimensionalPosition(2, n, n * n - 1)
    one_position = []

    density_pos = DimensionalPosition(2, n)
    density_ones = []
    density = 0
    for x in density_pos:
        if(chess_position(x, n)):
            density_ones.append(x)
            density += 1
    density /= n*n
    def update():
        for pos in one_position:
            Recursive.set_item(void, pos, 1)
        return complexity(void)

    count = 0

    complexity_points = Map(complexity = [], position = [])
    def show():
        for i, value in enumerate(complexity_points.values[0]):
            print(complexity_points.keys[1]+":")
            print(complexity_points.values[1][i], end="\n-")

            print(complexity_points.keys[0] + ": " + str(len(value)), end="\n")
            for c in value:
                print("-".join([str(int(x)) for x in c]), end=" | ")
            print("\n\n")
                
    one_position.append(density_ones[0])
    while count < k:
        for one in density_ones:
            one_position.append(one)
            complexity_points.append(complexity = update(), position = one)
            one_position.pop()
        else:
            min_complexity = complexity_points[0]
            min_index = 0
            def loop(min_complexity, min_index):
                for i, point in enumerate(complexity_points):
                    complexity_value = len(point['complexity'])
                    if complexity_value < len(min_complexity['complexity']) and not setin(one_position, point['position']):
                        min_complexity = point
                    elif i == len(complexity_points) - 1:
                        min_index += 1
                        min_complexity = complexity_points[min_index]
                        loop()
                else:
                    print(min_complexity["position"])
                    last = min_complexity['position']
                    i = 0
                    while setin(one_position, min_complexity['position']):
                        try:
                            min_complexity = complexity_points[i]
                            i += 1
                        except StopIteration:
                            break
            loop(min_complexity, min_index)
            one_position.append(min_complexity['position'])
        count += 1
    void = np.zeros([n, n])
    update()
    # time.sleep(.2)
    # os.system("cls")
    # print(np.flipud(void))
    return np.flipud(void)


def C(N):
    temp = 0
    for x in range(N**2 + 1):
        # print((N, x), "\n", minimum(N, x), "\n", complexity(minimum(N, x)), "\n\n")
        temp += len(complexity(minimum(N, x)))
    return temp

# print(C(5))
print(minimum(5,12))
print(
    complexity(
        np.array(
            [
                [0,0,0,1,0,0],
                [0,0,0,1,0,0],
                [0,0,0,1,1,1],                              # 12 unos
                [1,1,1,0,0,0],
                [0,0,0,0,0,0],
                [1,1,1,0,0,0],
            ]
        )
    )
)
print(
    complexity(
        np.array(
            [
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],                              # 12 unos
                [0,0,0,0,0,0],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1],
            ]
        )
    )
)