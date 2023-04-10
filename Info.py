
#
#   CLASE INFO DEL ALGORITMO
#   ------------------------
#   Clase que imprime la información del algoritmo según se va
#   ejecutando. Tiene como atributo el frame donde se imprime
#

import tkinter as tk
import Utilities
from Table import Table


class Info:

    # Constructor:
    def __init__(self, frame):
        self.frame = frame

    # Métodos públicos:

    # Imprime la lista de cada nodo con su mérito
    def draw_list(self, num, merits):
        empty_frame = tk.Frame(self.frame, height=15, bg=self.frame["bg"])
        empty_frame.pack(side=tk.TOP, fill=tk.X)
        # Crear frame
        title_frame = tk.Frame(self.frame, bg=self.frame["bg"])
        title_frame.pack(side=tk.TOP, fill=tk.X)
        # Añadir título
        title = str(num) + ". Nodos - Mérito"
        title_label = tk.Label(title_frame, text=title, font=Utilities.FONT_TABLE)
        title_label.config(highlightthickness=0, bd=0, bg=title_frame["bg"])
        title_label.pack(side=tk.LEFT, fill=tk.X, pady=3)
        # Crear lista nodo-mérito
        list_merits = ""
        for attr in merits.keys():
            list_merits += str(attr) + ": " + "{:.2f}".format(round(merits[attr], 2)) + "; "
        list_merits = list_merits[:-2]
        # Añadir lista
        list_frame = tk.Frame(self.frame, bg=self.frame["bg"])
        list_frame.pack(side=tk.TOP, fill=tk.X)
        list_label = tk.Label(list_frame, text=list_merits, font=Utilities.FONT_TABLE, wraplength=440, justify="left")
        list_label.config(highlightthickness=0, bd=0, bg=list_frame["bg"])
        list_label.pack(side=tk.LEFT, pady=1)

    # Imprime la tabla de datos para un nodo
    def draw_table(self, attr, attributes, data):
        empty_frame = tk.Frame(self.frame, height=10, bg=self.frame["bg"])
        empty_frame.pack(side=tk.TOP, fill=tk.X)
        # Crear frame
        title_frame = tk.Frame(self.frame, bg=self.frame["bg"])
        title_frame.pack(side=tk.TOP, fill=tk.X)
        # Añadir título
        title = (str(attr)).upper() + ". Tabla al quitar el atributo"
        title_label = tk.Label(title_frame, text=title, font=Utilities.FONT_TABLE)
        title_label.config(highlightthickness=0, bd=0, bg=title_frame["bg"])
        title_label.pack(side=tk.LEFT, pady=3)
        # Añadir tabla
        table_frame = tk.Frame(self.frame, bg=self.frame["bg"])
        table_frame.configure(borderwidth=1, relief="solid")
        table_frame.pack(side=tk.TOP, anchor=tk.W)
        Table(attributes, data, table_frame)

    # Imprime cuando se ha llegado a un nodo hoja
    def draw_text(self, num, pos):
        empty_frame = tk.Frame(self.frame, height=15, bg=self.frame["bg"])
        empty_frame.pack(side=tk.TOP, fill=tk.X)
        # Crear frame
        text_frame = tk.Frame(self.frame, bg=self.frame["bg"])
        text_frame.pack(side=tk.TOP, fill=tk.X)
        # Añadir texto al frame
        text = str(num) + ". Todos los ejemplares son \""
        if pos: text += "si\""
        else: text += "no\""
        text_label = tk.Label(text_frame, text=text, font=Utilities.FONT_TABLE)
        text_label.config(highlightthickness=0, bd=0, bg=text_frame["bg"])
        text_label.pack(side=tk.LEFT, pady=3)
