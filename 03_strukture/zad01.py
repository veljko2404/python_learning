# 1. Napisati program koji generise N=10 vrednosti dobijenih bacanjem dve standardne kockice.

import random

n = 10
for i in range(0, n):
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    print((first, second))
