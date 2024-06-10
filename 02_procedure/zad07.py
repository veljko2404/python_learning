# 7. Cena novog automobila je 20000. Vrednost automobila opada 15% godisnje u prvih 5 godina,
# a nakon toga 10% godisnje. Naci vrednost nakon k godina.

price = 20000
k = 10
for i in range(1, k):
    if i <= 5:
        price -= price * 0.15
    else:
        price -= price * 0.1
print(price)
