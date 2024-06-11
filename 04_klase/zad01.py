# 1. Definisati klasu Objekat koji ima konstruktor sa dva parametra x i y koji predstavljaju poziciju objekta u ravni.
# Implementirati property X i Y koji maskiraju vrednosti x i y kao i metodu ukupno_poziva koja vraca ukupan broj puta
# koliko su pozvani property-ji X i Y (bilo kao getter ili setter). Implementirati konverziju u string
# (u formatu po zelji). Napisati kratak test kod.

class Object:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.counter = 0

    @property
    def x(self):
        self.counter += 1
        return self._x

    @property
    def y(self):
        self.counter += 1
        return self._y

    @x.setter
    def x(self, x):
        self.counter += 1
        self._x = x

    @y.setter
    def y(self, y):
        self.counter += 1
        self._y = y

    def getCounter(self):
        return self.counter


t = Object(3, 5)
t.x = 2
t.y = 10
print(f"[{t.x}, {t.y}]")
print(t.getCounter())
