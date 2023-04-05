
#
#   CLASE TABLA
#   -----------
#   /RELLENAR/
#


import tkinter as tk

import Utilities


class Table:

    def __init__(self, attributes_input, data_input, table_frame):
        self.attributes = attributes_input
        self.data = data_input
        self.frame = table_frame
        self.init_gui()

    def init_gui(self):
        rows = len(self.data)
        cols = len(self.attributes)

        # Pintar nombres de los atributos
        for j in range(cols):
            e = tk.Entry(self.frame, width=11, font=Utilities.font_table, bg=Utilities.LIGHT_GREEN)
            e.grid(row=0, column=j)
            e.insert(tk.END, self.attributes[j])

        # Pintar valores de la tabla
        for i in range(rows - 1):
            for j in range(cols):
                e = tk.Entry(self.frame, width=11, fg='black', font=Utilities.font_table)
                e.grid(row=i+1, column=j)
                e.insert(tk.END, self.data[i+1][j])
