#Loja e Fantazmes

from random import randint
import time

emri = input("Si e ke emrin? ")
time.sleep(1)

print("\nPershendetje", emri, 'eshte koha per te luajtur "Loja e Fantazmes"')
time.sleep(1)

ndihem_i_guximshem = True
piket = 0

while ndihem_i_guximshem:
    dera_e_fantazmes = randint(1,3)
    print("\nTre dyer perpara...")
    time.sleep(1)
    print("Nje fantazem pas njeres.")
    time.sleep(1)
    print("Cilen dere do te hapni?")
    time.sleep(1)
    dera = input("1,2 apo 3? ")
    time.sleep(1)
    numri_i_deres = int(dera)

    if numri_i_deres == dera_e_fantazmes:
        print("\nFantazem!")
        time.sleep(1)
        ndihem_i_guximshem = False
    else:
        print("\nNuk ka Fantazem!")
        time.sleep(1)
        print("Ti u fute ne dhomen tjeter.")
        time.sleep(1)
        piket +=1

print("\nLargohu!")
time.sleep(1)
print("Loja Mbaroi! Ti kalove", piket, "dhoma")
