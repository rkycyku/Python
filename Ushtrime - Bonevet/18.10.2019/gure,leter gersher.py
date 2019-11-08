import random

lista = ["gure","leter","gershere"]


i = 1

while i <= 5:
    njeriu = input("Gure, leter apo gershere: ")
    pc = random.choice(lista)

    while njeriu not in lista:
        print("*****NUK ESHTE SHENUAR MIRE TEKSTI!*****")
        njeriu = input("Gure, leter apo grshere: ")
        

    #print("Kompjuteri ka zgjedhur: ", pc)


    while pc == njeriu:
        print("Kompjuteri ka zgjedhur: ", pc)
        print("*****BARAZIM*****")
        njeriu = input("Gure, leter apo grshere: ")
        pc = random.choice(lista)
        i-=-1
    #print("Kompjuteri ka zgjedhur: ", pc)
        
    if pc == "gershere" and njeriu == "gure":
        print("Kompjuteri ka zgjedhur: ", pc)
        print("Fituat pas heres se ", i)
        break
    elif pc == "gershere" and njeriu == "leter":
        print("Kompjuteri ka zgjedhur: ", pc)
        print("*****HUMBE*****")

    elif pc == "gure" and njeriu == "gershere":
        print("Kompjuteri ka zgjedhur: ", pc)
        print("*****HUMBE*****")

    elif pc == "gure" and njeriu == "leter":
        print("Kompjuteri ka zgjedhur: ", pc)
        print("Fituat pas heres se ", i)
        break
    elif pc == "leter" and njeriu == "gure":
        print("Kompjuteri ka zgjedhur: ", pc)
        print("*****HUMBE*****")

    elif pc == "leter" and njeriu == "gershere":
        print("Kompjuteri ka zgjedhur: ", pc)
        print("Fituat pas heres se ", i)
        break
    if (i >= 5):
        print("Keni kaluar limit e mundesive, keni pasur vetem", i, "raste.")
        break
    i-=-1
