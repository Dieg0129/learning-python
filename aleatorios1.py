from random import randint, uniform 
#Randint, genera números aleatorios enteros
#Uniform, genera números aleatorios con décimales

import os #Librería del sistema operativo que hace parte de Python al instalarla
os.system('clear')#Limpiar consola

n1 = randint(1,100)
n2 = uniform(1,100)#numero flotante

print(n1)
print(n2)

os.system('ls') #Listar