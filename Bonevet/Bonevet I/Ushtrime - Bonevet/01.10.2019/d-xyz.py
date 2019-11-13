x = int(input("Vlera e X: "))
y = int(input("Vlera e Y: "))
z = int(input("Vlera e Z: "))


#X - me e madhe
#Y - me e madhe
#Z - me e madhe
if x>y and x>z:
    print("X eshte vlera me e madhe!")
if y>z and y>x:
    print("Y eshte vlera me e madhe!")
if z>y and z>x:
    print("Z eshte vlera me e madhe!")


#X - mesatare
#Y - mesatare
#Z - mesatare
if x>y and x<z or x>z and x<y:
    print("X eshte vlera mesatare!")
if y>x and y<z or y>z and y<x:
    print("Y eshte vlera mesatare!")
if z>y and z<x or z>x and z<y:
    print("Z eshte vlera mesatare!")


#X - me e vogel
#Y - me e vogel
#Z - me e vogel
if x<y and x<z:
    print("X eshte vlera me e vogel!")
if y<x and y<z:
    print("Y eshte vlera me e vogel!")
if z<x and z<y:
    print("Z eshte vlera me e vogel!")


if x==y<z:
    print("X&Y jane vlerat me te vogla dhe te barabarta!")  
if x==y>z:
    print("X&Y jane vlerat me te medha dhe te barabarta!")   
if y==z<x:
    print("Y&Z jane vlerat me te vogla dhe te barabarta!")       
if y==z>x:
    print("Y&Z jane vlerat me te medha dhe te barabarta!")
if z==x<y:
    print("X&Z jane vlerat me te vogla dhe te barabarta!")
if z==x>y:
    print("X&Z jane vlerat me te medha dhe te barabarta!")
