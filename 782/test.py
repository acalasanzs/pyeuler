""" import itertools

perm = itertools.permutations(range(5444532),452) """


class sequence:
        def __init__(self, *values):
            self.current = "0"
            self.push(*values)
        def __getitem__(self, item):
            current = self
            for idx in item:
                current = getattr(current, str(idx))
                if not isinstance(current, sequence):
                    return current
        def push(self, *values):
            for value in values:
                setattr(self, self.current, value)
                self.current = str(int(self.current) + 1)
        @property
        def len(self):
            temp = 0
            for prop in dir(self):
                if not prop.startswith("_"):
                    temp += 1
            return temp