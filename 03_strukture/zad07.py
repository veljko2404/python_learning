# 7. Bacamo kocku prvi put. Neka je n dobijeni broj. Onda je bacamo narednih n puta i neka je s suma dobijenih
# n brojeva. Odrediti koje su moguće vrednosti za s i koliko puta se svaka pada ukoliko eksperiment
# ponovimo N=100000 puta.

import random

N = 100000
result = [0] * 36
for i in range(N):
    sum = 0
    n = random.randint(1, 6)
    for j in range(n):
        sum += random.randint(1, 6)
    result[sum] += 1
for i in range(len(result)):
    print(f"Sum {i + 1} occurred {result[i]} times")
