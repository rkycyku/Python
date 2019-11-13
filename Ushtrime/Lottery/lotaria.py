import random

i1ne1 = False
i2ne1 = False
i3ne1 = False
i1ne2 = False
i2ne2 = False
i3ne2 = False
i1ne3 = False
i2ne3 = False
i3ne3 = False

sakta = 0
shumaparave = 0


numrat = [1,2,3,4,5,6,7,8,9]

kompjuteri1 = random.choice(numrat)
kompjuteri2 = random.choice(numrat)
kompjuteri3 = random.choice(numrat)

numri1 = int(input("Vendosni nje numer nga 1 deri ne 9: "))
numri2 = int(input("Vendosni nje numer nga 1 deri ne 9: "))
numri3 = int(input("Vendosni nje numer nga 1 deri ne 9: "))

if kompjuteri1 == numri1:
    i1ne1 = True
    sakta = sakta + 1
elif i1ne1 == False and kompjuteri1 == numri2:
    i1ne2 = True
    sakta = sakta + 1
elif i1ne1 == False and i2ne1 == False and kompjuteri1 == numri3:
    i1ne3 = True
    sakta = sakta + 1 

if i1ne1 == False and kompjuteri2 == numri1:
    i1ne2 = True
    sakta = sakta + 1
elif i1ne2 == False and i2ne1 == False and kompjuteri2 == numri2:
    i2ne2 = True
    sakta = sakta + 1
elif i1ne2 == False and i2ne2 == False and i3ne1 == False and kompjuteri2 == numri3:
    i3ne2 = True
    sakta = sakta + 1

if i1ne1 == False and i1ne2 == False and kompjuteri3 == numri1:
    i1ne3 = True
    sakta = sakta + 1
elif i1ne3 == False and i2ne1 == False and i2ne2 == False and kompjuteri3 == numri2:
    i2ne3 = True
    sakta = sakta + 1
elif i1ne3 == False and i2ne3 == False and i3ne1 == False and i3ne2 == False and kompjuteri3 == numri3:
    i3ne3 = True
    sakta = sakta + 1

if sakta == 1:
    shumaparave = 250
elif sakta == 2:
    shumaparave = 500
elif sakta == 3:
    shumaparave = 1000
else:
    shumaparave = 0

if sakta == 0:
    print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3) + "\nNdersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3) + "\nNa vjen keq por ti nuk ke fituar asgje pasiqe nuk keni asnje numer te sakt!")
elif sakta == 1:
    print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3) + "\nNdersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3) + "\nDhe ti ke vetem " + str(sakta) + " numer te sakte" + "\nDhe ke fituar $" + str(shumaparave))
elif sakta == 2:
    print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3) + "\nNdersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3) + "\nDhe ti ke " + str(sakta) + " numera te sakte" + "\nDhe ke fituar $" + str(shumaparave))
elif sakta == 3:
    print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3) + "\nNdersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3) + "\nJu lumte ju keni gjetur " + str(sakta) + " numra te sakte" + "\nDhe ju keni fituar $" + str(shumaparave))
