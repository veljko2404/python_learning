# 1. Na osnovu vremena (u satima) odrediti koje je doba dana (jutro je od 6h do 10h,
# dan do 18h, vece do 22h, a u suprotnom je noc).

hours = 22
if hours > 24 or hours < 0:
    raise (ValueError("Number must be between 0 and 24"))
if hours > 6 and hours < 10:
    print("Morning")
elif hours >= 10 and hours < 18:
    print("Day")
elif hours >= 18 and hours < 22:
    print("Midnight")
else:
    print("Night")
