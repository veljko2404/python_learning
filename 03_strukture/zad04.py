# 4. Na zabavu je pozvano M ljudi. Kolike su sanse da dve osobe imaju rođendan istog dana
# (pod pretpostavkom da je su za svaku osobu podjednake šanse da je rođena bilo kog od 365 dana u godini)?

m = 10
if m > 365:
    print(1)
else:
    prob = 1.0
    for i in range(m):
        prob *= (365 - i) / 365
    print(1 - prob)
