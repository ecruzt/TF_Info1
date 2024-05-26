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

#funcion para inicializar las tablas y/o insertar datos
    # Argumentos:
    #     nombre_tabla (str): El nombre de la tabla a crear.
    #     definicion_columnas (str): La definición de las columnas de la tabla en formato SQL donde se especifique el tipo de dato de cada columna.
    #     datos_iniciales (list of tuples): Una lista de tuplas donde cada tupla representa una fila de datos a insertar.
    #     columnas_insercion (list of str): Una lista de nombres de columnas en las que se insertarán los datos.
def crear_tabla_y_insertar_datos(nombre_tabla, definicion_columnas, datos_iniciales, columnas_insercion):
    cnx = conectar()
    if cnx is None:
        print(f"No se pudo establecer la conexión. No se puede crear la tabla '{nombre_tabla}'.")
        return
    
    cursor = cnx.cursor()
    try:
        # Crear la tabla
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({definicion_columnas})")
        print(f"Tabla '{nombre_tabla}' creada correctamente.")

        # Insertar datos iniciales
        for datos in datos_iniciales:
            placeholders = ', '.join(['%s'] * len(datos))
            sql = f"INSERT INTO {nombre_tabla} ({', '.join(columnas_insercion)}) VALUES ({placeholders})"
            cursor.execute(sql, datos)
        
        cnx.commit()
        print(f"Datos insertados correctamente en la tabla '{nombre_tabla}'.")
    except mysql.connector.Error as err:
        print(f"Error al crear la tabla o insertar datos: {err}")

def cargar_tablas():
    #informacion inicial
    usuarios_definicion = "_id INT AUTO_INCREMENT PRIMARY KEY, password INT, user VARCHAR(250)"
    usuarios_datos = [(123, "Peter"), (321, "Amy"), (456, "Hannah"), (436, "Michael"), (686, "Sandy"), (234, "Betty"), (587, "Richard"), (686, "Susan")]
    usuarios_columnas = ["password", "user"]

    medicamentos_definicion = "lote INT AUTO_INCREMENT PRIMARY KEY, nombre_del_medicamento VARCHAR(250), distribuidor VARCHAR(250), cantidad_en_bodega INT, fecha_de_llegada VARCHAR(250), precio_de_venta INT"
    medicamentos_datos = [('Aspirina', 'Alemana', 5, "20/05/2024", 45000)]
    medicamentos_columnas = ["nombre_del_medicamento", "distribuidor", "cantidad_en_bodega", "fecha_de_llegada", "precio_de_venta"]

    proveedores_deficicion = 'codigo INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(250), apellido VARCHAR(250), documento_de_identidad INT, entidad VARCHAR(250)'
    proveedores_datos = [('Juanito', 'Perez', '467', 'Juridica')]
    proveedores_columnas = ['nombre', 'apellido', 'documento_de_identidad', 'entidad']

    ubicaciones_definicion = '_id INT AUTO_INCREMENT PRIMARY KEY, codigo VARCHAR(250), nombre_de_la_ubicacion VARCHAR(250), telefono INT'
    ubicaciones_datos = [('123abc', 'Barrancabermeja', 350)]
    ubicaciones_columnass = ['codigo', 'nombre_de_la_ubicacion', 'telefono']

    # Crear tablas e insertar datos
    crear_tabla_y_insertar_datos('usuarios', usuarios_definicion, usuarios_datos, usuarios_columnas)
    crear_tabla_y_insertar_datos('medicamentos', medicamentos_definicion, medicamentos_datos, medicamentos_columnas)
    crear_tabla_y_insertar_datos('proveedores', proveedores_deficicion, proveedores_datos, proveedores_columnas)
    crear_tabla_y_insertar_datos('ubicaciones', ubicaciones_definicion, ubicaciones_datos, ubicaciones_columnass)


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
            password = readUserInput('Ingrese su contraseña: ', int)
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