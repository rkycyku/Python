mosha = int(input("Mosha juaj: "))
statusi = 0
rezultati = ""
mesazhi = ""

if mosha <= 18:
    statusi = 0
elif mosha <= 64:
    statusi = 1
else:
    statusi = 0


if statusi == 1:
    rezultati = "mund te votoni"
else:
    rezultati = "nuk mund te votoni"

mesazhi = "Ju " + rezultati

print(mesazhi)

