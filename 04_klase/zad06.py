# 6. Implementirati iterator/generator Prosti koji generise proste brojeve.

def is_prime(number):
    if number == 1:
        return True
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


class PrimeGenerator:
    def __init__(self, n):
        self.idx = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        while not is_prime(self.idx):
            if self.n == self.idx:
                raise StopIteration
            self.idx += 1
        return self.idx


for i in PrimeGenerator(40):
    print(i)
