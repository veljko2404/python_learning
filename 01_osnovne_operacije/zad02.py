# 2. Ispisati osnovnu cenu artikla, vrednost poreza od 20 %, kao i ukupnu cenu
# artikla. Sve vrednosti ispisati na dve decimale, svaku u novom redu,
# sa odgovarajućom porukom na pocetku reda.

price = float(input())
base_price = price
total_price = price * 1.2
tax = price * 0.2

print(f"Base price = {base_price:.2f}")
print(f"Total price = {total_price:.2f}")
print(f"Tax = {tax:.2f}")