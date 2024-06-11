# 18. Napisati funkciju koja zadatu listu brojeva L meša tako da najpre idu elementi
# sa parnim, pa onda sa neparnim indeksima. Ako je L=[1,2,3,4,5] tada funkcija vraca
# listu [1,3,5,2,4].

list = [1, 2, 3, 4, 5]
result = []
for i in list:
    if i % 2 == 1:
        result.append(i)
for i in list:
    if i % 2 == 0:
        result.append(i)
print(result)
