
x = int(input("Vlera e X: "))
y = int(input("Vlera e Y: "))

def mbledhja(x,y):
    return x + y
def zbritja(x,y):
    return x - y
def shumezimi(x,y):
    return x * y
def pjestimi(x,y):
    return x / y

print("Zgjidh njerin nga operatoret: ")
print("1. Mbledhje")
print("2. Zbritje")
print("3. Shumezim")
print("4. Pjestim")

operatori = int(input("Zgjidhni njerin nga opertoret: "))

if operatori == 1:
    print("X + Y = ", mbledhja(x,y))
elif operatori == 2:
    print("X - Y = ", zbritja(x,y))
elif operatori == 3:
    print("X * Y = ", shumezimi(x,y))
elif operatori == 4:
    print("X / Y = ", pjestimi(x,y))
else:
    print("Operatori eshte gabim")
