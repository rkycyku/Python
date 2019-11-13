lista2 = []
lista3 = []

a = 50

while a < 150:
    if a%7 == 0 and a%5 !=0:
        if len(str(a)) == 2:
            lista2.append(a)
        elif len(str(a)) == 3:
            lista3.append(a)
    a+=1

print(lista2)
print(lista3)