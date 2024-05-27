import mysql.connector
from mysql.connector import errorcode

## Función para validar entradas del usuario
def readUserInput(output, dataType):
    while True:
        user_input = input(output)
        try: 
            result = dataType(user_input)
            break
        except ValueError:
            print(f"Error: '{user_input}' no es un valor válido para {dataType.__name__}. Por favor, intenta de nuevo.")
    return result

## funcion para establecer la conexion y crear la base de datos informatica1
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

## Funcion para inicializar las tablas y/o insertar datos
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

# funcion para añadir datos
def insertar_datos(nombre_tabla, datos_iniciales, columnas_insercion):
    cnx = conectar()
    if cnx is None:
        print(f"No se pudo establecer la conexión. No se pueden insertar datos en la tabla '{nombre_tabla}'.")
        return
    
    cursor = cnx.cursor()
    try:
        # Insertar datos iniciales
        for datos in datos_iniciales:
            placeholders = ', '.join(['%s'] * len(datos))
            sql = f"INSERT INTO {nombre_tabla} ({', '.join(columnas_insercion)}) VALUES ({placeholders})"
            cursor.execute(sql, datos)
        
        cnx.commit()
        print(f"Datos insertados correctamente en la tabla '{nombre_tabla}'.")
    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")
        
#funcion que pregunta por datos y los almacena en una lista de tupla
def pedir_datos_para_insercion(columnas):
    datos = []
    for columna in columnas:
        if "cantidad_en_bodega" in columna or "precio" in columna or 'documento_de_identidad' in columna or "telefono" in columna:
            valor = readUserInput(f"Ingrese el valor para {columna}: ", int)
        elif "fecha" in columna:
            valor = readUserInput(f"Ingrese el valor para {columna} (formato DD/MM/YYYY): ", str)
        else:
            valor = readUserInput(f"Ingrese el valor para {columna}: ", str)
        datos.append(valor)
    return tuple(datos)

def gestionar_añadir_info(nombre_tabla, columnas_insercion):
    while True:
        print(f"\nGestionando información de {nombre_tabla.capitalize()}")
        print("1. Ingresar un nuevo dato")
        print("2. Volver al menú anterior")
        opcion = readUserInput("Ingrese la opción deseada: ", int)
        
        if opcion == 1:
            datos = pedir_datos_para_insercion(columnas_insercion)
            insertar_datos(nombre_tabla, [datos], columnas_insercion)
        elif opcion == 2:
            print("Volviendo al menú anterior...")
            break
        else:
            print("Por favor, ingrese una opción válida (1-2)")

def menu_medicamentos():
    menu = """
    ╔════════════════════════════════════════════╗
    ║            Gestión de Medicamentos         ║
    ╠════════════════════════════════════════════╣
    ║ 1. Ingresar un nuevo medicamento           ║
    ║ 2. Actualizar información de medicamento   ║
    ║ 3. Buscar un medicamento                   ║
    ║ 4. Ver todos los medicamentos              ║
    ║ 5. Eliminar un medicamento                 ║
    ║ 6. Volver al menú principal                ║
    ╚════════════════════════════════════════════╝
    """    
    while True:
        print(menu)
        option = readUserInput('Ingrese la opción deseada: ', int)
        
        if option == 1:
            nombre_tabla = 'medicamentos'
            columnas_insercion = ["nombre_del_medicamento", "distribuidor", "cantidad_en_bodega", 'fecha_de_llegada', "precio_de_venta"]
            gestionar_añadir_info(nombre_tabla, columnas_insercion)
        elif option == 2:
            # Implementar la lógica para actualizar información de un medicamento
            print("Actualizar información de un medicamento")
        elif option == 3:
            # Implementar la lógica para buscar un medicamento
            print("Buscar un medicamento")
        elif option == 4:
            # Implementar la lógica para ver todos los medicamentos
            print("Ver todos los medicamentos")
        elif option == 5:
            # Implementar la lógica para eliminar un medicamento
            print("Eliminar un medicamento")
        elif option == 6:
            print("Volviendo al menú principal...")
            break
        else:
            print("Por favor, ingrese una opción válida (1-6)")

def menu_proveedores():
    menu = """
    ╔════════════════════════════════════════════╗
    ║            Gestión de Proveedores          ║
    ╠════════════════════════════════════════════╣
    ║ 1. Ingresar un nuevo proveedor             ║
    ║ 2. Actualizar información de proveedor     ║
    ║ 3. Buscar un proveedor                     ║
    ║ 4. Ver todos los proveedores               ║
    ║ 5. Eliminar un proveedor                   ║
    ║ 6. Volver al menú principal                ║
    ╚════════════════════════════════════════════╝
    """    
    while True:
        print(menu)
        option = readUserInput('Ingrese la opción deseada: ', int)
        
        if option == 1:
            nombre_tabla = 'proveedores'
            columnas_insercion = ["nombre", "apellido", "documento_de_identidad", 'entidad']
            gestionar_añadir_info(nombre_tabla, columnas_insercion)
        elif option == 2:
            # Implementar la lógica para actualizar información de un proveedor
            print("Actualizar información de un proveedor")
        elif option == 3:
            # Implementar la lógica para buscar un proveedor
            print("Buscar un proveedor")
        elif option == 4:
            # Implementar la lógica para ver todos los proveedores
            print("Ver todos los proveedores")
        elif option == 5:
            # Implementar la lógica para eliminar un proveedor
            print("Eliminar un proveedor")
        elif option == 6:
            print("Volviendo al menú principal...")
            break
        else:
            print("Por favor, ingrese una opción válida (1-6)")

def menu_ubicaciones():
    menu = """
    ╔════════════════════════════════════════════╗
    ║            Gestión de Ubicaciones          ║
    ╠════════════════════════════════════════════╣
    ║ 1. Ingresar una nueva ubicación            ║
    ║ 2. Actualizar información de ubicación     ║
    ║ 3. Buscar una ubicación                    ║
    ║ 4. Ver todas las ubicaciones               ║
    ║ 5. Eliminar una ubicación                  ║
    ║ 6. Volver al menú principal                ║
    ╚════════════════════════════════════════════╝
    """    
    while True:
        print(menu)
        option = readUserInput('Ingrese la opción deseada: ', int)
        
        if option == 1:
            nombre_tabla = 'ubicaciones'
            columnas_insercion = ["codigo", "nombre_de_la_ubicacion", "telefono"]
            gestionar_añadir_info(nombre_tabla, columnas_insercion)
        elif option == 2:
            # Implementar la lógica para actualizar información de una ubicación
            print("Actualizar información de una ubicación")
        elif option == 3:
            # Implementar la lógica para buscar una ubicación
            print("Buscar una ubicación")
        elif option == 4:
            # Implementar la lógica para ver todas las ubicaciones
            print("Ver todas las ubicaciones")
        elif option == 5:
            # Implementar la lógica para eliminar una ubicación
            print("Eliminar una ubicación")
        elif option == 6:
            print("Volviendo al menú principal...")
            break
        else:
            print("Por favor, ingrese una opción válida (1-6)")
        
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