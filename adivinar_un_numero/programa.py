# escoger un numero aleatorio

from random import random

import random
print("-----------------------")
print("----adivina el numero--")
print("-----------------------")

#output
pc=random.randint(0,10)

print("La computadora ya ha escogido un numero ahora usted")
n=int(input("digite un numero del 1 al 10 : "))

#processing
while(pc!=n ):
    
    if(pc>n):
        print("el numero que escogio la computadora es mayor que  " + str (n))
    else:
        print("el numero que escogio la computadora es menor que " + str (n))
    n=int(input("digite un numero del 1 al 10 : "))
    
print ("la computadora eligio el numero " + str (pc) )
    

