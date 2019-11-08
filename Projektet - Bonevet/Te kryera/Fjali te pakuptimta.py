#Fjali te Pakuptimta

from random import randint
import time

emri = input("Si e ke emrin? ")
time.sleep(1)

print("\nPershendetje", emri, 'eshte koha per te luajtur "Fjali te pakuptimta"')
time.sleep(1)

name = []
verb = []
noun = []

i = 0

here_emra = int(input("Sa emra do te shtoni: "))

while i in range(here_emra):
    emri = input("Vendosni emrin: ")
    name.append(emri)
    i+=1
print("Ju keni shtuar keto emra ne liste:", name)

i = 0
here_folje = int(input("\nSa folje do te shtoni: "))

while i in range(here_folje):
    folje = input("Vendosni foljen: ")
    verb.append(folje)
    i+=1
print("Ju keni shtuar keto emra ne liste:", verb)

i = 0
here_emer = int(input("\nSa emra do te shtoni: "))

while i in range(here_emer):
    emer = input("Vendosni emrin: ")
    noun.append(emer)
    i+=1
print("Ju keni shtuar keto emra ne liste:", noun)

def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked

while True:
    print(pick(name), pick(verb), pick(noun), end='.')
    input()
    