import mysql.connector
from mysql.connector import errorcode

def crear_base_de_datos():
    '''
    Description:
        Función para crear la base de datos 'informatica1' en el servidor local MySQL, si aún no existe.

    parameters:
        - output: str (mensaje para informar si la base de datos fue creada o ya existía)

    return:
        - None
    '''
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="informatica1",
            password="bio123"
        )

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS informatica1")
        print("Base de datos 'informatica1' creada o ya existía.")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error de acceso: Usuario o contraseña incorrectos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: La base de datos no existe.")
        else:
            print(err)

## Función para validar entradas del usuario
def readUserInput(output, dataType):
    '''
    Description:
        Función para validar las entradas del usuario.

    parameters:
        - output: str (mensaje para solicitar la entrada del usuario)
        - dataType: type (tipo de dato esperado para la entrada del usuario)

    return:
        - result: dataType (entrada del usuario convertida al tipo de dato especificado)
    '''
    while True:
        user_input = input(output)
        try: 
            result = dataType(user_input)
            break
        except ValueError:
            print(f"Error: '{user_input}' no es un valor válido para {dataType.__name__}. Por favor, intenta de nuevo.")
    return result

## Función para establecer la conexión y crear la base de datos informatica1
def conectar():
    '''
    Description:
        Función para establecer la conexión y crear la base de datos 'informatica1' en el servidor MySQL.

    return:
        - cnx: connection object (objeto de conexión si la conexión se establece correctamente, de lo contrario, None)
    '''
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


def crear_tabla_y_insertar_datos(nombre_tabla, definicion_columnas, datos_iniciales, columnas_insercion):
    '''
    Description:
        Función para crear una tabla y/o insertar datos en la base de datos 'informatica1'.

    parameters:
        - nombre_tabla: str (nombre de la tabla a crear)
        - definicion_columnas: str (definición de las columnas de la tabla en formato SQL)
        - datos_iniciales: list of tuples (lista de tuplas representando filas de datos a insertar)
        - columnas_insercion: list of str (lista de nombres de columnas donde se insertarán los datos)

    return:
        - None
    '''
    cnx = conectar()
    if cnx is None:
        print(f"No se pudo establecer la conexión. No se puede crear la tabla '{nombre_tabla}'.")
        return
    
    cursor = cnx.cursor()
    try:
        # Crear la tabla
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({definicion_columnas})")
        print(f"Tabla '{nombre_tabla}' creada correctamente.")

        # Verificar si ya existen datos iniciales en la tabla
        cursor.execute(f"SELECT COUNT(*) FROM {nombre_tabla}") #cuenta las filas en una tabla
        count = cursor.fetchone()[0] #recupera la primera fila
        
        if count == 0:
            # Insertar datos iniciales solo si la tabla está vacía
            for datos in datos_iniciales:
                placeholders = ', '.join(['%s'] * len(datos))
                sql = f"INSERT INTO {nombre_tabla} ({', '.join(columnas_insercion)}) VALUES ({placeholders})"
                cursor.execute(sql, datos)
            
            cnx.commit()
            print(f"Datos insertados correctamente en la tabla '{nombre_tabla}'.")
        else:
            print(f"La tabla '{nombre_tabla}' ya contiene datos. No se insertaron datos adicionales.")
    except mysql.connector.Error as err:
        print(f"Error al crear la tabla o insertar datos: {err}")

def cargar_tablas():
    '''
    Description:
        Función para cargar las tablas 'usuarios', 'medicamentos', 'proveedores', 'ubicaciones' con datos iniciales.

    return:
        - None
    '''
    # Información inicial
    # Definiciones de tablas y columnas para usuarios
    usuarios_definicion = """
    _id INT AUTO_INCREMENT PRIMARY KEY,
    password INT,
    user VARCHAR(250)
    """
    usuarios_datos = [
        (123, "Peter"),
        (321, "Amy"),
        (456, "Hannah"),
        (436, "Michael"),
        (686, "Sandy"),
        (234, "Betty"),
        (587, "Richard"),
        (686, "Susan")
    ]
    usuarios_columnas = ["password", "user"]

    # Definiciones de tablas y columnas para medicamentos
    medicamentos_definicion = """
    lote INT AUTO_INCREMENT PRIMARY KEY,
    nombre_del_medicamento VARCHAR(250),
    distribuidor VARCHAR(250),
    cantidad_en_bodega INT,
    fecha_de_llegada VARCHAR(250),
    precio_de_venta INT,
    proveedor_por_codigo INT,
    ubicacion_por_id INT
    """
    medicamentos_datos = [
        ('Aspirina', 'Alemana', 5, f'{obtener_fecha_y_hora_actual()}', 45000, 1, 1)
    ]
    medicamentos_columnas = [
        "nombre_del_medicamento",
        "distribuidor",
        "cantidad_en_bodega",
        "fecha_de_llegada",
        "precio_de_venta",
        'proveedor_por_codigo',
        'ubicacion_por_id'
    ]

    # Definiciones de tablas y columnas para proveedores
    proveedores_definicion = """
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(250),
    apellido VARCHAR(250),
    documento_de_identidad INT,
    entidad VARCHAR(250),
    ubicacion_por_id INT,
    medicamento_por_lote INT
    """
    proveedores_datos = [('Pepa', 'Perez', 467, 'Juridica', 1, 1)]
    proveedores_columnas = [
        'nombre',
        'apellido',
        'documento_de_identidad',
        'entidad',
        'ubicacion_por_id',
        'medicamento_por_lote'
    ]

    # Definiciones de tablas y columnas para ubicaciones
    ubicaciones_definicion = """
    _id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(250),
    nombre_de_la_ubicacion VARCHAR(250),
    telefono INT,
    proveedor_por_codigo INT,
    medicamento_por_lote INT
    """
    ubicaciones_datos = [('123abc', 'Barrancabermeja', 350, 1, 1)]
    ubicaciones_columnas = [
        'codigo',
        'nombre_de_la_ubicacion',
        'telefono',
        'proveedor_por_codigo',
        'medicamento_por_lote'
    ]

    # Crear tablas e insertar datos
    crear_tabla_y_insertar_datos('usuarios', usuarios_definicion, usuarios_datos, usuarios_columnas)
    crear_tabla_y_insertar_datos('medicamentos', medicamentos_definicion, medicamentos_datos, medicamentos_columnas)
    crear_tabla_y_insertar_datos('proveedores', proveedores_definicion, proveedores_datos, proveedores_columnas)
    crear_tabla_y_insertar_datos('ubicaciones', ubicaciones_definicion, ubicaciones_datos, ubicaciones_columnas)

import mysql.connector

def obtener_encabezado(tabla):
    # Conexión a la base de datos MySQL
    conexion =  conectar()    

    # Cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Consulta para obtener el encabezado de la tabla
    consulta = f"SHOW COLUMNS FROM {tabla};"
    
    # Ejecutar la consulta
    cursor.execute(consulta)
    
    # Obtener los resultados y guardar los nombres de las columnas en una lista
    encabezado = [columna[0] for columna in cursor.fetchall()]
    
    # Cerrar cursor y conexión
    cursor.close()
    conexion.close()
    
    return encabezado

def obtener_valores_columna(tabla, columna):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # Consultar los valores de la columna en la tabla
        sql = f"SELECT {columna} FROM {tabla}"
        cursor.execute(sql)

        # Obtener los resultados y guardar los valores en una lista
        valores = [fila[0] for fila in cursor.fetchall()]

        return valores

    except mysql.connector.Error as error:
        print(f"Error al obtener los valores de la columna: {error}")

def validar_columna(lista):
    """
    Solicita al usuario que ingrese un valor presente en la lista proporcionada.
    
    La función continúa solicitando la entrada del usuario hasta que éste ingrese un valor válido,
    es decir, un valor que esté contenido en la lista. Si el valor ingresado no está en la lista,
    se le indicará al usuario que intente nuevamente.
    
    Parámetros:
    lista (list): Una lista de valores válidos que el usuario puede ingresar.
    """
    while True:
        valor = readUserInput(f"Ingrese un dato a modificar {lista}: ", str)
        if valor in lista:
            print(f"Valor {valor} aceptado.")
            x = valor
            return x
        else:
            print(f"Valor no válido. Intente nuevamente.")
        

# Función para validar si un usuario está en la tabla 'usuarios'
def iniciar_sesion():
    '''
    Description:
        Función para iniciar sesión de usuario.

    return:
        - user_found: bool (True si el usuario se encontró y la contraseña es correcta, de lo contrario, False)
    '''
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

# Función para añadir datos
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

def obtener_fecha_y_hora_actual():
    '''
    Descripción:
        Función para obtener la fecha y hora actuales en formato "DD/MM/YYYY HH:MM:SS".

    Parámetros:
        - Ninguno

    Retorno:
        - str: Fecha y hora actuales en formato "DD/MM/YYYY HH:MM:SS"
    '''
    from datetime import datetime
    # Obtener la fecha y hora actuales
    fecha_y_hora_actual = datetime.now()
    # Formatear la fecha y hora en "DD/MM/YYYY HH:MM:SS"
    fecha_y_hora_formateada = fecha_y_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return fecha_y_hora_formateada

def validador_value(table_name, column_name, ask):
    '''
    Description:
        Función para iniciar sesión de usuario.

    parameters:
        - table_name: str (nombre de la tabla que contiene los datos de inicio de sesión)
        - column_name: str (nombre de la columna que contiene los datos de inicio de sesión)
        - ask: str (nombre de lo que se solicita)

    return:
        - user_found: bool (True si el usuario se encontró y la contraseña es correcta, de lo contrario, False)
    '''
    try:
        cnx = conectar()  
        cursor = cnx.cursor()

        toma = f"SELECT {column_name} FROM {table_name}"
        cursor.execute(toma)
        resultados = cursor.fetchall()
        column_data = [resultado[0] for resultado in resultados]
        while True:
            input_data = readUserInput(f'Asigne un {ask} por {column_name}: ', int)

            if input_data in column_data:
                return input_data
            else:
                print('Dato incorrecto. Intente de nuevo.')

    except Exception as e:
        print("Error: ", e)
        return False
    

    
def actualizar_tabla(tabla, primary_key):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # Mostrar todos los datos de la tabla
        mostrar_datos_tabla(tabla)

        # Solicitar el valor de la clave primaria
        valor_primaria = readUserInput(f"Ingrese la fila de {primary_key} a modificar: ", int)
        primary_keys = obtener_valores_columna(tabla, primary_key)
        while True:
            if valor_primaria in primary_keys:
                print(f"Valor {valor_primaria} aceptado.")
                break
            else:
                print(f"Valor no válido. Intente nuevamente.")
                valor_primaria = readUserInput(f"Ingrese la fila de {primary_key} a modificar: ", int)


        # Solicitar el nombre de la columna a actualizar
        encabezadoForUpdate = readUserInput("Ingrese el nombre de la columna a actualizar: ", str)
        encabezados = obtener_encabezado(tabla)
        while True:
            if encabezadoForUpdate == primary_key:  # Verificar si la columna a actualizar es la clave primaria
                print("La clave primaria no puede ser modificada.")
                encabezadoForUpdate = readUserInput("Ingrese el nombre de la columna a actualizar: ", str)
                
            elif encabezadoForUpdate in encabezados:
                print(f"Valor {valor_primaria} aceptado.")
                break
            else:
                print(f"Valor no válido. Intente nuevamente.")
                encabezadoForUpdate = readUserInput("Ingrese el nombre de la columna a actualizar: ", str)
        
        # Solicitar el nuevo valor utilizando la funcion pedir_datos_para_insercion()
        nuevo_valor = pedir_datos_para_insercion([encabezadoForUpdate])[0]

        # Actualizar la tabla
        sql = f"UPDATE {tabla} SET {encabezadoForUpdate} = '{nuevo_valor}' WHERE {primary_key} = '{valor_primaria}'"
        cursor.execute(sql)
        conexion.commit()
        print("Tabla actualizada exitosamente.")

    except mysql.connector.Error as error:
        print(f"Error al actualizar los valores: {error}")







# Función que pregunta por datos y los almacena en una lista de tuplas
def pedir_datos_para_insercion(columnas):
    '''
    Descripción:
        Función para solicitar datos de entrada al usuario para insertar en una tabla de la base de datos. Dependiendo del nombre de la columna, la función solicitará el tipo de dato apropiado y, en algunos casos, mostrará las tablas relacionadas para que el usuario seleccione el valor correspondiente.

    Parámetros:
        - columnas: list of str (lista de nombres de columnas para las que se solicitarán los datos)

    Retorno:
        - tuple: tupla de valores introducidos por el usuario, uno por cada columna

    Funcionamiento:
        - Para columnas que contienen "cantidad_en_bodega", "precio", "documento_de_identidad" o "telefono", se solicitará un valor entero.
        - Para columnas que contienen "fecha", se usa la funcion que pone la fecha actual.
        - Para columnas que contienen "proveedor_por_codigo", "ubicacion_por_id" o "medicamento_por_lote", se mostrará la tabla correspondiente y se solicitará un valor entero.
        - Para todas las demás columnas, se solicitará una cadena de texto.
    '''
    datos = []
    for columna in columnas:
        if "cantidad_en_bodega" in columna or "precio" in columna or 'documento_de_identidad' in columna or "telefono" in columna:
            valor = readUserInput(f"Ingrese {columna}: ", int)
        elif "fecha" in columna:
            valor = obtener_fecha_y_hora_actual()
        elif 'proveedor_por_codigo' in columna:
            mostrar_datos_tabla('proveedores')
            valor = validador_value('proveedores', 'codigo', 'proveedor')
        elif "ubicacion_por_id" in columna:
            mostrar_datos_tabla('ubicaciones')
            valor = validador_value('ubicaciones', '_id', 'ubicacion')
        elif 'medicamento_por_lote' in columna:
            mostrar_datos_tabla('medicamentos')
            valor = validador_value('medicamentos', 'lote', 'medicamento')
        else:
            valor = readUserInput(f"Ingrese {columna}: ", str)
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

def mostrar_datos_tabla(nombre_tabla):
    '''
    Description:
        Función para mostrar todos los valores de una tabla de manera organizada y centrada.

    parameters:
        - nombre_tabla: str (nombre de la tabla a mostrar)

    return:
        - None
    '''
    cnx = conectar()
    if cnx is None:
        print(f"No se pudo establecer la conexión. No se puede mostrar la tabla '{nombre_tabla}'.")
        return
    
    cursor = cnx.cursor()
    try:
        cursor.execute(f"SELECT * FROM {nombre_tabla}")
        rows = cursor.fetchall()
        
        if rows:
            # Obtener nombres de las columnas
            column_names = [i[0] for i in cursor.description]
            
            # Calcular anchos de columna
            column_ancho = []
            for name in column_names:
                column_ancho.append(len(name))
            for row in rows:
                for i, cell in enumerate(row):
                    column_ancho[i] = max(column_ancho[i], len(str(cell)))
            
            # Imprimir cabeceras de columna
            header = ""
            for i, name in enumerate(column_names):
                header += name.center(column_ancho[i]) + " | "
            print(header.strip())
            print("─" * len(header))
            
            # Imprimir filas
            for row in rows:
                row_data = ""
                for i, cell in enumerate(row):
                    cell_str = str(cell)
                    space = (column_ancho[i] - len(cell_str)) // 2
                    row_data += " " * space + cell_str + " " * (column_ancho[i] - len(cell_str) - space) + " | "
                print(row_data.strip())
        else:
            print(f"La tabla '{nombre_tabla}' está vacía o no existe.")
    except mysql.connector.Error as err:
        print(f"Error al mostrar los datos de la tabla '{nombre_tabla}': {err}")

# Adorno
def adorno(output):
    '''
    Description
    parameters:
        - output: tipo de dato

    return 
       - None 
    '''
    tamaño = 5
    for i in range(tamaño):
        if i == tamaño - 1:
            print("*" * (2 * i + 1) + output)
        else:
            print("" * (tamaño - i - 1) + "*" * (2 * i + 1))
    for i in range(tamaño - 2, -1, -1):
        print("" * (tamaño - i - 1) + "*" * (2 * i + 1))

