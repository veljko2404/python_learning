# 8. Naci najveci broj d takav da su brojevi m i n deljivi brojem d (najveci zajednicki delilac).

m = 40
n = 35
d = 1
for i in range(min(n, m), 1, -1):
    if m % i == 0 and n % i == 0:
        d = i
        break
print(d)
