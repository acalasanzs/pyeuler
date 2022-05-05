import itertools
import math
from time import sleep
def posible_sums(num):
        posibilities = []
        divisor = 1
        while divisor < num:
            current = num / divisor
            while not current.is_integer():
                divisor +=1
                current = num / divisor
            divisor += 1
            if current == 1:
                break
            posibilities.append(int(current))
        return posibilities
print(posible_sums(120))

def to_exponent(base, exp):
    result = 1
    results = []
    
    for x in range(2, exp+1):
        results.append((x, pow(base, x)))
