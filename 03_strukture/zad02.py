# 2. Izbrojati koliko puta se javlja koji broj pri bacanju dve kockice N=10000 puta. Koliko
# procenata od svih bacanja odgovara svakom od brojeva od 2 do 12?

import random

n = 1000
l = [0] * 11
for i in range(0, n):
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    sum = first + second
    l[sum - 2] += 1
for i in range(len(l)):
    print(f"Sum {i + 2} occured {l[i]} times which is {l[i] / 10}%")
