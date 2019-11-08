import random, time

min = 1
max = 6

gjuajguret = input("A deshironi te filloni me gjuajtjen e gureve? ")

while gjuajguret == "PO" or gjuajguret == "Po" or gjuajguret == "po" or gjuajguret == "pO":
    print("\nRrotullimim i gureve...")
    time.sleep(1)
    print("\nKeni qelluar...")
    time.sleep(1)
    g1 = print("Guri i pare:",random.randint(min,max))
    time.sleep(.5)
    g2 = print("Guri i dyte:",random.randint(min,max))
    

    gjuajguret = input("\nA deshironi te provoni prap? ")

