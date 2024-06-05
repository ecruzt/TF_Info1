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
    """
    Inserta datos en una tabla específica de una base de datos MySQL.

    Parámetros:
        nombre_tabla (str): El nombre de la tabla donde se insertarán los datos.
        datos_iniciales (list): Una lista de tuplas, donde cada tupla contiene los datos a insertar en la tabla.
        columnas_insercion (list): Una lista de cadenas que especifican las columnas en las que se insertarán los datos.

    Return:
        None
    """

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

def eliminar_fila(tabla, primary_key):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        # Mostrar todos los datos de la tabla
        mostrar_datos_tabla(tabla)

        # Solicitar el valor de la clave primaria
        valor_primaria = readUserInput(f"Ingrese la fila de {primary_key} a eliminar: ", int)
        primary_keys = obtener_valores_columna(tabla, primary_key)
        while True:
            if valor_primaria in primary_keys:
                print(f"Valor {valor_primaria} aceptado.")
                break
            else:
                print(f"Valor no válido. Intente nuevamente.")
                valor_primaria = readUserInput(f"Ingrese la fila de {primary_key} a eliminar: ", int)

        # Eliminar la fila
        sql = f"DELETE FROM {tabla} WHERE {primary_key} = '{valor_primaria}'"
        cursor.execute(sql)
        conexion.commit()
        print("Fila eliminada exitosamente.")

    except mysql.connector.Error as error:
        print(f"Error al eliminar la fila: {error}")

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
            if nombre_tabla == 'medicamentos':
                #comparar proveedores repetidos de la tabla medicamentos para agregar su respectivo medicamento a tabla proveedores
                comparacion = diccionarios_pk_value('medicamentos', 'proveedor_por_codigo', 'lote')
                lote_clonar, lote_codigo = key_mayor_valor_repetido(comparacion)
                if lote_clonar is not None:
                    valores = valores_por_primary_key("proveedores", "codigo", lote_codigo[lote_clonar])
                    valores['medicamento_por_lote'] = lote_clonar
                    columnas, datos_iniciales = manipular_datos_para_insercion(valores)
                    insertar_datos('proveedores', datos_iniciales, columnas)

                #comparar ubicaciones repetidos de la tabla medicamentos para agregar su respectivo medicamento a tabla medicamentos
                comparacion = diccionarios_pk_value('medicamentos', 'ubicacion_por_id', 'lote')
                lote_clonar, lote_codigo = key_mayor_valor_repetido(comparacion)
                if lote_clonar is not None:
                    valores = valores_por_primary_key("ubicaciones", "_id", lote_codigo[lote_clonar])
                    valores['medicamento_por_lote'] = lote_clonar
                    columnas, datos_iniciales = manipular_datos_para_insercion(valores)
                    insertar_datos('ubicaciones', datos_iniciales, columnas)

            elif nombre_tabla == 'proveedores':
                #comparar ubicaciones repetidas de la tabla proveedores para agregar su respectivo ubicacion a tabla ubicaciones
                comparacion = diccionarios_pk_value('proveedores', 'ubicacion_por_id', 'codigo')
                lote_clonar, lote_codigo = key_mayor_valor_repetido(comparacion)
                if lote_clonar is not None:
                    valores = valores_por_primary_key("ubicaciones", "_id", lote_codigo[lote_clonar])
                    valores["proveedor_por_codigo"] = lote_clonar
                    columnas, datos_iniciales = manipular_datos_para_insercion(valores)
                    insertar_datos('ubicaciones', datos_iniciales, columnas)

                #comparar medicamentos repetidos de la tabla proveedores para agregar su respectivo proveedor a tabla medicamentos
                comparacion = diccionarios_pk_value('proveedores', 'medicamento_por_lote', 'codigo')
                lote_clonar, lote_codigo = key_mayor_valor_repetido(comparacion)
                if lote_clonar is not None:
                    valores = valores_por_primary_key("medicamentos", "lote", lote_codigo[lote_clonar])
                    valores['proveedor_por_codigo'] = lote_clonar
                    columnas, datos_iniciales = manipular_datos_para_insercion(valores)
                    insertar_datos('medicamentos', datos_iniciales, columnas)

            elif nombre_tabla == 'ubicaciones':
                #comparar proveedores repetidas de la tabla ubicaciones para agregar su respectivo ubicacion a tabla proveedores
                comparacion = diccionarios_pk_value('ubicaciones', 'proveedor_por_codigo', '_id')
                lote_clonar, lote_codigo = key_mayor_valor_repetido(comparacion)
                if lote_clonar is not None:
                    valores = valores_por_primary_key("proveedores", "codigo", lote_codigo[lote_clonar])
                    valores["ubicacion_por_id"] = lote_clonar
                    columnas, datos_iniciales = manipular_datos_para_insercion(valores)
                    insertar_datos('proveedores', datos_iniciales, columnas)

                #comparar medicamentos repetidos de la tabla ubicaciones para agregar su respectiva ubicacion a tabla medicamentos
                comparacion = diccionarios_pk_value('ubicaciones', 'medicamento_por_lote', '_id')
                lote_clonar, lote_codigo = key_mayor_valor_repetido(comparacion)
                if lote_clonar is not None:
                    valores = valores_por_primary_key("medicamentos", "lote", lote_codigo[lote_clonar])
                    valores['ubicacion_por_id'] = lote_clonar
                    columnas, datos_iniciales = manipular_datos_para_insercion(valores)
                    insertar_datos('medicamentos', datos_iniciales, columnas)
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


def diccionarios_pk_value(nombre_tabla, nombre_columna, columna_pk):
    """
    Conecta a una base de datos MySQL, recupera los valores de una columna específica y 
    devuelve esos valores en un diccionario donde las claves son los valores de la columna 
    de clave primaria.

    Parámetros:
    nombre_tabla (str): El nombre de la tabla de la cual se desean obtener los datos.
    nombre_columna (str): El nombre de la columna cuyos valores se desean obtener.
    columna_pk (str): El nombre de la columna de clave primaria que se usará como clave en el diccionario.

    Retorna:
    dict: Un diccionario donde las claves son los valores de la columna de clave primaria y 
          los valores son los valores de la columna especificada.
    """

    try:
        # Conectar a la base de datos MySQL
        conn = conectar()
        
        if conn.is_connected():
            cursor = conn.cursor()

            # Obtener los valores de la columna especificada junto con la clave primaria
            query = f"SELECT {columna_pk}, {nombre_columna} FROM {nombre_tabla}"
            cursor.execute(query)
            
            # Recuperar los resultados
            resultados = cursor.fetchall()
            
            # Convertir los resultados en un diccionario
            valores_columna = {fila[0]: fila[1] for fila in resultados}
            
            return valores_columna
    
    except errorcode as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def key_mayor_valor_repetido(diccionario):
    """
    Revisa un diccionario para encontrar valores repetidos y retorna la clave mayor entre aquellas que tienen
    el mismo valor, junto con un diccionario que contiene las claves mayores y sus respectivos valores repetidos.

    Parámetros:
    diccionario (dict): El diccionario a evaluar, con formato {key: value}.

    Retorna:
    tuple: Una tupla que contiene la clave mayor entre aquellas que tienen valores repetidos
           y un diccionario que contiene las claves mayores y sus respectivos valores repetidos.
    """

    # Crear un diccionario para contar las ocurrencias de cada valor
    conteo_valores = {}
    for key, value in diccionario.items():
        if value in conteo_valores:
            conteo_valores[value].append(key)
        else:
            conteo_valores[value] = [key]

    # Revisar los valores repetidos y encontrar la clave mayor entre ellos
    keys_mayores = {}
    for valor, keys in conteo_valores.items():
        if len(keys) > 1:  # Si hay más de una key para el mismo valor
            key_mayor = max(keys)
            keys_mayores[key_mayor] = valor

    # Retornar la clave mayor y el diccionario de claves mayores y sus valores repetidos
    clave_mayor = max(keys_mayores.keys()) if keys_mayores else None
    return clave_mayor, keys_mayores

def valores_por_primary_key(nombre_tabla, columna_pk, valor_pk):
    """
    Obtiene los valores de una fila específica en una tabla de una base de datos MySQL
    utilizando su clave primaria, y los almacena en un diccionario donde la clave
    es el nombre de la columna y el valor es el valor específico de esa columna.

    Parámetros:
    nombre_tabla (str): El nombre de la tabla de la cual se obtendrán los datos.
    columna_pk (str): El nombre de la columna de clave primaria.
    valor_pk: El valor de la clave primaria de la fila que se desea obtener.

    Retorna:
    dict: Un diccionario donde las claves son los nombres de las columnas (excluyendo la clave primaria)
          y los valores son los valores específicos de esas columnas para la fila seleccionada.
    """

    try:
        # Conectar a la base de datos MySQL
        conn = conectar()
        
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)

            # Construir y ejecutar la consulta SQL para obtener la fila deseada
            query = f"SELECT * FROM {nombre_tabla} WHERE {columna_pk} = %s"
            cursor.execute(query, (valor_pk,))
            
            # Recuperar el resultado (debería ser solo una fila)
            resultado = cursor.fetchone()

            # Verificar si se encontró la fila y retornar un diccionario con los valores
            if resultado:
                # Eliminar la clave primaria del diccionario
                resultado.pop(columna_pk, None)
                return resultado
            else:
                print(f"No se encontró la fila con {columna_pk} = {valor_pk}.")
                return None
    
    except:
        print(f"Error al conectar a la base de datos o al ejecutar la consulta")
        return None
    
def manipular_datos_para_insercion(diccionario):
    """
    Manipula un diccionario de datos para que sea compatible con la función insertar_datos.

    Parámetros:
    diccionario (dict): Un diccionario con los datos a manipular.

    Retorna:
    tuple: Una tupla de dos elementos, donde el primer elemento es una lista de las columnas
           de inserción y el segundo elemento es una lista de tuplas con los datos iniciales
           para insertar en la base de datos.
    """

    columnas = list(diccionario.keys())
    datos_iniciales = [tuple(diccionario.values())]
    return columnas, datos_iniciales



# comparacion = diccionarios_pk_value('medicamentos', 'proveedor_por_codigo', 'lote')
# lote_clonar, lote_codigo = key_mayor_valor_repetido(comparacion)
# if lote_clonar is not None:
#     valores = valores_por_primary_key("proveedores", "codigo", lote_codigo[lote_clonar])
#     valores['medicamento_por_lote'] = lote_clonar
#     columnas, datos_iniciales = manipular_datos_para_insercion(valores)
#     insertar_datos('proveedores', datos_iniciales, columnas)
