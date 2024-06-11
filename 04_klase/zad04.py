# 4. Implementirati klasu ModP koja ima konstruktor sa dva parametra k i p,
# gde je p ceo prost broj (ako nije prost, konstruktor vraca exception).
# Klasa implementira operacije po modulu p (+, -, *).


class NotPrimeException(Exception):
    pass


def is_prime(number):
    if number == 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


class ModP:
    def __init__(self, k, p):
        if not is_prime(p):
            raise NotPrimeException("Number p must be prime!")
        self.k = k % p
        self.p = p

    def __add__(self, other):
        if isinstance(other, ModP) and other.p == self.p:
            return ModP((self.k + other.k) % self.p, self.p)
        elif isinstance(other, int):
            return ModP((self.k + other) % self.p, self.p)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ModP) and self.p == other.p:
            return ModP((self.k - other.k) % self.p, self.p)
        elif isinstance(other, int):
            return ModP((self.k - other) % self.p, self.p)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, ModP) and self.p == other.p:
            return ModP((self.k * other.k) % self.p, self.p)
        elif isinstance(other, int):
            return ModP((self.k * other) % self.p, self.p)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, ModP):
            return self.k == other.k and self.p == other.p
        elif isinstance(other, int):
            return self.k == other % self.p
        else:
            return False

    def __str__(self):
        return f"{self.k} (mod {self.p})"


try:
    a = ModP(10, 7)
    b = ModP(3, 7)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a + 5)
    print(a - 5)
    print(a * 5)

    # c = ModP(5, 9)
except NotPrimeException as e:
    print(e)
