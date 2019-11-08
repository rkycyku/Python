
b = "Python"

lista = ["Bonevet", 56, 5.6, b]

lista.append("Kosove")
lista.remove(56)

print(lista)

print(len(lista))

print(lista[0])

print(len("Bonevet"))

print(lista.index(b))

if 56 in lista:
    print("PO")
else:
    print("JO")
