'''Calculadora que reciba dos números y realice la operación que desee'''


import os

os.system('clear')

def calculadora(x, y, z):
    if z == '1':
        return  x+y    
    elif z == '2':
        return x-y
    elif z == '3':
        return  x*y
    elif z == '4':
        if y == 0:
            return 'No es posible dividir entre cero'
        else:
            return x/y
    elif z == '5':
        if y == 0:
            div ='No es posible dividir entre cero'
            suma = x+y 
            resta = x-y 
            mult = x*y
        else:
            suma = x+y 
            resta = x-y 
            mult = x*y
            div = x/y
        return suma, resta, mult, div 
    else:   
        return 'Fail invalid option'


n1 = float(input("Ingrese primer valor: "))
n2 = float(input("Ingrese segundo valor: "))

print ("'''MENU CALCULADORA'''")
print("[1] sumar")
print("[2] restar")
print("[3] multiplicar")
print("[4] dividir")
print("[5] todos")

opc = input("Digite una opción del menu: ")

if opc == '5':
    resltado =calculadora(n1, n2, opc)
    sum=resltado[0]
    rest=resltado[1] 
    mul=resltado[2]
    divi=resltado[3]
    print("La suma de", n1, "+", n2, "es:", sum)
    print("La resta de", n1, "-", n2, "es:", rest)
    print("La multiplicación de", n1, "*", n2, "es:", mul)
    print("La división de", n1, "/", n2, "es:", divi)
else:
    resltado =calculadora(n1, n2, opc)
    print(resltado)




