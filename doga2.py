import random
import math

tipp= input("Fej(1) vagy Írás(2): ")
erme=str(random.randint(1, 3))
for i in tipp:
    if tipp==erme :
        print("Nyertél!")
    elif tipp!=erme:
        print("Vesztettél! :c")
print("Bizonyíték hogy jó-e: ",erme)