print("Sheno 1, per C ne F")
print("Sheno 2, per F ne C")
lloji = int(input("Sheno numrin: "))
temp = int(input("Sheno graden e temperatures: "))

def CneF():
    return (C * 9/5) + 32

def FneC():
    return (F - 32) * 5/9

if lloji == 1:
    C = temp

    print(CneF())

elif lloji == 2:
    F = temp

    print(FneC())