from time import sleep
from random import randint

shakedice = input("Let's shake some dice! (Y/N) ")
shakedice = shakedice.lower()

playerpoints = 0
computerpoints = 0


while shakedice == "y":
    d1 = randint(1,6)
    d2 = randint(1,6)
    d3 = randint(1,6)
    d4 = randint(1,6)
    
    player = d1 + d2
    computer = d3 + d4

    print("\nYour turn to roll")
    sleep(1)
    print("You shook a " + str(d1) + " and " + str(d2) + ", so you have " + str(player))
    sleep(1)
    print("\nMy turn to roll")
    sleep(1)
    print("I shook a " + str(d3) + " and " + str(d4) + ", so I have " + str(computer))

    if player > computer:
        playerpoints += 1
        sleep(1)
        print("\nYou won")
        sleep(1)
        print("\nYou win", str(player) + " to " + str(computer))
        sleep(1)
    elif player < computer:
        computerpoints += 1
        sleep(1)
        print("\nI won")
        sleep(1)
        print("\nI win", str(computer) + " to " + str(player))
        sleep(1)
    elif player == computer:
        sleep(1)
        print("\nTie")
        
    if playerpoints > 4:
        print("\nYou win the game!")
        break
    elif computerpoints > 4:
        print("\nI win the game!")
        break
    
    if playerpoints > computerpoints:
        sleep(1)
        print("\nYou're winning", str(playerpoints) + " to " + str(computerpoints))
    elif computerpoints > playerpoints:
        sleep(1)
        print("\nI'm winning", str(computerpoints) + " to " + str(playerpoints))
    else:
        sleep(1)
        print("\nThe score is tied", str(playerpoints) + " to " + str(computerpoints))

    shakedice = input("\nCountinue? (Y/N) ")
    shakedice = shakedice.lower()

    if shakedice == "n":
        print("\nHave a nice day!")
        sleep(1)
        if playerpoints > computerpoints:
            print("\nYou win the game!")
            sleep(1)
            print("You've won", str(playerpoints) + " to " + str(computerpoints))
        elif computerpoints > playerpoints:
            print("\nI win the game!")
            sleep(1)
            print("I've won ", str(computerpoints) + " to " + str(playerpoints))
        else:
            print("\nGame is a Tie!")
            sleep(1)
            print("The score is tied", str(playerpoints) + " to " + str(computerpoints))




