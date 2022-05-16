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
        while not self.is_prime(self.current):
            self.current += 1
        return self.current
    def is_prime(self, number):
        if number == 1:
            return False
        x = number-1
        while x > 1:
            if number % x == 0:
                return False
            x -= 1
        return True