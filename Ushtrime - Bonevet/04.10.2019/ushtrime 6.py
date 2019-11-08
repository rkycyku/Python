

b = "Python"

lista = ["Bonevet", 56, 5.6, b]

lista.append("Kosove")
lista.append("Dafina")
lista.append("Kacanik")
lista.remove(56)

print(lista)

print(len(lista))

print(lista[0])

print(len("Dafina"))

print(lista.index(b))

if 56 in lista:
    print("PO")
else:
    print("JO")
    


