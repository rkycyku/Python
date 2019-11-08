import time,random

emri = input("Si e keni emrin? ")

print("Tung", emri, 'Koha per te luajtur "Qello fjalen sekrete"!')

time.sleep(1)

print("\nProvo te qellosh fjalen sekrete...")
time.sleep(.5)

lista = ["bonevet","rilind","kacanik"]
fjala_sekrete = random.choice(lista)


qello = ""

radha = 10

while radha > 0:
    deshtim = 0

    for shkronja in fjala_sekrete:
        if shkronja in qello:
            print(shkronja)
        else:
            print("_")
            deshtim +=1
    print("\nJu keni edhe", radha, "here per te provuar")

    if deshtim == 0:
        print("***FITOVE***")
        break
    
    qello_shkronjen = input("\nShkruaj shkronjen: ")
    qello_shkronjen = qello_shkronjen.lower()
    qello += qello_shkronjen
    
    if qello_shkronjen not in fjala_sekrete:
        radha -=1
        print("\n***GABIM***")
    if radha == 0:
        print("\n***HUMBE***")
        
