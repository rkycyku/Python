

grada = int(input("Sa grade eshte: "))
shkalla = input("Deshironi ta konvertoni ne C apo F: ")

F = int((grada * 9/5) + 32)
C = int((grada - 32) * 5/9)

def konvertimi(grada, shkalla):
    if shkalla == "c" or "C":
        return C
def konvertimi2(grada,shkalla):
    if shkalla == "f" or "F":
        return F


if shkalla == "c" or shkalla == "C":
    print(grada,"°F","eshte e barabart me", konvertimi(grada,shkalla),"°C")
elif shkalla == "f" or shkalla == "F":
    print(grada,"°C","eshte e barabart me", konvertimi2(grada,shkalla),"°F")
