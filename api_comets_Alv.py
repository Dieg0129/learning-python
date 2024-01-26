import requests
import os 

os.system('Clear') #Nos limpia pantalla despues de ejecución

def get_comets():
    global count
    print(":::COMETS INFORMATION:::")
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"

    try: #funciona como un if
        #Request to API
        response = requests.get(url) #El get trae la info de la URL
        response.raise_for_status()

         
        data = response.json() #Convierte la salida en formato Json
        #Print all comets names
        #print(data)#Nos imprime todos los datos sin el for de abajo 
        #count = 0
        #total = int(input("Cantidad de datos a mostrar:"))
        planet = input("Escriba el planeta a buscar: ")
        for comet in data['bodies']:
            #if comet["isPlanet"] == True: #Si es planeta nos imprimirá TRUE
            if comet["englishName"] == planet:
                print("English name:", comet["englishName"]) # nos muestra los datos de englishName
                print("moons:", comet["moons"]) # nos muestra los datos de englishName
                print("Gravity:", comet["gravity"]) # nos muestra los datos de englishName
                print("Is planet:", comet["isPlanet"]) # nos muestra los datos de englishName
                print("\n") # nos muestra los datos de englishName
            
            
                '''count += 1
            if count == total:  #Muestra hasta la cantidad de datos que se pone en el input total
                break
        print("El contador es = ", count)'''
    except requests.exceptions.RequestException as e:  #except funciona como un else
        print(f"API ERROR: {e}")
# Llamamos la función 
get_comets()