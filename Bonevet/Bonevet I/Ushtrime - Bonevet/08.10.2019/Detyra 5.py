lista = ['popo',1,2,'prepre']

i=0

while i < len(lista):
    if (len(str(lista[i]))) > 2:
        lista[i] = "Eshte"
    i+=1
print(lista)