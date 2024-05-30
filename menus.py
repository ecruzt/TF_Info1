import mysql.connector
from mysql.connector import errorcode
from funciones import *

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
        nombre_tabla = 'medicamentos'
        primary_Key = 'lote'
        if option == 1:
            columnas_insercion = ["nombre_del_medicamento", "distribuidor", "cantidad_en_bodega", 'fecha_de_llegada', "precio_de_venta", 'proveedor_por_codigo', 'ubicacion_por_id']
            gestionar_añadir_info(nombre_tabla, columnas_insercion)
        elif option == 2:
            actualizar_tabla(nombre_tabla, primary_Key)
        elif option == 3:
            # Implementar la lógica para buscar un medicamento
            print("Buscar un medicamento")
        elif option == 4:
            mostrar_datos_tabla(nombre_tabla)
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
        nombre_tabla = 'proveedores'
        primary_key = 'codigo'
        if option == 1:
            columnas_insercion = ["nombre", "apellido", "documento_de_identidad", 'entidad', 'ubicacion_por_id', 'medicamento_por_lote']
            gestionar_añadir_info(nombre_tabla, columnas_insercion)
        elif option == 2:
            actualizar_tabla(nombre_tabla, primary_key)
        elif option == 3:
            # Implementar la lógica para buscar un proveedor
            print("Buscar un proveedor")
        elif option == 4:
            mostrar_datos_tabla(nombre_tabla)
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
        nombre_tabla = 'ubicaciones'
        primary_key = '_id'
        if option == 1:
            nombre_tabla = 'ubicaciones'
            columnas_insercion = ["codigo", "nombre_de_la_ubicacion", "telefono", 'proveedor_por_codigo', 'medicamento_por_lote']
            gestionar_añadir_info(nombre_tabla, columnas_insercion)
        elif option == 2:
            actualizar_tabla(nombre_tabla, primary_key)
        elif option == 3:
            # Implementar la lógica para buscar una ubicación
            print("Buscar una ubicación")
        elif option == 4:
            mostrar_datos_tabla(nombre_tabla)
        elif option == 5:
            # Implementar la lógica para eliminar una ubicación
            print("Eliminar una ubicación")
        elif option == 6:
            print("Volviendo al menú principal...")
            break
        else:
            print("Por favor, ingrese una opción válida (1-6)")
