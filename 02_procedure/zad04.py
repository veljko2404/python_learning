# 4. Plate se oporezuju progresivno. Plate do 20.000 dinara se ne oporezuju, one do 40.000
# se oporezuju po stopi od 2%, do 60.000 po stopi od 4%, a one iznad toga po stopi od 8%.
# Na osnovu vrednosti bruto plate izračunati vrednost neto plate, koja se dobija odbitkom poreza.

salary = 60000

if salary >= 60000:
    salary = salary * 1.08
elif salary >= 40000:
    salary = salary * 1.04
elif salary >= 20000:
    salary = salary * 1.02

print(salary)
