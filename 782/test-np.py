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

""" arr = np.eye(3,3)
Recursive.set_item(arr,[1,1],3)
print(arr)
print(Recursive.get_item(arr, [1,1])) """

print(Recursive.array(2,4))