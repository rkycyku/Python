aplikantet = int(input("Sa Persona do te aplikojne? "))

lista = []

for i in range(aplikantet):
    emrimbiemri = input("Emri dhe Mbiemri: ")
    lista.append(emrimbiemri)
    mosha = input("Mosha: ")
    lista.append(mosha)
    gjinia = input("Gjinia: ")
    lista.append(gjinia)
    shkolla = input("Shkolla: ")
    lista.append(shkolla)

e = 0


while e < len(lista):
    print("\nEmri dhe Mbiemri: ",lista[e])
    e+=1
    print("Mosha: ",lista[e])
    e+=1
    print("Gjinia: ",lista[e])
    e+=1
    print("Shkolla: ",lista[e])
    e+=1
