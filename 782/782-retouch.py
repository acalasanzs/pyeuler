"""
Made with love by Albert Calasanz Sallen in Python 3
This time I'm going hard.
"""
import os
import time
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


# For 0 <= k <= n^2, let c(n,k) be the minimum complexity of an n * n matrix with eactly k ones.
def minimum(n, k):
    void = np.zeros([n, n])
    matrix_position = DimensionalPosition(2, n, 0)
    matrix_max = DimensionalPosition(2, n, n * n - 1)
    one_position = []

    relative_half = int(n/2)
    count = k

    actual = n - relative_half
    cactual = 1
    changed = False
    done = False
    my_turn_up = False
    dangerous_range = [[x, (n - 1) - x] for x in range(0, relative_half - 1)]
    print(dangerous_range)
    while count > 0:
        if count == k:
            one_position.append(matrix_max.current)
        else:
            if count % 2 == 0 and count <= relative_half:
                matrix_max.go_to_d(1, -1)
                if not setin(dangerous_range, matrix_max.current):                          
                    one_position.append(matrix_max.current)
            else:
                if matrix_position.current[1] < (n - relative_half) and matrix_position.current[0] <= (n - relative_half) and not changed :
                    one_position.append(next(matrix_position))
                else:
                    if matrix_position.current[0] >= relative_half:
                        changed = True
                        condition = (my_turn_up) if not done else True
                        if condition:
                            matrix_position.current = [actual, n - cactual]
                            one_position.append(matrix_position.go_to(-1))
                            actual += 1
                            if actual > (n - relative_half + 1):
                                my_turn_up = not my_turn_up
                                actual = n - relative_half
                                cactual += 1
                                if cactual > n:
                                    changed = False
                        else:
                            one_position.append(matrix_max.go_to_d(1, -1))
                            if matrix_max.current[0] == 0 + 1:
                                my_turn_up = not my_turn_up
                                done = True
                    else:
                        matrix_position.go_to_d(1,0)
                        one_position.append(matrix_position.go_to(relative_half))
        count -= 1
    for pos in one_position:
        Recursive.set_item(void, pos, 1)
    # time.sleep(.2)
    # os.system("cls")
    # print(np.flipud(void))
    return np.flipud(void)


def C(N):
    temp = 0
    for x in range(0, N**2 + 1):
        print((N, x), "\n", minimum(N, x), "\n", complexity(minimum(N, x)), "\n\n")
        temp += len(complexity(minimum(N, x)))
    return temp

print(C(6))
print(
    complexity(
        np.array(
            [
                [0,0,0,1,1,1],                              # 12 unos
                [0,0,0,1,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,0],
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