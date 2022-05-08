import itertools
import math
from time import sleep
def posible_sums(num):
        posibilities = []
        divisor = 1
        while divisor < num:
            current = num / divisor
            while not current.is_integer():
                divisor += 1
                current = num / divisor
            divisor += 1
            posibilities.append(int(current))
        return posibilities

def to_exponent(base, exp):
    result = 1
    results = []
    current = 1
    while True:
        rest = exp
    return results
# print(to_exponent(2,12))
print(posible_sums(12))
