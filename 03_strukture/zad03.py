# 3. Napisati program koji za zadati datum ispisuje dane u nedelji za taj dan i narednih 7 dana.

from datetime import datetime, timedelta

t = datetime.now()
for i in range(0, 8):
    print(t.strftime("%A"))
    t = t + timedelta(days=1)
