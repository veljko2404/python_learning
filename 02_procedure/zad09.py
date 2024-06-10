# 9. Naci sumu parnih elemenata liste brojeva L.

l = [1, 3, 7, 5, 6, 3, 2, 0, 1, 6, 8, 2]
sum = 0
for i in range(0, len(l)):
    if l[i] % 2 == 0:
        sum += l[i]
print(sum)
