lista = ["bonevet", "makina", "shtepia", "policia", "duqani"]

anetarlista = len(lista)

if anetarlista == 5:
    lista.remove("bonevet")
    print(lista)
elif anetarlista == 3:
    lista.append("Rilind")
    print(lista)
else:
    print("Gjithqka ne rregull")

