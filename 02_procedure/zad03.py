# 3. Ispitati da li je uneta godina prestupna. Godina je prestupna ako je deljiva sa 4
# a nije deljiva sa 100, ili deljiva sa 400.

year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Yes")
else:
    print("No")
