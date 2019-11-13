x = int(input("Vlera e X : "))
y = int(input("Vlera e Y : "))
z = int(input("Vlera e Z : "))

#X - me i madh,vogel,mesatar
if x>y and x>z:
    print("X eshte numri me i madhe!")
elif x>y and x<z or x>z and x<y:
    print("X eshte numri mesatar!")
else:
    print("X eshte numri me i vogel!")
#Y - me i madh,vogel,mesatar
if y>x and y>z:
    print("Y eshte numri me i madhe!")
elif y>x and y<z or y>z and y<x:
    print("Y eshte numri mesatar!")
else:
    print("Y eshte numri me i vogel!")
#Z - me i madh,vogel,mesatar
if z>y and z>x:
    print("Z eshte numri me i madhe!")
elif z>y and z<x or z<y and z>x:
    print("Z eshte numri mesatar!")
else:
    print("Z eshte numri me i vogel!")
#Mbledhja e XYZ
print("X + Y + Z =", x+y+z)
#Zbritja e XYZ
print("X - Y - Z =", x-y-z)
'''print("Y - Z - X =", y-z-x)
print("Z - X - Y =", z-x-y)
print("X - Z - Y =", x-z-y)
print("Y - X - Z =", y-x-z)
print("Z - Y - x =", z-y-z)'''
#Shumezimi i XYZ
print("X * Y * Z =", x*y*z)
#Pjestimi i XYZ
print("X / Y / Z =",x/y/z)
'''
print("Y / Z / X =", y/z/x)
print("Z / X / Y =", z/x/y)
print("X / Z / Y =", x/z/y)
print("Y / X / Z =", y/x/z)
print("Z / Y / x =", z/y/z)
'''




