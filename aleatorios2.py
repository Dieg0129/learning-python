#Cree una función Script que genere el lanzamiento de dos dados (1-6) y 
#que muestre por pantalla el mensaje"GANADOR" cuando genere un par, de lo contrario, el mensaje 
#será "Sigue intentando".

#Importo biblioteca para generar números aleatorios de tipo entero
from random import randint

#Lanzar y generar los dos dados con una función
def dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)  

    return dado1, dado2

d = dados()
d1 = d[0]
d2 = d[1]
print("Dados= ", d)
print("Dado 1= ", d1)
print("Dado 2= ", d2)

if (d1 == d2):
    print("Ganaste")
else:
    print("Sigue intentando")


