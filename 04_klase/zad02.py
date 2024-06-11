# 2. Definisati klasu Krug koja nasledjuje klasu Objekat i ima 3 parametra, _x, y i r (poluprecnik kruga). Implementirati property R,
# prilagoditi funkciju ukupno_poziva da racuna i pozive property-ja R. Implementirati metodu povrsina koja vraca povrsinu kruga po
# formuli r^2*pi. Konstantu pi uvesti iz biblioteke math.

import math


class Object:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y


class Circle(Object):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self._r = r
        self.counterR = 0

    @property
    def r(self):
        self.counterR += 1
        return self._r

    @r.setter
    def r(self, r):
        self.counterR += 1
        self._r = r

    def surface(self):
        return math.pi * self._r ** 2

    def getCounterR(self):
        return self.counterR


c = Circle(3, 4, 8)
c.x = 5
c.r = 7
print(c.getCounterR())
