maximum_width : int = 16
word : str = ""
spaces : int = []

def wypisz(index : int):
    nowa_lista = " ".join(a[:index])
    print(nowa_lista)
word = input()
a = word.split(" ")
b = 0
for i in range(len(a)):
    if (b + len(a[i])) < maximum_width:
        b += len(a[i])
    else:
        wypisz(i)
