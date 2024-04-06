from school_db import con, cur, sqlite3
import os

status_menu = True
global status_op

def create_country(op):
    os.system('clear')

    name = input("Ingrese el nombre del país: ")
    abrev = input("Ingrese la abreviatura del país: ")
    descrip = input("Ingrese la descripción del país: ")
    cur.execute("INSERT INTO Country (name, abrev, descrip) VALUES (?, ?, ?)",
                (name, abrev, descrip))
    con.commit()
    print("Registro de país creado con éxito.")

    os.system('pause')
    menu()

def create_department(op):
    os.system('clear')

    name = input("Ingrese el nombre del departamento: ")
    abrev = input("Ingrese la abreviatura del departamento: ")
    descrip = input("Ingrese la descripción del departamento: ")

    cur.execute("SELECT * from Country")
    print(cur.fetchall())
    id_country = input("Ingrese el ID del país al que pertenece el departamento: ")
    
    cur.execute("INSERT INTO Department (name, abrev, descrip, id_country) VALUES (?, ?, ?, ?)",
                (name, abrev, descrip, id_country))
    con.commit()
    print("Registro de departamento creado con éxito.")

    os.system('pause')
    menu()

def create_City(op):
    os.system('clear')

    name = input("Ingrese el nombre de la ciudad: ")
    abrev = input("Ingrese la abreviatura de la ciudad: ")
    descrip = input("Ingrese la descripción de la ciudad: ")
    cur.execute("SELECT * from Department")
    print(cur.fetchall())
    id_department = input("Ingrese el ID del departamento al que pertenece la ciudad: ")
    cur.execute("INSERT INTO City (name, abrev, descrip, id_department) VALUES (?, ?, ?, ?)",
                (name, abrev, descrip, id_department))
    con.commit()
    print("Registro de ciudad creado con éxito.")

    os.system('pause')
    menu()

def create_identification_types(op):
    os.system('clear')

    name = input("Ingrese el nombre del tipo de identificación: ")
    abrev = input("Ingrese la abreviatura del tipo de identificación: ")
    descrip = input("Ingrese la descripción del tipo de identificación: ")
    cur.execute("INSERT INTO identification_types (name, abrev, descrip) VALUES (?, ?, ?)",
                (name, abrev, descrip))
    con.commit()
    print("Registro de tipo de identificación creado con éxito.")

    os.system('pause')
    menu()

def create_persons(op):
    os.system('clear')

    first_name = input("Ingrese el primer nombre de la persona: ")
    last_name = input("Ingrese el apellido de la persona: ")
    
    cur.execute("SELECT * from Identification_types")
    print(cur.fetchall())
    id_ident_type = input ("Seleccione el tipo de documento:")
        
    ident_number = input("Ingrese el número de identificación de la persona: ")
    
    cur.execute("SELECT * from City")
    print(cur.fetchall())
    id_exp_city = input ("Seleccione su ciudad de origen:")
    
    
    address = input("Ingrese la dirección de la persona: ")
    mobile = input("Ingrese el número de móvil de la persona: ")
    cur.execute("INSERT INTO persons (first_name, last_name, ident_number, address, mobile, id_ident_type, id_exp_city) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (first_name, last_name, ident_number, address, mobile, id_ident_type, id_exp_city))
    con.commit()
    print("Registro de persona creado con éxito.")

    os.system('pause')
    menu()

def create_students(op):
    os.system('clear')

    code = input("Ingrese el código del estudiante: ")
    cur.execute("INSERT INTO students (code) VALUES (?)",
                (code,))
    con.commit()
    print("Registro de estudiante creado con éxito.")

    os.system('pause')
    menu()

def create_users(op):
    os.system('clear')

    email = input("Ingrese el correo electrónico del usuario: ")
    password = input("Ingrese la contraseña del usuario: ")

    cur.execute("INSERT INTO users (email, password) VALUES (?, ?)",
                (email, password))
    con.commit()
    print("Registro de usuario creado con éxito.")

    os.system('pause')
    menu()

def menu():
    global opt
    status_opt = True
    while status_menu: 
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: MAIN MENU ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. Create Country")
        print("[2]. Create Department")
        print("[3]. Create City")
        print("[4]. Create Identification Type")
        print("[5]. Create Person")
        print("[6]. Create Student")
        print("[7]. Create User")
        print("[8]. Exit")
        
        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '8':
                print(".:::::: Invalid option, try again.")
            else :
                status_opt = False

        if opt == '1':
            create_country(opt)
        elif opt == '2':
            create_department(opt)
        elif opt == '3':
            create_City(opt)
        elif opt == '4':
            create_identification_types(opt)
        elif opt == '5':
            create_persons(opt)
        elif opt == '6':
            create_students(opt)
        elif opt == '7':
            create_users(opt)       
        else: 
            print("::: Gracias por ingresar :::")
            exit()
    
#Call main menu
menu()

#Close connection
con.close()