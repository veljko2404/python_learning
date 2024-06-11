# 8. Izračunati približno broj π pomoću formule: π≈ 4Nu/N gde je N broj (uniformnih) pseudoslučajnih tačaka
# (x,y)∈[0,1]^2 a Nu broj tačaka koje se nalaze unutar jediničnog kruga!

import random

n = 1000000
nu = 0
for _ in range(n):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <= 1:
        nu += 1
print(4 * nu / n)
