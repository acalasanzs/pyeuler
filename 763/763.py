""" 
IMPORTS FROM 782 with some improvements
"""
from pydoc import locate
import numpy as np

class Map:
    def __init__(self, name, **variables):
        self.name = str(name)
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
        return self.__getitem__(len(self) - 1)
    def add(self, instance):
        if instance.__name__ == self.name:
            for key, value in vars(instance).items():
                if not key.startswith("__"):
                    self.values[np.where(self.keys == key)][0].append(value)
        else:
            raise f"{type(instance)} is not an instance of {self.name}"
    def pop(self, **values):
        for key, index in values.items():
            self.values[np.where(self.keys == key)][0].pop(index)
    def __iter__(self):
        return self
    def __len__(self):
        return len(self.values[0])
    def __next__(self):
        self.index += 1
        return self.__getitem__(self.index)
    def __getitem__(self, item):
        total = {}
        try:
            for i, key in enumerate(self.keys):
                total[key] = self.values[i][item]
            total = type(
                self.name,
                (),
                total
            )
            return total
        except IndexError:
            raise StopIteration
    def __setitem__(self, item, value):
        self.values[np.where(self.keys == item)][0] = value
    @property
    def data(self):
        if len(self) == 0:
            return None
        for i, key in enumerate(self.keys):
            print(key, end="\n")
            print(", ".join([str(x) for x in self.values[i][0]]), end="\n\n")
    def show(self):
        for i, value in enumerate(self.values[0]):
            print(self.keys[1]+":")
            print(self.values[1][i], end="\n-")

            print(self.keys[0] + ": " + str(len(value)), end="\n")
            for c in value:
                print("-".join([str(int(x)) for x in c]), end=" | ")
            print("\n\n")
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


""" 
Made with love by Albert Calasanz Sallen
"""
class Space:
    def __init__(self, space_map):
        self.map = space_map if isinstance(space_map, Map) else Map("Amoeba", amoeba = [], position = [])
        self.count = 0
        pass
    def add(self, amoeba):
        self.count += 1
        try:
            if not isinstance(amoeba, Space.Amoeba):
                amoeba = self.map.append(amoeba = self.count, position = list(amoeba))
            else:
                self.map.add(amoeba)
        except:
            self.count -= 1
            raise "Something wrong happened on adding a new Amoeba"

map = Map("Amoeba", amoeba = [0], position = [[0,0,0]])
map.add(map[0])
map.show()