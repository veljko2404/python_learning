# 16. Napisati funkciju koja generiše listu delioca datog prirodnog broja n.

list = []
n = 168
for i in range(1, n + 1):
    if n % i == 0:
        list.append(i)
print(list)
