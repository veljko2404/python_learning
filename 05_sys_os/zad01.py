# 1. Napisati program koji pronalazi sve fajlove sa zadatim imenom i stampa kompletne putanje do tih fajlova. Ime se unosi kao prvi parametar programa.

import os
import sys


def find_files(filename, search):
    result = []
    for root, dirs, files in os.walk(search):
        if filename in files:
            result.append(os.path.join(root, filename))
        return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    filename = sys.argv[1]
    search = os.getcwd()
    found_files = find_files(filename, search)
    if found_files:
        for file_path in found_files:
            print(file_path)
        else:
            print("Nothing was foundLL")
