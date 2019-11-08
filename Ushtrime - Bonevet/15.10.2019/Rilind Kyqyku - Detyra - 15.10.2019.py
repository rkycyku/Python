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

print(*lista, sep = "\n")
