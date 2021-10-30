# Write your code here :-)
numery = {1: "", 2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"],
            5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["q", "r", "s"],
            8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
def wypisywanie(key : str, iteracja : int, numer : str):
    ktora_iteraca = iteracja
    #print(str(ktora_iteraca))
    iteracja += 1
    if key != "":
        if key[0] == "" or int(int(key[0])) <= 1:
                print("\n")
                wypisywanie(key[1:], iteracja, numer)
        else:
            pierwszy = True
            for value in numery.get(int(key[0])):
                if pierwszy:
                    pierwszy = False
                    numer = numer + value
                    if len(key) == 1:
                        print("\"" + numer + "\", ", end="")
                else:
                    if len(key) == 1:
                        print("\"" + (numer[:ktora_iteraca] + value) + "\", ", end="")
                    else:
                        #print("#")
                        nowy_numer = list(numer)
                        nowy_numer[ktora_iteraca] = value
                        numer = "".join(nowy_numer)
                wypisywanie(key[1:], iteracja, numer)

def wypisz_liczby(digits : str):
    numer = ""
    iteracja = 0
    wypisywanie(digits, iteracja,numer)
    print("\n")

digits = input()
if digits != "":
    wypisz_liczby(digits)
