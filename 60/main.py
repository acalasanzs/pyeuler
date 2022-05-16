""" 
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
class Prime:
    def __init__(self, current = None):
        self.current = current
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            self.current = 1
        else:
            self.current += 1
        while not Prime.is_prime(self.current):
            self.current += 1
        return self.current
    def is_prime(number):
        if number == 1:
            return False
        x = number-1
        while x > 1:
            if number % x == 0:
                return False
            x -= 1
        return True

class TwoPrimeSum:
    def __init__(self, start):
        self.n = 2
        self.start = start
        self.primes = []
        self.sum = 0
    def __iter__(self):
        return self
    def __next__(self):
        pass
    def has_property(self, arr):
        index = [0 for x in range(self.n)]
        minimum = None
        def update():
            self.sum = sum("".join([self.primes[i] for i in index]))
        while True:
            if self.x == self.n:
                self.x = 0
                if self.y < self.n:
                    self.y += 1
            else:
                break
            update()
    def concat(*values):
        return int("".join([str(val) for val in values]))

""" from60 = Prime(60)
for x in range(3):
    next(from60)
    print(from60.current) """