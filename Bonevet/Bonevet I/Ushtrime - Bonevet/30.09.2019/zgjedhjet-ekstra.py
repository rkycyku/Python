emri = input("Emri juaj: ")
mbiemri = input("Mbiemri juaj: ")
print("Ju lutemi qe tek gjinia te shenoni: ")
print("1 - per gjinin mashkullore")
print("0 - per gjinin femrore")
gjinia = int(input("Gjinia juaj: "))
qyteti = input("Nga cili qytet,fshat jeni: ")
mosha = int(input("Mosha juaj: "))
statusi = 0
rezultati = ""
mesazhiM = ""


if mosha <= 17:
    statusi = 0
elif mosha <= 64:
    statusi = 1
else:
    statusi = 0

if statusi == 1:
    rezultati = "mund te votoni " + "dhe keni te drejt vote ne " + qyteti
else:
    rezultati = "nuk mund te votoni!"

mesazhiM = "I nderuar Z. " + emri + " " + mbiemri + " " + "ju " + rezultati + "."
mesazhiF = "E nderuar Znj. " + emri + " " + mbiemri + " " + "ju " + rezultati + "."

if gjinia == 1:
    print(mesazhiM)
else:
    print(mesazhiF)
    