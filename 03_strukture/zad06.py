# 6. Biramo dva (pseudo)slučajna broja a,b iz (0,1) a zatim i treći x uniformno u intervalu (a,b).
# Podeliti interval (0,1) na M intervala jednake dužine i odrediti koliko puta broj x pripada svakom od
# intervala, ukoliko se eksperiment ponovi N puta. Izvrsiti program za M=10 i N=1000000.

import random

m = 10
n = 1000000
intervals = [0] * m
width = 1 / m
for i in range(n):
    a = random.random()
    b = random.random()
    x = random.uniform(a, b)
    interval = int(x / width)
    intervals[interval] += 1
print(intervals)
