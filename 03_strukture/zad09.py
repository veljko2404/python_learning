# 9. Izbrojati koliko ima redova u fajlu SMSSpamCollection.txt koji pocinju sa 'ham' i
# koji pocinju sa 'spam'.

def count_lines(filename, word):
    result = 0
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if line.startswith(word):
                result += 1
            if not line:
                break
    return result


print(f"{count_lines('SMSSpamCollection.txt', 'spam')} lines has spam")
print(f"{count_lines('SMSSpamCollection.txt', 'ham')} lines has ham")
