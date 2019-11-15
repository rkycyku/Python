from time import sleep
from random import randint

shakedice = input("Do you want to shake the dice? ")
shakedice = shakedice.lower()

while shakedice == "yes":
    d1 = randint(1,6)
    d2 = randint(1,6)
    d3 = randint(1,6)
    d4 = randint(1,6)
    
    player = d1 + d2
    computer = d3 + d4

    print("Your turn to roll")
    sleep(1)
    print("You shook a " + str(d1) + " and " + str(d2) + ", so you have " + str(player))
    sleep(1)
    print("My turn to roll")
    sleep(1)
    print("I shook a " + str(d1) + " and " + str(d2) + ", so I have " + str(player))

    if player > computer:
        sleep(1)
        print("\nYou won")
    elif player < computer:
        sleep(1)
        print("\nI won")
    else:
        sleep(1)
        print("\nTie")
        
    sleep(1)
    shakedice = input("\nA deshironi te gjuani perseri? ")
    shakedice = shakedice.lower()
    



