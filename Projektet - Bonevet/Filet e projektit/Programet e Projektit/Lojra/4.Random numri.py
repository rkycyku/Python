import random
times = int(input("Sa here deshironi ta provon: "))

numri = random.randint(1,100)
qello = int(input("\nGjej numrin nga 1 deri 100: "))

i = 1
while qello != numri:
    if qello < numri:
        print("\nNumri eshte me i madhe!")
        qello = int(input("\nGjej numrin nga 1 deri 100: "))
    else:
        print("\nNumri eshte me i vogel!")
        qello = int(input("\nGjej numrin nga 1 deri 100: "))
    i+=1
    for i in range(times + 1):
        print("Keni kaluar limit e mundesive, keni pasur vetem", i, "raste.")
        i+=1
        break
        
        
print("\nNumri eshte i sakte!")
print("Fituar per heren e", i)
  