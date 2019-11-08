from random import randint,shuffle
from time import sleep

def perziej(string):
  tempList = list(string)
  shuffle(tempList)
  return ''.join(tempList)

#Shkronja te medha
shtm1 = chr(randint(65,90))
shtm2 = chr(randint(65,90))
#Shkronja te vogla
shtv1 = chr(randint(97,122))
shtv2 = chr(randint(97,122))
#Numra
nm1 = chr(randint(48,57))
nm2 = chr(randint(48,57))
#Simbole
si1 = chr(randint(33,47))
si2 = chr(randint(58,64))

a = int(input("Sa Password ju nevojiten?: "))
sleep(.1)
print('Per 8 Karaktere vendosni numrin 8')
sleep(.1)
print('Per 16 karaktere vendosni numrin 16')
sleep(.1)
print('Per 24 karaktere vendosni numrin 24')
sleep(.1)
print('Per 32 karaktere vendosni numrin 32')
sleep(.1)
print('Per 40 karaktere vendosni numrin 40')
sleep(.1)
b = int(input("Sa karakteresh e deshironi Paswordin?: "))


i = 1

while i in range(a+1):
  while b != 8 and b != 16 and b != 24 and b != 32 and b != 40:
    print("E keni shkruar gabim, Ju lutemi shkruani numrin perseri.")
    b = int(input("Sa karakteresh e deshironi Paswordin?: "))
  if b == 8:
    password = shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2 
    password = perziej(password)
  elif b == 16:
    ppassword = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*2 
    password = perziej(password)
  elif b == 24:
    password = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*3 
    password = perziej(password)
  elif b == 32:
    password = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*4 
    password = perziej(password)
  elif b == 40:
    password = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*5 
    password = perziej(password)
  while b != 8:
    print("E keni shkruar gabim, Ju lutemi shkruani numrin perseri.")
    b = int(input("Sa karakteresh e deshironi Paswordin?: "))

  print("Paswordi i", str(i) + ":", password)
  sleep(.1)
  i+=1

