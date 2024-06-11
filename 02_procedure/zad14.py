# 14. Datu poruku je potrebno sifrovati tako što se svako slovo zamenjuje sledecim
# slovom u engleskoj abecedi. Drugim recima, a se zamenjuje sa b, b sa c, ... ,
# z sa a, i slicno za velika slova. Ostali karakteri ostaju nepromenjeni.
# Na primer, ako je poruka = 'Marko123', nakon zamene je se dobija Nbslp123.

def encode_word(word):
    result = []
    for i in word:
        if 'a' <= i <= 'z':
            if i == 'z':
                result.append(i)
            else:
                result.append(chr(ord(i) + 1))
        elif 'A' <= i <= 'Z':
            if i == 'Z':
                result.append('A')
            else:
                result.append(chr(ord(i) + 1))
        else:
            result.append(i)
    return ''.join(result)


word = "Marko123"
print(encode_word(word))
