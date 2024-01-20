#Tipos de datos en Python
#Python es un lenguaje dinámicamente tipado, es decir, al declarar una variable 
#no es obligatorio especificar su tipo
#Python es un lenguaje interpretado

#1. Numéricos
#Enteros Z (int)
num1 = 42
print("Num1 es tipo:", type(num1))
#Flotantes o decimales R (float)
num2 = 50.5
print("Num2 es tipo:", type(num2))
#Complejos (complex)
num3 = 2j
print("Num3 es tipo:", type(num3))

#2. Cadena (string)
name = "Diego"
print("My_name es tipo:", type(name))
my_lastname = 'Puchana'
print(name, my_lastname)
print("My_lastname es tipo:", type(my_lastname))
profile = '''Diego es una persona enfocada
            en el trabajo de equipos.'''
print("Profile es tipo:", type(profile))

#3. Lógicos (Valores o expresionaes boleanas)
usuario_activo =True
print("Usuario activo es tipo:", type(usuario_activo))
pago_realizado = False
print("Pago realizado es tipo:", type(pago_realizado))

#4. Listas
frutas = ['Apple', 'Banana']
print("Frutas: ", type(frutas))
print(frutas)
colores = ['Green', 'Yellow', 'Black']
print("Colores: ", type(colores))
print(colores)

##Posición de la lista:
print("Colores: ", type(colores[2]))

#5. Tuplas
#6. Diccionarios
#7. Conjuntos