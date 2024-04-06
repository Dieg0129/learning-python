
#Import engine database package
import sqlite3

#Create a database connnection (Database name)
con = sqlite3.connect('school.db')

#Creating cursor object by conection => Let us execute sql commands or operations (Query)
cur = con.cursor()

#Create users table
cur.execute('''
    CREATE TABLE IF NOT EXISTS Country (
        id_country INTEGER PRIMARY KEY, 
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        deleted_at DATETIME DEFAULT NULL
            
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Department (
        id_department  INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        id_country INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        deleted_at DATETIME DEFAULT NULL,  
        FOREIGN KEY (id_country) REFERENCES Country(id_country)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS City (
        id_exp_City INTEGER PRIMARY KEY, 
        name VARCHAR(50) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(100) NOT NULL,
        id_department INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        deleted_at DATETIME DEFAULT NULL,
        FOREIGN KEY (id_department) REFERENCES Department(id_department)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Identification_types (
        id_ident_type INTEGER PRIMARY KEY, 
        name VARCHAR(50) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(100) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        deleted_at DATETIME DEFAULT NULL
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Persons (
        id_persons INTEGER PRIMARY KEY, 
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        id_ident_type INTEGER,
        ident_number VARCHAR(15) NOT NULL,
        id_exp_city INTEGER,
        address VARCHAR(150) NOT NULL,
        mobile VARCHAR(50) NOT NULL,
        id_users INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        deleted_at DATETIME DEFAULT NULL,
        FOREIGN KEY (id_ident_type) REFERENCES Identification_type(id_ident_type),
        FOREIGN KEY (id_exp_City) REFERENCES City(id_exp_City),
        FOREIGN KEY (id_users) REFERENCES Users(id_users)
                
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id_students INTEGER PRIMARY KEY, 
        code VARCHAR(50) NOT NULL,
        id_persons INTEGER,
        status BOOLEAN NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        deleted_at DATETIME DEFAULT NULL,
        FOREIGN KEY (id_persons) REFERENCES Persons(id_persons)
            
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id_users INTEGER PRIMARY KEY,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(250) NOT NULL,
        status BOOLEAN NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        deleted_at DATETIME DEFAULT NULL
            
    )
''')

#Execute SQL (Query)
#cur.execute(user_table)

#Save changes in database => Push to database
con.commit()

#print("::: Database market has been created :::")

#Close connection
#con.close()