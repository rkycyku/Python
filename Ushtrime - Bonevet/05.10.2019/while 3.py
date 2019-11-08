
a= ['Bonevet','Python','klasa','Kacanik']

v = input("Vendosni nje anetare: ")

print(a)
i=0

while i< len(a):
    if v == a[i]:
        print(v, "eksziston ne liste")
        break
    i+=1
else:
    print(v,"Nuk ekziston ne liste")

