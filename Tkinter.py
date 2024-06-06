import tkinter as tk
from tkinter import messagebox
import funciones  # Importa tus funciones desde el archivo funciones.py

def crear_ventana_ayuda():
    """
    Crea una ventana con botones para cada función en el módulo `funciones`.
    Al hacer clic en un botón, se muestra la ayuda de la función correspondiente.

    Return:
        None
    """
    def show_help(func_name):
        """
        Muestra la ayuda para una función seleccionada.

        Parámetros:
            func_name (str): El nombre de la función seleccionada.

        Return:
            None
        """
        try:
            func = getattr(funciones, func_name)  # Obtiene la función desde el módulo
            help_text = help(func)
            messagebox.showinfo("Ayuda para " + func_name, help_text)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener ayuda para {func_name}: {str(e)}")
    
    def regresar_menu_principal():
        """
        Cierra la ventana de ayuda y regresa al menú principal.

        Return:
            None
        """
        root.destroy()
    
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Ayuda de funciones")
    root.configure(bg='pale green')  # Fondo verde pastel

    # Ajustar el tamaño de la ventana
    root.geometry("800x600")  # Aumentar el tamaño del recuadro principal
    
    # Crear el encabezado
    header = tk.Label(root, text="Help() funciones en el programa", bg='pale green', font=('Helvetica', 16, 'bold'))
    header.pack(pady=20)
    
    # Crear un marco para contener los botones de funciones
    frame_botones = tk.Frame(root, bg='pale green')
    frame_botones.pack(expand=True, fill=tk.BOTH)
    
    # Obtener una lista de todas las funciones del módulo funciones
    all_functions = [name for name in dir(funciones) if callable(getattr(funciones, name))]
    
    # Dividir las funciones en tres columnas
    num_cols = 3
    functions_per_col = (len(all_functions) + num_cols - 1) // num_cols
    
    # Crear contenedores para las columnas
    columns = [tk.Frame(frame_botones, bg='pale green') for _ in range(num_cols)]
    
    # Colocar botones en las columnas
    for i, func_name in enumerate(all_functions):
        col_index = i // functions_per_col
        button = tk.Button(columns[col_index], text=func_name, command=lambda name=func_name: show_help(name), bg='pink')
        button.pack(pady=5)
    
    # Colocar las columnas en el marco de botones
    for col in columns:
        col.pack(side=tk.LEFT, padx=5, pady=5)

    # Botón para regresar al menú principal en la parte inferior
    btn_regresar = tk.Button(root, text="Regresar al menú principal", command=regresar_menu_principal, bg='pink')
    btn_regresar.pack(side=tk.BOTTOM, pady=20)
    
    root.mainloop()
