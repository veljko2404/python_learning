# 11. Slucajno izmesati sve redove fajla SMSSpamCollection.txt i zapamtiti ih u fajl shuffle.txt.
import random

with open("SMSSpamCollection.txt", "r") as f:
    lines = f.readlines()
    random.shuffle(lines)
    with open("shuffle.txt", "w") as shuffle:
        shuffle.writelines(lines)
