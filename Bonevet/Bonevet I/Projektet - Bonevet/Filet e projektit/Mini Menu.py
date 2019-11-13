# Librarit
from random import randint,choice,shuffle
## Randint perdoret per te zgjedhur nje numer te qfardoshem
## Choice perdoret per te zgjedhur diqka nga lista
## Shuffle perdeoret per te perzier karakteret
from time import sleep
## Sleep perdoret per ta vendosur nje komand ne pritje per aq kohe sa i japim 


# Emri i perdoruesit
perdoruesi = input("Pershendetje. Si quheni? ")
sleep(.5)
# Ky mesazh sherben per te pershendetur perdoruesin
print("\nMiresevini", perdoruesi)
sleep(.5)
# Keto variabla sherbejne per te pyetur perdoruesin a deshiron te hapi menun apo jo
print('\nShkruani "Po" per te hapur menun,')
sleep(.1)
print('Shkruani "Jo" per te mbyllur programin.')
sleep(.1)
fillimi_i_menys = input("\nA deshironi te hapni menun? ")
fillimi_i_menys = fillimi_i_menys.lower()

# Ky funksion sherben kur perdoruesi nuk deshiron te kthehet ne menu
while fillimi_i_menys == "jo":
    menuja = 0
    loja = 0
    programi = 0
    print("\nMire u pafshim", perdoruesi)
    break

# Ky funksion sherben per te shfaqur menun
while fillimi_i_menys == "po":
    # Mini Menuja per te vendosur cilen nga menut te hapesh
    print("\n///////////////////////////////////////////////")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("/                  Mini Menu                  /")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("///////////////////////////////////////////////")
    sleep(.1)
    # Menut ne dispozicion
    print("\nVendos numrin 1 per te hapur menun e lojrave")
    sleep(.1)
    print("Vendos numrin 2 per te hapur menun e programeve")
    sleep(.1)
    # Variabla e menys
    menuja = int(input("\nCilen meny deshironi te hapni? "))

    # Kodimet e Menyve 

    # Menuja e pare
    while menuja == 1:
        # Menuja e Lojrave
        print("\n//////////////////////////////////////////////////////////////")
        sleep(.1)
        print("/                                                            /")
        sleep(.1)
        print("/                                                            /")
        sleep(.1)
        print("/                         Game Menu                          /")
        sleep(.1)
        print("/                                                            /")
        sleep(.1)
        print("/                                                            /")
        sleep(.1)
        print("//////////////////////////////////////////////////////////////")
        sleep(.1)
        # Lojrat ne dispozicion
        print('\nVendos numrin 1 per te luajtur lojen e "Lotaris"')
        sleep(.1)
        print('Vendos numrin 2 per te luajtur lojen e "Hedhjes se gureve"')
        sleep(.1)
        print('Vendos numrin 3 per te luajtur lojen e "Gure,Leter & Gershere"')
        sleep(.1)
        print('Vendos numrin 9 per tu kthyer prapa ne menu')
        sleep(.1)
        # Variabla e lojes
        loja = int(input("\nCilen loje deshironi te luani? "))

        # Fillimi i kodimit te lojrave
        
        # Loja e lotaris
        while loja == 1:
            # Grafiku i lojes se lotaris
            print("\n///////////////////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                                 /")
            sleep(.1)
            print("/                                                                 /")
            sleep(.1)
            print("/                         Loja e lotaris                          /")
            sleep(.1)
            print("/                                                                 /")
            sleep(.1)
            print("/                                                                 /")
            sleep(.1)
            print("///////////////////////////////////////////////////////////////////")

            # False ne kete rast sherben per ti bere variablat si te pasakta 
            i1ne1 = False
            i2ne1 = False
            i3ne1 = False
            i1ne2 = False
            i2ne2 = False
            i3ne2 = False
            i1ne3 = False
            i2ne3 = False
            i3ne3 = False

            # Keto variabla sherbejn per ti bere ato si 0 apo fillestare pastaj ti japin vlere kodet e meposhtme
            sakta = 0
            shumaparave = 0

            # Lista e numrave
            numrat = [1,2,3,4,5,6,7,8,9]

            # Keto variabla sherbejne per te zgjedhur nje numer nga lista 'numrat'
            kompjuteri1 = choice(numrat)
            kompjuteri2 = choice(numrat)
            kompjuteri3 = choice(numrat)

            # Keto variabla sherbejne per te vendosur numrat nga pordoruesi
            numri1 = int(input("\nVendosni nje numer nga 1 deri ne 9: "))
            numri2 = int(input("Vendosni nje numer tjeter nga 1 deri ne 9: "))
            numri3 = int(input("Vendosni per here te fundit nje numer nga 1 deri ne 9: "))

            # Keto sherbejn per te treguar se a eshte numri i 1 i sakt apo pasakt
            if kompjuteri1 == numri1:
                i1ne1 = True
                sakta = sakta + 1
            elif i1ne1 == False and kompjuteri1 == numri2:
                i2ne1 = True
                sakta = sakta + 1
            elif i1ne1 == False and i2ne1 == False and kompjuteri1 == numri3:
                i3ne1 = True
                sakta = sakta + 1 

            # Keto sherbejn per te treguar se a eshte numri i 2 i sakt apo pasakt
            if i1ne1 == False and kompjuteri2 == numri1:
                i1ne2 = True
                sakta = sakta + 1
            elif i1ne2 == False and i2ne1 == False and kompjuteri2 == numri2:
                i2ne2 = True
                sakta = sakta + 1
            elif i1ne2 == False and i2ne2 == False and i3ne1 == False and kompjuteri2 == numri3:
                i3ne2 = True
                sakta = sakta + 1

            # Keto sherbejn per te treguar se a eshte numri i 3 i sakt apo pasakt
            if i1ne1 == False and i1ne2 == False and kompjuteri3 == numri1:
                i1ne3 = True
                sakta = sakta + 1
            elif i1ne3 == False and i2ne1 == False and i2ne2 == False and kompjuteri3 == numri2:
                i2ne3 = True
                sakta = sakta + 1
            elif i1ne3 == False and i2ne3 == False and i3ne1 == False and i3ne2 == False and kompjuteri3 == numri3:
                i3ne3 = True
                sakta = sakta + 1

            # Keto funksione sherbejne per te caktuar shumen e parave te fituara
            if sakta == 1:
                shumaparave = 250
            elif sakta == 2:
                shumaparave = 500
            elif sakta == 3:
                shumaparave = 1000
            else:
                shumaparave = 0

            # Printimi i rezultatit ne qoftese asnje numer nuk eshte i sakte
            if sakta == 0:
                sleep(.1)
                print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3)) 
                sleep(.1)
                print("Ndersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3)) 
                sleep(.1)
                print("Na vjen keq por ti nuk ke fituar asgje pasiqe nuk keni asnje numer te sakt!")
                sleep(.1)
            # Printimi i rezultatit ne qoftese vetem nje numer eshte i sakte
            elif sakta == 1:
                sleep(.1)
                print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3))
                sleep(.1)
                print("Ndersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3)) 
                sleep(.1)
                print("Dhe ti ke vetem " + str(sakta) + " numer te sakte") 
                sleep(.1)
                print("Dhe ke fituar $" + str(shumaparave))
                sleep(.1)
            # Printimi i rezultatit kur dy numera jane te sakta
            elif sakta == 2:
                sleep(.1)
                print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3))
                sleep(.1)
                print("Ndersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3))
                sleep(.1)
                print("Dhe ti ke " + str(sakta) + " numera te sakte")
                sleep(.1)
                print("Dhe ke fituar $" + str(shumaparave))
                sleep(.1)
            # Printimi i rezultatit ne qoftese te gjitha numrat jane te sakta
            elif sakta == 3:
                sleep(.1)
                print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3)) 
                sleep(.1)
                print("Ndersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3))
                sleep(.1)
                print("Ju lumte ju keni gjetur " + str(sakta) + " numra te sakte") 
                sleep(.1)
                print("Dhe ju keni fituar $" + str(shumaparave))
                sleep(.1)
            
            # Keto funksione sherbejn per tu kthyer ne menu
            loja = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()
            
        # Loja e hedhjes se gureve
        while loja == 2:
            # Grafiku i lojes se hedhjes se gureve
            print("\n////////////////////////////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                                          /")
            sleep(.1)
            print("/                                                                          /")
            sleep(.1)
            print("/                         Loja e hedhjes se gureve                         /")
            sleep(.1)
            print("/                                                                          /")
            sleep(.1)
            print("/                                                                          /")
            sleep(.1)
            print("////////////////////////////////////////////////////////////////////////////")
            # Numrat e gurit
            min = 1
            max = 6

            # Variabla e Gjuaj Guret
            print('\nShkruani "Po" per tu gjuajtur guret,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur lojen.')
            sleep(.1)
            gjuajguret = input("\nA deshironi te filloni me gjuajtjen e gureve? ")
            gjuajguret = gjuajguret.lower()

            # While ne kete rast perdoret per kur Gjuaj Guret eshte Po
            while gjuajguret == "po":
                # Guri i 1
                g1 = randint(min,max)
                # Guri i 2
                g2 = randint(min,max)
                # Guri i 3
                g3 = randint(min,max)
                # Guri i 4
                g4 = randint(min,max)
                # Printimi i Gureve per lojtarin e 1
                print("\nPo Rrotullohen guret per lojtarin e 1...")
                sleep(1)
                print("\nKeni qelluar...")
                sleep(1)
                print("Guri i pare:",g1)
                sleep(.8)
                print("Guri i dyte:",g2)
                # Printimi i Gureve per lojtarin e 2
                print("\nPo rrotullohen guret per lojtarin e 2...")
                sleep(1)
                print("\nKeni qelluar...")
                sleep(1)
                print("Guri i pare:",g3)
                sleep(1)
                print("Guri i dyte:",g4)

                # Guret per lojtarin e 1
                lojtari1 = g1 + g2
                sleep(1)
                print("\nLojtari 1 ne total ka:", lojtari1)
                # Guret per lojtarin e 2
                lojtari2 = g3 + g4
                sleep(1)
                print("Lojtari 2 ne total ka:", lojtari2)

                # Ky funksion sherben kur guret e lojtarit te 1 jane me te madhenj se guret e lojtarit te 2 
                if lojtari1 > lojtari2:
                    sleep(1)
                    print("\nKa fituar lojtari 1")
                # Ky funksion sherben kur guret e lojtarit te 1 jane me te vegjel se guret e lojtarit te 2 
                elif lojtari1 < lojtari2:
                    sleep(1)
                    print("\nKa fituar lojtari 2")
                # Ky funksion sherben kur guret e 2 lojtareve jane barazim
                else:
                    sleep(1)
                    print("\nRezultati eshte barazim")
                    
                sleep(1)
                print('\nShkruani "Po" per tu gjuajtur perseri,')
                sleep(.1)
                print('Shkruani "Jo" per te mbyllur lojen.')
                sleep(.1)
                gjuajguret = input("\nA deshironi te gjuani perseri? ")
                gjuajguret = gjuajguret.lower()
                
            # Keto funksione sherbejn per tu kthyer ne menu
            if gjuajguret == "jo":
                print('\nShkruani "Po" per tu rikthyer,')
                sleep(.1)
                print('Shkruani "Jo" per te mbyllur programin.')
                sleep(.1)
                loja = 0
                fillimi_i_menys = input("\nA deshironi te ktheheni tek menuja? ")
                fillimi_i_menys = fillimi_i_menys.lower()
        
        # Loja e Gure,Leter & Gershere
        while loja == 3:
            # Grafiku i lojes se Gure,Leter & Gershere
            print("\n//////////////////////////////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                                            /")
            sleep(.1)
            print("/                                                                            /")
            sleep(.1)
            print("/                         Loja e Gure,Leter & Gershere                       /")
            sleep(.1)
            print("/                                                                            /")
            sleep(.1)
            print("/                                                                            /")
            sleep(.1)
            print("//////////////////////////////////////////////////////////////////////////////")
            # Keto sherbejne per te treguar rregullat e lojes
            print("Rregullat e lojes Gure,Leter & Gershere jane keto: \n"
                                +"Gure vs Leter->Fiton ai qe ka zgjedhur Leter \n"
                                + "Gure vs Gershere->Fiton ai qe ka zgjedhur Gur \n"
                                +"Leter vs Gershere->Fiton ai qe ka zgjedhur Gersher \n") 
            
            # Ne kete liste jane te vendosur opcinet e lojes
            lista = ["gure","leter","gershere"]
            
            # Kjo variabel sherben per ti dhene vlere i-se
            i = 1

            # Ky kod eshte funksional vetem kur i eshte me e vogel apo e njejte me 5
            while i <= 5:
                njeriu = input("\nGure, leter apo gershere: ")
                sleep(.1)
                pc = choice(lista)
                njeriu = njeriu.lower()

                # Ky funksion sherben kur eshte shkruar teksti gabim
                while njeriu not in lista:
                    print("\n*****NUK ESHTE SHENUAR MIRE TEKSTI!*****")
                    sleep(.1)
                    njeriu = input("Gure, leter apo gershere: ")
                    njeriu = njeriu.lower()
                    sleep(.1)

                # Ky funksion sherben kur Kompjuteri dhe Perdoruesi kane zjedhur te njejtin opcion    
                while pc == njeriu:
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("*****BARAZIM*****")
                    sleep(.1)
                    njeriu = input("\nGure, leter apo gershere: ")
                    njeriu = njeriu.lower()
                    sleep(.1)
                    pc = choice(lista)
                    i+=1

                # Keto funksione sherbejne kur Kompjuteri dhe Perdoruesi kane zgjedhur opsione te ndryshme
                ## Keto funksione gjithashtu sherbejne per te treguar se a keni humbur apo keni fituar
                if pc == "gershere" and njeriu == "gure":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("Fituat pas heres se ", i)
                    sleep(.1)
                    break
                elif pc == "gershere" and njeriu == "leter":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("*****HUMBE*****")
                    sleep(.1)

                elif pc == "gure" and njeriu == "gershere":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("*****HUMBE*****")
                    sleep(.1)

                elif pc == "gure" and njeriu == "leter":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("Fituat pas heres se ", i)
                    sleep(.1)
                    break
                elif pc == "leter" and njeriu == "gure":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("*****HUMBE*****")
                    sleep(.1)
                elif pc == "leter" and njeriu == "gershere":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("Fituat pas heres se ", i)
                    sleep(.1)
                    break
                
                # Ky funksion sherben kur Perodoruesi ka kaluar limitin e mundesive 
                if i >= 5:
                    print("\nKeni kaluar limit e mundesive, keni pasur vetem", i, "raste.")
                    sleep(.1)
                    break
                i+=1
            # Keto funksione sherbejn per tu kthyer ne menu
            loja = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()
        
        # Ky kod sherben per tu kthyer prapa ne menu
        while loja == 9:
            loja = 0
            menuja = 0
            fillimi_i_menys == "po"
        
        # Ky funksion sherben kur perdoruesi nuk deshiron te kthehet ne menu
        while fillimi_i_menys == "jo":
            loja = 0
            menuja = 0
            print("\nMire u pafshim", perdoruesi)
            sleep(.1)
            break 
    # Menuja e dyte
    while menuja == 2:
        # Menuja e programeve
        print("\n//////////////////////////////////////////////////////////////////////")
        sleep(.1)
        print("/                                                                    /")
        sleep(.1)
        print("/                                                                    /")
        sleep(.1)
        print("/                            Programs Menu                           /")
        sleep(.1)
        print("/                                                                    /")
        sleep(.1)
        print("/                                                                    /")
        sleep(.1)
        print("//////////////////////////////////////////////////////////////////////")
        sleep(.1)
        # Programet ne dispozicion
        print('\nVendos numrin 1 per te perdorur programin e "Kovertimit te gradeve"')
        sleep(.1)
        print('Vendos numrin 2 per te perdorur programin e "Gjetjes se perimetrit"')
        sleep(.1)
        print('Vendos numrin 3 per te perdorur programin e "Gjenerimit te Paswordit"')
        sleep(.1)
        print('Vendos numrin 9 per tu kthyer prapa ne menu')
        sleep(.1)
        # Variabla e Programit
        programi = int(input("\nCilin program deshironi te perdorni? "))
        
        # Fillimi i kodimit te Programeve
        
        # Konvertimi i Gradeve
        while programi == 1:
            # Grafiku i Konvertimit te Gradeve
            print("\n/////////////////////////////////////////////////")
            sleep(.1)
            print("/                                               /")
            sleep(.1)
            print("/                                               /")
            sleep(.1)
            print("/            Konvertimi i Gradeve               /")
            sleep(.1)
            print("/                                               /")
            sleep(.1)
            print("/                                               /")
            sleep(.1)
            print("/////////////////////////////////////////////////")
            sleep(.1)
            # Variabla e gradeve
            grada = int(input("\nSa grade eshte: "))
            # Variabla e shkalles
            shkalla = input("Deshironi ta konvertoni ne C apo F: ")
            # Formula per konvertimin e °F
            F = int((grada * 9/5) + 32)
            # Formula per konvertimin e °C
            C = int((grada - 32) * 5/9)
                    
            # Funksioni i °C
            def konvertimi(grada, shkalla):
                        if shkalla == "c" or "C":
                            return C
            # Funksioi i °F
            def konvertimi2(grada,shkalla):
                        if shkalla == "f" or "F":
                            return F
                    
            # Printimi per °C
            if shkalla == "c" or shkalla == "C":
                        print(grada,"°F","eshte e barabart me", konvertimi(grada,shkalla),"°C")
            # Printimi per °F
            elif shkalla == "f" or shkalla == "F":
                        print(grada,"°C","eshte e barabart me", konvertimi2(grada,shkalla),"°F")
            
            # Keto funksione sherbejn per tu kthyer ne menu
            programi = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()

        # Perimetri
        while programi == 2:
            # Grafiku i perimetrit
            print("\n////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                  /")
            sleep(.1)
            print("/                                                  /")
            sleep(.1)
            print("/              Gjetja e Perimetrit                 /")
            sleep(.1)
            print("/                                                  /")
            sleep(.1)
            print("/                                                  /")
            sleep(.1)
            print("////////////////////////////////////////////////////")
            sleep(.1)
            
            # Variabla e Gjatesise
            a = float(input("\nGjeresia: "))
            sleep(.5)
            
            # Variabla e Gjeresise
            b = float(input("Gjatesia: "))
            sleep(.25)
            
            # Formula e Perimetrit
            P = 2*(a+b)
            
            # Perimetri 
            print("\nPerimetri i kesaj siperfaqe eshte: ", P, "cm")
            sleep(.25)
            
            # Keto funksione sherbejn per tu kthyer ne menu
            programi = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()
        
        # Gjenerimi i Paswordeve
        while programi == 3:
            # Grafiku i Gjenerimit te paswordeve
            print("\n///////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                     /")
            sleep(.1)
            print("/                                                     /")
            sleep(.1)
            print("/              Gjenerimi i Paswordeve                 /")
            sleep(.1)
            print("/                                                     /")
            sleep(.1)
            print("/                                                     /")
            sleep(.1)
            print("///////////////////////////////////////////////////////")
            sleep(.1)
            
            # Ky funksion sherben per te perzier karakteret
            def perziej(shkronja):
                listaezbrazet = list(shkronja)
                shuffle(listaezbrazet)
                return ''.join(listaezbrazet)

            # Keto shkronja,numra & simbole jane marrur bazuar ne kodin ASCII
            # Keto shkronja,numra & simbole jane marrur nga http://www.asciitable.com/
            ## Shkronja te medha
            shtm1 = chr(randint(65,90)) 
            shtm2 = chr(randint(65,90))
            ## Shkronja te vogla
            shtv1 = chr(randint(97,122))
            shtv2 = chr(randint(97,122))
            ## Numra
            nm1 = chr(randint(48,57))
            nm2 = chr(randint(48,57))
            ## Simbole
            si1 = chr(randint(33,47))
            si2 = chr(randint(58,64))

            # Variabla per te treguar se sa password do te printohen
            a = int(input("\nSa Password ju nevojiten?: "))
            sleep(.1)
            
            # Keto printime perdoren per te treguar Perdoruesit sa Karaktere jane ne dispozicion
            print('\nPer 8 Karaktere vendosni numrin 8')
            sleep(.1)
            print('Per 16 karaktere vendosni numrin 16')
            sleep(.1)
            print('Per 24 karaktere vendosni numrin 24')
            sleep(.1)
            print('Per 32 karaktere vendosni numrin 32')
            sleep(.1)
            print('Per 40 karaktere vendosni numrin 40')
            sleep(.1)
            
            # Variabla per te treguar programit se sa karaktere duhet te gjenerohen
            b = int(input("\nSa karakteresh e deshironi Paswordin?: "))

            # Kjo variabel sherben per te i dhene vlere i-se
            i = 1

            # Ky funksion eshte aktiv per aq here sa password ju nevojiten perdoruesit
            ## Ndersa a+1 sherben qe kur te gjenerohen passwordet printimi i tyre te filloj nga 1 dhe jo nga 0
            while i in range(a+1):
                # Ky kod sherben kur shkruhet numri i karaktereve eshte shkruar gabim
                while b != 8 and b != 16 and b != 24 and b != 32 and b != 40:
                    print("\nE keni shkruar gabim, Ju lutemi shkruani numrin perseri.")
                    b = int(input("\nSa karakteresh e deshironi Paswordin?: "))
                
                # Kodi per 8 Karaktere
                if b == 8:
                    password = shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2 
                    password = perziej(password)
                # Kodi per 16 Karaktere
                elif b == 16:
                    password = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*2 
                    password = perziej(password)
                # Kodi per 24 Karaktere
                elif b == 24:
                    password = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*3 
                    password = perziej(password)
                # Kodi per 32 Karaktere
                elif b == 32:
                    password = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*4 
                    password = perziej(password)
                # Kodi per 40 Karaktere
                elif b == 40:
                    password = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*5 
                    password = perziej(password)
                
                # Printimi i Paswordeve
                print("Paswordi i", str(i) + ":", password)
                sleep(.1)
                i+=1
            
            # Keto funksione sherbejn per tu kthyer ne menu
            programi = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()

        # Ky kod sherben per tu kthyer prapa ne menu
        while programi == 9:
            programi = 0
            menuja = 0
            fillimi_i_menys == "po"
    
        # Ky funksion sherben kur perdoruesi nuk deshiron te kthehet ne menu
        while fillimi_i_menys == "jo":
            programi = 0
            menuja = 0
            print("\nMire u pafshim", perdoruesi)
            sleep(.1)
            break 
    

# Keto inpute sherbejn qe kur programi te hapet ne Comand Prompt te Pythonit mos te mbyllet pas perfundimit
input()
input()
input()
