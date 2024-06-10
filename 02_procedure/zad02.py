# 2. Porodice sa maloletnom decom dobijaju decji dodatak i to, ako imaju jedno dete,
# dobijaju 15.000 dinara, za dvoje dece dobijaju 20.000, za troje 25.000, a ako imaju
# više od tri deteta, dobijaju 30.000 dinara. Na osnovu datog broja dece, odrediti
# koliko dinara će porodica dobiti.

number_of_kids = 2
if number_of_kids == 1:
    print(15000)
elif number_of_kids == 2:
    print(20000)
elif number_of_kids == 3:
    print(25000)
elif number_of_kids > 3:
    print(30000)
