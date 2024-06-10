# 11. Naci maksimalnu vrednost aritmeticke sredine dva uzastopna elementa liste L.

l = [1, 3, 7, 5, 6, 3, 2, 0, 1, 6, 8, 2]
max = (l[0] + l[1]) / 2
for i in range(2, len(l)):
    if (l[i] + l[i - 1]) / 2 > max:
        max = (l[i] + l[i - 1]) / 2
print(max)
