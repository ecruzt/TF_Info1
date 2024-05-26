import mysql.connector
from mysql.connector import errorcode

#función para validar entradas del usuario
def readUserInput(output, dataType):
    while True:
        user_input = input(output)
        try: 
            result = dataType(user_input)
            break
        except ValueError:
            print(f"Error: '{user_input}' no es un valor válido para {dataType.__name__}. Por favor, intenta de nuevo.")
    return result

#funcion para establecer la conexion y crear la base de datos informatica1
def conectar():
    user = 'informatica1'
    password = "bio123"
    host = 'localhost'
    database_name = "informatica1"
    try:
        # Conectar al servidor MySQL
        cnx = mysql.connector.connect(user=user, password=password, host=host, database=database_name)
        print("Conexión establecida correctamente.")

        return cnx
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error de acceso: Usuario o contraseña incorrectos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"Error: La base de datos '{database_name}' no existe.")
        else:
            print(err)
        return None
    
# Función para inicializar la tabla de usuarios
def crear_tabla_usuarios():
    cnx = conectar()
    if cnx is None:
        print("No se pudo establecer la conexión. No se puede crear la tabla.")
        return
    
    cursor = cnx.cursor()
    try:
        cursor.execute("CREATE TABLE usuarios (_id INT AUTO_INCREMENT PRIMARY KEY, password INT, user VARCHAR(250))")
        print("Tabla 'usuarios' creada correctamente.")

        # Insertar usuarios iniciales
        users = [
            (123, "Peter"),
            (321, "Amy"),
            (456, "Hannah"),
            (436, "Michael"),
            (686, "Sandy"),
            (234, "Betty"),
            (587, "Richard"),
            (686, "Susan")
        ]
        for user in users:
            sql = "INSERT INTO usuarios (password, user) VALUES (%s, %s)"
            cursor.execute(sql, user)
        
        cnx.commit()
        print("Usuarios insertados correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al crear la tabla o insertar datos: {err}")

# Función para validar si un usuario está en la tabla 'usuarios'
def iniciar_sesion():
    try:
        cnx = conectar()  
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM usuarios")
        myresult = cursor.fetchall()
        usuarios = {}
        for x in myresult:
            usuarios[x[0]] = [x[1], x[2]]
        print('''
   (ʘ ͜ʖ ʘ)
Inicie sesión''')

        while True:
            user = readUserInput('Ingrese su usuario: ', str)
            password = readUserInput('Ingrese su contraseña: ', int)  # Cambiado a str para coincidir con el tipo almacenado en la base de datos
            datos = [password, user]

            user_found = False
            for i in usuarios:
                if usuarios[i] == datos:
                    user_found = True
                    return user_found
                    break
            if user_found:
                break
            else:
                print('Usuario o contraseña incorrectos. Intente de nuevo.')
    except Exception as e:
        print("Error: ", e)

#adorno
def adorno(output):
    tamaño = 7
    for i in range(tamaño):
        if i == tamaño - 1:
            print("*" * (2 * i + 1) + output)
        else:
            print("" * (tamaño - i - 1) + "*" * (2 * i + 1))
    for i in range(tamaño - 2, -1, -1):
        print("" * (tamaño - i - 1) + "*" * (2 * i + 1))