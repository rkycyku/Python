

def shuma(numri1,numri2):
    return numri1 + numri2
def zbritja(numri1,numri2):
    return numri1 - numri2
def shumezimi(numri1,numri2):
    return numri1 * numri2
def pjesetimi(numri1,numri2):
    return numri1 / numri2

x = int(input("Vlera e X: "))
y = int(input("Vlera e Y: "))

'''print("x + y = ", shuma(x,y))

print("x - y = ", zbritja(x,y))

print("x * y = ", shumezimi(x,y))

print("x / y = ", pjesetimi(x,y))'''

print("Operatoret:")
print("1. Shuma")
print("2. Zbritja")
print("3. Shumezimi")
print("4. Pjesetimi")

z = input("Zgjidh operatorin: ")

if z=="1":
    print("x + y = ", shuma(x,y))
elif z=="2":
    print("x - y = ", zbritja(x,y))
elif z=="3":
    print("x * y = ", shumezimi(x,y))
elif z=="4":
    print("x / y = ", pjesetimi(x,y))
    
    
