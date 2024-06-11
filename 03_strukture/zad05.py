# 5. Bacamo 3 kocke (kao u igri Jamb) i neka je  s  zbir dobijenih brojeva. Odrediti moguće vrednosti za s
# i koliko puta se javlja svaka vrednost ukoliko eksperiment ponovimo N=10000 puta.

import random

n = 10000
l = [0] * 16
for i in range(0, n - 2):
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    third = random.randint(1, 6)
    s = first + second + third
    l[s - 3] += 1
for i in range(len(l)):
    print(f"Number {i + 3} occurs {l[i]} times which is {l[i] / n * 100}% of time")
