# 2. Napisati program koji racuna i ispisuje koliko bajtova zauzima radni direktorijum (sa svim fajlovima i poddirektorijumima).

import os


def get_dir_size(dir):
    total = 0
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total += os.path.getsize(filepath)
    return total


print(get_dir_size(os.getcwd()))
