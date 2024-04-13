from flask import Flask, render_template, request, url_for, redirect


app= Flask(__name__) #Se inicializa la aplicación

@app.before_request #Acciones antes de ejecutar una peticion
def before_request():
    print("Antes de la peticion...")

@app.after_request #Acciones despues de ejecutar una peticion
def after_request(response):
    print("Despues de la peticion")
    return response

@app.route('/')
def index():
    #return "Hola" 
    cursos = ['Php', 'Python', 'Java', 'Kotlin']
    data ={
        'titulo': 'Index',
        'bienvenida': 'Saludos!',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template('index.html', data = data) #Retornar una plantilla html

@app.route('/contacto/<nombre>/<int:edad>') #Significa que tendra un parametro
def contacto(nombre, edad):
    data ={
        'titulo': 'contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data = data)

def query_string():
    print(request) #La solicitud que se hace
    print(request.args)
    print(request.args.get('param1'))
    return "OK"

def pagina_no_encontrada(error):
    #return render_template('404.html'), 404
    return redirect(url_for('index')) #Redirecciona a otra pagina
    

if __name__ == '__main__': #Si esta desde el main, entonces se corre el pograma
    app.add_url_rule('/query_string', view_func=query_string) #Indica que se pasara unos parametros con esa url
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)