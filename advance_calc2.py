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
    else:   
        return 'Fail invalid option'


n1 = float(input("Ingrese primer valor: "))
n2 = float(input("Ingrese segundo valor: "))

print ("'''MENU CALCULADORA'''")
print("[1] sumar")
print("[2] restar")
print("[3] multiplicar")
print("[4] dividir")
print("[5] dividir")

opc = input("Digite una opción del menu: ")

resltado =calculadora(n1, n2, opc)
print(resltado)
