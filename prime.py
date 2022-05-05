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