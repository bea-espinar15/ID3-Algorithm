
#
#   CLASE TABLA
#   -----------
#   Clase que dibuja la tabla de datos de entrada. Atributos:
#   · attributes = lista de atributos (nombres de las columnas)
#   · data = matriz de datos de la tabla
#   · frame = frame en el que se dibuja la tabla
#


import tkinter as tk
import Utilities


class Table:

    # Constructor:
    def __init__(self, attributes_input, data_input, table_frame):
        self.attributes = attributes_input
        self.data = data_input
        self.frame = table_frame
        self.init_gui()

    # Métodos privados:

    # Dibuja la tabla
    def init_gui(self):
        rows = len(self.data)
        cols = len(self.attributes)

        # Ajustar anchura columnas
        self.frame.grid_columnconfigure(0, minsize=120)
        self.frame.grid_columnconfigure(1, minsize=100)

        # Pintar nombres de los atributos
        for j in range(cols):
            e = tk.Entry(self.frame, width=11, font=Utilities.FONT_ATTRIBUTES, bg=Utilities.LIGHT_GREEN, justify=tk.CENTER)
            e.grid(row=0, column=j, sticky="nsew")
            e.insert(tk.END, self.attributes[j])

        # Pintar valores de la tabla
        for i in range(rows - 1):
            for j in range(cols):
                e = tk.Entry(self.frame, width=11, fg='black', font=Utilities.FONT_TABLE, justify=tk.CENTER)
                e.grid(row=i+1, column=j, sticky="nsew")
                e.insert(tk.END, self.data[i+1][j])
