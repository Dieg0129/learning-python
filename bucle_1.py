'''
Bucle loop, repetir una acción N veces, iteraciones (cantidad de ejecuciones)
Contadores (cuenta o incrementa)
Acumuladores (Acumulación de valores. Sumar valores)
Contar valores es diferente de sumar valores


Contador: c = c + k -> k es una constante
cont = cont + 1 / cont++ / cont+=1

Acumulador: a = a + v -> v es una variable (num, salario, edad, temperaturas, etc)
acum = acum + num / acum+=num
'''

#Bucle para imprimir los números del 1 al 10 en pantalla

def lista_numeros():
    incr = 1
    while incr <= 10: #Mientras incre sea menor o igual a 10
        print (incr)
        incr += 1

    print ("Valor de incremento al romperse el bucle: ", incr)

lista_numeros()


    