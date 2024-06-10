# 1. Napisati program kojim se odredjuje vreme prizemljenja aviona koji je uzleteo u
# x sati, y minuta i z sekundi, i u letu proveo ukupno q sekundi. Vreme ispisati
# u formatu hh:mm:ss.

from _datetime import datetime, timedelta

x = int(input())
y = int(input())
z = int(input())
q = int(input())

takeoff_time = datetime(year=2024, month=5, day=2, hour=x, minute=y, second=z)

landed_time = takeoff_time + timedelta(seconds=q)

print(f"Airplane landed: {landed_time.strftime('%H:%M:%S')}")

message = str(landed_time)
print(message)
print(message.split()[1])
