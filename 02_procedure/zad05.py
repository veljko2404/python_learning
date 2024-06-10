# 5. Stampati sve brojeve k od 2 do n koji su deljivi sa 3 a njihovi susedi (k−1 i k+1) nisu
# deljivi sa 7.

n = 100
for i in range(2, n):
    if i % 3 == 0 and (i - 1) % 7 != 0 and (i + 1) % 7 != 0:
        print(i)
