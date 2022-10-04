""" import itertools

perm = itertools.permutations(range(5444532),452) """


import operator


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
            items = [x for x in (item if not type(item) == int else [item])]
            for i,idx in enumerate(items):
                current = getattr(current, str(idx))
                if isinstance(current, Recursive.sequence) and i < (len(items) - 1):
                    continue
                return current
        def push(self, *values):
            for value in values:
                setattr(self, self.current, value)
                self.increase()
        def toArray(self):
            temp = []
            for x in range(self.len):
                temp.append(self[str(x)])
            return temp
        def toArrayRecursively(self):
            arr = self.toArray()
            index = 0
            current_position = [index]
            last = self
            while True:
                try:
                    last = last[current_position]
                    arr[index] = last.toArray()
                    index += 1
                    current_position.append(0)
                except:
                    if index == len(arr) - 1:
                        break
                    index += 1
                    current_position = [index]
                
            return arr
                
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
        return temp.toArrayRecursively()
