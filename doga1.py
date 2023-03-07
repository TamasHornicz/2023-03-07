import random
import math
#1. feladat

osszeg=int(input("Összeg: "))
ev=int(input("Év: "))
kamat=int(input("Kamat: "))

kamat1 = kamat/100
zárójel = 1+kamat1
négyzet = zárójel**ev
számolás = osszeg*négyzet

print(ev, "év várakozás után ennyi pézed lesz:",round(számolás))
