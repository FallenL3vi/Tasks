import sys

max_bits : int = 32
now_liczba : int = 0

def porownanie(x: int) -> int:
    nowa_liczba = 0
    #print(str(x.bit_length()))
    if x.bit_length() > max_bits:
        return 0
    else:
        ujemna = False
        if x < 0:
            ujemna = True
        for i in str(abs(x)):
            x = abs(x)
            pozostala = x%10
            nowa_liczba = nowa_liczba * 10 + pozostala
            x = x//10
        if ujemna:
            nowa_liczba = -nowa_liczba
    return nowa_liczba

x = input()
x = int(x)
x = porownanie(x)
print(str(x))
