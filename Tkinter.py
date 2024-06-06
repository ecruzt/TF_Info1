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
    
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Ayuda de funciones")
    
    # Obtener una lista de todas las funciones del módulo funciones
    all_functions = [name for name in dir(funciones) if callable(getattr(funciones, name))]
    
    # Dividir las funciones en tres columnas
    num_cols = 3
    functions_per_col = (len(all_functions) + num_cols - 1) // num_cols
    
    # Crear contenedores para las columnas
    columns = [tk.Frame(root) for _ in range(num_cols)]
    
    # Colocar botones en las columnas
    for i, func_name in enumerate(all_functions):
        col_index = i // functions_per_col
        button = tk.Button(columns[col_index], text=func_name, command=lambda name=func_name: show_help(name))
        button.pack()
    
    # Colocar las columnas en la ventana principal
    for col in columns:
        col.pack(side=tk.LEFT, padx=5)
    
    root.mainloop()
    
# crear_ventana_ayuda()


