'''
API: Application programing interface (interfaz de programación de aplicaciones)
Nasa API: https://api.nasa.gov/
API_KEY_NASA: uaaYcUPdlwQboTwc27Zw1flKQFeox5HIoOUgGnhX
https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key=uaaYcUPdlwQboTwc27Zw1flKQFeox5HIoOUgGnhX
Reveloper: Diego Puchana
Date: 24012024
Script description: Get and read data from NASA API about comets
'''


#Importar librerias de terceros
'''
Estás son las bibliotecas de Python Request: https://pypi.org/project/requests/
Listar en Python los paquetes instalados mediante consola:
pip freeze, pip list
Instalar paquetes:
pip install requests
Documentar en un archivo plano los requeriments:
pip freeze > requirements.txt
pip install open-cv-plus     -> Permite instalar cv plus
pip install math22  -> Paquete de matematicas
Instalar los paquetes de requeriments:
pip install -r requeriments.txt
'''
import requests

def get_comet_data(api_key): #obtener información del cometa
    print("Información del cometa")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}" #Convertir a cadena

    #Mostrar errores si no funciona
    try:
        #Realizar la solicitud a la API
        response=requests.get(url)
        response.raise_for_status() #Valida si se presento algún error en la petición
        #Convertir la respuesta de la nasa a fomato JSON (JS Object Nation)
        datos = response.json()

        #print(datos)
        print(f"comet name: {datos['name']}") #Nombre del cometa
        print(f"Maginitud absoluta: {datos['absolute_magnitude_h']}") 
        print(f"Diametro maximo estimado (KM): {datos['estimated_diameter']['kilometers']['estimated_diameter_min']}")
    except requests.exceptions.RequestException as e: #Si genera un erro, mostar en pantalla
        print(f"Error al realizar la petición a la API de la Nasa {e}") #e es error

api_key_nasa = 'uaaYcUPdlwQboTwc27Zw1flKQFeox5HIoOUgGnhX'
get_comet_data(api_key_nasa)



