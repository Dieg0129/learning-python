'''
Script description: Obtener toda la información acerca de los cometas
'''

import requests
import os

os.system('clear')

def get_comets():
    global count
    print('Comets information')
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    
    #Si o no
    try:
        #Request to API
        response = requests.get(url) #Obtener información de la url
        response.raise_for_status() #Verificamos errores

        #Imprimir todos los nombres de cometas
        datos = response.json()
        count = 0

       # total = int(input("Cantidad de datosa a mostrar: "))
        planet = int(input("Planeta a mostrar "))

        #print(datos["bodies"]) #Los datos es muy extensa, si se extraen algunos si funciona, como bodies
        for cometas in datos["bodies"]:
            #print("English name: ",cometas["englishName"])
            #print(cometas) muestra todo
            #if cometas["isPlanet"] == True: #Valida si es planeta
            if cometas["englishName"] == True:
                print("English name: ",cometas["englishName"])
                print("Moons: ",cometas["moons"])
                print("Gravitiy: ",cometas["gravity"])
                print("Is planet: ",cometas["isPlanet"])
                print("\n")

             #   count += 1

            #if count == total:
                #break

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")


#Call function
get_comets()
#print("Total de datos: ", count)
