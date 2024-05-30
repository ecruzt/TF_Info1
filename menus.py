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
        if option == 1:
            columnas_insercion = ["nombre_del_medicamento", "distribuidor", "cantidad_en_bodega", 'fecha_de_llegada', "precio_de_venta", 'proveedor_por_codigo', 'ubicacion_por_id']
            gestionar_añadir_info(nombre_tabla, columnas_insercion)
        elif option == 2:
            # Nombre de la tabla y columnas para actualización y validación
            columna_id = 'lote'
            mostrar_datos_tabla('medicamentos')
            valor_id = validador_value('medicamentos', 'lote', 'medicamento')
            encabezados = obtener_encabezado(nombre_tabla)
            columna_a_actualizar = validar_columna(encabezados)
            solicitud = input(f'Ingrese nuevo valor para {columna_a_actualizar}: ')

            # Actualizar el valor en la columna especificada de la fila especificada
            actualizar_valor(nombre_tabla, columna_id, valor_id, columna_a_actualizar, solicitud)

            print("Actualizar información de un medicamento")
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
        if option == 1:
            columnas_insercion = ["nombre", "apellido", "documento_de_identidad", 'entidad', 'ubicacion_por_id', 'medicamento_por_lote']
            gestionar_añadir_info(nombre_tabla, columnas_insercion)
        elif option == 2:
            # Implementar la lógica para actualizar información de un proveedor
            print("Actualizar información de un proveedor")
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
        if option == 1:
            nombre_tabla = 'ubicaciones'
            columnas_insercion = ["codigo", "nombre_de_la_ubicacion", "telefono", 'proveedor_por_codigo', 'medicamento_por_lote']
            gestionar_añadir_info(nombre_tabla, columnas_insercion)
        elif option == 2:
            # Implementar la lógica para actualizar información de una ubicación
            print("Actualizar información de una ubicación")
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
