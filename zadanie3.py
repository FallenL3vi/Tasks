maximum_width : int = 16
word : str = ""
spaces : int = []
b = 0

def wypisz(index : int):
    nowa_lista = ""
    nowa_lista = " ".join(a[:index+1])
    spacje = []
    for i in range(len(nowa_lista)):
        if nowa_lista[i] == " ":
            spacje.append(i)
    while (maximum_width - len(nowa_lista)) > 0:
        for i in range(len(spacje)):
            nowa_lista = nowa_lista[:spacje[i]] + " " + nowa_lista[spacje[i]:]
            if len(nowa_lista) >= maximum_width:
                break
    print(nowa_lista + "\n")

word = input()
a = word.split(" ")

for i in range(len(a)):
    if b == 0:
        if (b + len(a[i])) < maximum_width:
            print("True")
            b += len(a[i])
        else:
            wypisz(i)
    elif (b + len(a[i])+1) < maximum_width:
        b += len(a[i])+1
        if i+1 <= len(a) and (b + len(a[i+1])+1) > maximum_width:
            wypisz(i)
            b = 0
    else:
        wypisz(i)
        b = 0
    if i+1 >= len(a):
        wypisz(i)
