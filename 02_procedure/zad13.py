#13. Data je lista imena koja se sastoji od imena ucenika, kao i lista poeni koja se
#sastoji od broja poena koje je svaki ucenik ostvario. Formirati i ispisati rang listu.
#Ukoliko dva učenika imaju isti broj poena, prednost ima učenik cije je ime prvo
#po abecednom redu.

names=["pera","jack","nick","james","patrick","villy","nicholas"]
points=[90,35,50,10,99,47,99]
n=len(names)
for i in range(0,n):
    for j in range(i+1,n):
        if points[i]>points[j]:
            tmp=points[i]
            points[i]=points[j]
            points[j]=tmp
            tmp=names[i]
            names[i]=names[j]
            names[j]=tmp
        elif points[i]==points[j]:
            if names[i] > names[j]:
                tmp=points[i]
                points[i]=points[j]
                points[j]=tmp
                tmp=names[i]
                names[i]=names[j]
                names[j]=tmp

for i in range(0,n):
    print(f"{names[i]} got {points[i]} points")
