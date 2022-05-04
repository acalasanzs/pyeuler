import itertools
import math
from time import sleep

class prime:
    def __init__(self, current = None):
        self.current = current
    def __iter__(self):
        return self
    def __next__(self):
        def is_prime():
            if self.current == 1:
                return False
            x = self.current-1
            while x > 1:
                if self.current % x == 0:
                    return False
                x -= 1
            return True
        if self.current is None:
            self.current = 1
        else:
            self.current += 1
        while not is_prime():
            self.current += 1
        return self.current


def to_exponent(base, exp):
    result = 1
    results = []
    def posible_sums(num):
        divisor = prime()
        next(divisor)
        while divisor.current < num:
            current = num / divisor.current
            if current.is_integer():
                next(divisor)

    for x in range(2, exp+1):
        results.append((x, pow(base, x)))