# 12. Naći drugi maksimalni element liste L i njegov indeks.

l = [1, 3, 7, 5, 6, 3, 2, 0, 1, 6, 8, 2]
max = max(l)
position = 0
max2 = l[0]
for i in range(1, len(l)):
    if l[i] > max2 and l[i] != max:
        max2 = l[i]
        position = i
print(f"l[{position}] = {max2}")
