fjalori = {"Bonevet" : "Kacanik", 2 : "Python"}

print(fjalori[2])
print(fjalori.get(2))

fjalori['Shkolla'] = "Emin DUraku"
print(fjalori)

fjalori.popitem()
print(fjalori)

del fjalori["Bonevet"]
print(fjalori)

fjalori.clear()
print(fjalori)
