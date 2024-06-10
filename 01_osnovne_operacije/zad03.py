# 3. Izracunati cenu proizvoda, ako je data cena materijala
# i energenata. Za izradu proizvoda je potrebno broj_sati sati rada,
# a cena jednog radnog sata je cena_rada. Na tako dobijenu cenu treba
# dodati PDV od 20%.

price_mat=100
price_ene=100
hours=10
price_work=10
pdv=0.2
print((price_mat+price_ene+hours*price_work)*(1+pdv))
