lista = [1,2,3,4,5,6,7,8,9]

tek = 0
qift = 0
for i in range(len(lista)):
    if lista[i] %2 == 0:
        qift+=1
    if lista[i] %2 !=0:
        tek+=1

print("Numra Qift jane : ", qift)
print("Numra Tek jane : ", tek)