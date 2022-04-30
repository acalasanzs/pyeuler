import numpy as np
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
            while next_occurence(0) != last._index:
                print(next_occurence(0),last._index) 
                next(last)
            self.matrix[x][y] = 2
            lx, ly = last.current

            self.matrix[lx][ly] = 1
            print(self.matrix)
        self._index += 1
        return self.matrix
    def __iter__(self):
        return self



#proof = MatrixIterator(5,3)
proof2 = BiPosition(5)

for i in proof2:
    print(i)