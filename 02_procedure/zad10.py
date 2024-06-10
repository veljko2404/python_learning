# 10. Naci minimalni element liste L kao i poziciju na kojoj se nalazi.

l = [1, 3, 7, 5, 6, 3, 2, 0, 1, 6, 8, 2]
position = 0
min = l[0]
for i in range(1, len(l)):
    if l[i] < min:
        min = l[i]
        position = i
print(f"l[{position}] = {min}")
