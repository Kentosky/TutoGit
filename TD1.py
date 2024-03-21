import math

DC = int(input("Entrez 1 pour déchiffrement, 2 pour chiffrement\n--> "))
phrase = str(input("Entrez votre mot : "))
p = int(input("Entrez le décallage voulu : "))
final = str()

if DC == 1:
    for i in range(len(phrase)):
        x = ord(phrase[i])
        x = ((((x - 96) + p) % 25) + 96)
        final = final + chr(x)

if DC == 2:
    for i in range(Nb):
        x = ord(input(str("Entrez la lettre à coder\n--> ")))
        x = x - 96
        x = x % 26
        x = x + 96
        x = ((x - p))
        final = final + chr(x)

print("votre mot est : ", final)



