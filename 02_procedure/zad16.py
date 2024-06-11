# 17. Napisati funkciju koja računa broj velikih i malih slova u datom stringu s.

s = "NOdnaodnNSANdansdNsN"
small = 0
big = 0
for i in s:
    if 'a' <= i <= 'z':
        small += 1
    elif 'A' <= i <= "Z":
        big += 1
print(f"Small: {small}, big: {big}")
