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
    exponents = posible_sums(exp)[::-1]
    idx = 0
    while idx < len(exponents)-1:
        current = exponents[idx]
        if idx > 0:
            rest = exponents[idx+1] - current
            match = -1
            matches = []
            for i in exponents:
                match += 1
                if rest == i:
                    matches.append(True)
                else:
                    matches.append(False)
            print(matches)
            if any(matches):
                results.append((exponents[match], pow(base, exponents[match])))
            else:
                results.append((current, pow(base, current)))
        else:
            results.append((current, pow(base, current)))
        idx += 1
    return results
print(to_exponent(2,12))
