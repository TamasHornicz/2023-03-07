import random
import math

szam = int(input("Szám: "))

gyök = math.sqrt(szam)
if int(gyök + 0.5) ** 2 == szam:
    print("A",szam, "Négyzetgyökös szám")
else:
    print("A",szam, "Nem négyzetgyökös szám")
