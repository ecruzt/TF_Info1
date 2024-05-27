from utils import *

# Conectar a la base de datos e inicializar la tabla de usuarios
conectar()

# cargar las tablas con algunos valores iniciales
cargar_tablas()

# Mostrar mensaje de inicio
adorno(" Iniciando app farmacos Medellín!")

# Intentar iniciar sesión
Response_iniciar_sesion = iniciar_sesion()
while Response_iniciar_sesion == True:
    print('Bienvedido!')
    break

# Mostrar el menú principal si el inicio de sesión es exitoso
menu1 = """
╔═════════════════════════════════════════╗
║               Menú Principal            ║
╠═════════════════════════════════════════╣
║ Gestionar información de:               ║
║ 1. Medicamentos                         ║
║ 2. Proveedores                          ║
║ 3. Ubicaciones                          ║
║ 4. Salir                                ║
╚═════════════════════════════════════════╝
"""
while True:
    print(menu1)
    try:
        responsemenu1 = readUserInput('Ingrese la opción deseada: ', int)
        if responsemenu1 == 1:
            print("Opción 1 seleccionada: Gestionar información de medicamentos")
            # funcion para gestionar información de medicamentos
            menu_medicamentos()
        elif responsemenu1 == 2:
            print("Opción 2 seleccionada: Gestionar información de proveedores")
            # funcion para gestionar información de proveedores
            menu_proveedores()
        elif responsemenu1 == 3:
            print("Opción 3 seleccionada: Gestionar información de ubicaciones")
            # funcion para gestionar información de ubicaciones
            menu_ubicaciones()
        elif responsemenu1 == 4:
            adorno("Hasta luego!")
            break  # salir del bucle
        else:
            print("Por favor, ingrese una opción válida (1-4)")
    except ValueError:
        print('Ingrese un dato válido')