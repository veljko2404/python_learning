# 10. Formirati dva nova fajla ham.txt i spam.txt koji se sastoje iz SMS poruka iz
# fajla SMSSpamCollection.txt koje su oznacene kao 'ham' i 'spam'.

with open("SMSSpamCollection.txt", "r") as f:
    for line in f:
        if line.startswith("spam"):
            with open("spam.txt", "a") as spam:
                spam.write(line)
        else:
            with open("ham.txt", "a") as ham:
                ham.write(line)
