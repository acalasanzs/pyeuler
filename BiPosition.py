class BiPosition:
    def __init__(self, n, index = 0):
        self.n = n
        self.x = 0
        self.y = 0
        self._index = index if type(index) is int else 0
        self.current = self.__getitem__(self._index)
    def __iter__(self):
        return self
    def __getitem__(self, item):
        if item < 0:
            item = (self.n + self.n*self.n) - -(item + 1)
        def go_to(to_arrive):
            while to_arrive > 0:
                if self.x == self.n:                             #If x exceeds the last index, reset x and increase y if it's not the last index of y
                    self.x = 0
                    if self.y < self.n:
                        self.y += 1
                    else:
                        raise StopIteration
                self.x += 1
                to_arrive -= 1
        if item >= self._index:
            to_arrive = item - (self.x + self.y*self.n)
            go_to(to_arrive)
        else:
            while item < self._index:
                self.x -= 1
                item -= 1
                if self.y > 0:
                    self.y -= 1
                    self.x = 5
                else:
                    break
                
        self.current = [self.x, self.y]
        return self.current
    def __next__(self):
        to_arrive = self._index - (self.x + self.y*self.n)
        if to_arrive > 0:
            while to_arrive > 0:
                if self.x == self.n:                             #If x exceeds the last index, reset x and increase y if it's not the last index of y
                    self.x = 0
                    if self.y < self.n:
                        self.y += 1
                    else:
                        raise StopIteration
                else:
                    self.x += 1
                to_arrive -= 1
            
            self.current = [self.x, self.y]
            return self.current
        else:
            if self.x == self.n:                             #If x exceeds the last index, reset x and increase y if it's not the last index of y
                self.x = 0
                if self.y < self.n:
                    self.y += 1
                else:
                    raise StopIteration
            else:
                self.x += 1
            self.current = [self.x, self.y]
            return self.current 
class MatrixIterator:
    def __init__(self, n, k):
        self.n = n                                      #B-Matrix's size
        self.k = k                                      #B-Matrix's ones
        self.matrix = np.zeros((n, n))
        self.cpositions = [BiPosition(self.n, i) for i in range(self.k)]
        self._index = 0
        for i in self.cpositions:
            print(i[-1])
    def __next__(self):
        self._index += 1
        return self._index
    def __iter__(self):
        return self


#proof = MatrixIterator(5,3)
proof2 = BiPosition(5)
print(proof2.current)