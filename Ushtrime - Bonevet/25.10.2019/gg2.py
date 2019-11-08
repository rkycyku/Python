import random, time

min = 1
max = 6

gjuajguret = input("A deshironi te filloni me gjuajtjen e gureve? ")

while gjuajguret == "Po" or gjuajguret == "po" or gjuajguret == "PO":
    g1 = random.randint(min,max)
    g2 = random.randint(min,max)
    g3 = random.randint(min,max)
    g4 = random.randint(min,max)
    print("\nPo Rrotullohen guret per lojtarin e 1...")
    time.sleep(1)
    print("\nKeni qelluar...")
    time.sleep(1)
    print("Guri i pare:",g1)
    time.sleep(.8)
    print("Guri i dyte:",g2)

    print("\nPo rrotullohen guret per lojtarin e 2...")
    time.sleep(1)
    print("\nKeni qelluar...")
    time.sleep(1)
    print("Guri i pare:",g3)
    time.sleep(.8)
    print("Guri i dyte:",g4)

    lojtari1 = g1 + g2
    time.sleep(1)
    print("\nLojtari 1 ne total ka:", lojtari1)
    lojtari2 = g3 + g4
    time.sleep(1)
    print("Lojtari 2 ne total ka:", lojtari2)

    if lojtari1 > lojtari2:
        time.sleep(1)
        print("\nKa fituar lojtari 1")
    elif lojtari1 < lojtari2:
        time.sleep(1)
        print("\nKa fituar lojtari 2")
    else:
        time.sleep(1)
        print("\nRezultati eshte barazim")
        
    time.sleep(1)
    gjuajguret = input("\nA deshironi te gjuani perseri? ")
    



