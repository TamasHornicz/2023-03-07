import random
import math

atmero= int(input("Írja be a kör átmérőjét: "))
pi = math.pi
r=atmero/2
terulete= round(r*r*pi, 2)
print("Területe: ", terulete)

kerulete= round(2*r*pi, 2)
print("Kerülete: ", kerulete)