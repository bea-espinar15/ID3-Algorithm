
#
#   CLASE ÁRBOL DE DECISIÓN
#   -----------------------
#   Clase que dibuja el árbol de decisión una vez terminado el algoritmo
#   · root = nodo raíz del árbol a partir del cual lo dibuja
#

import tkinter as tk

import Utilities


class Tree:

    # Constructor:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas

    # Métodos privados:
    def draw(self, node, pos):
        x, y = pos
        num_children = len(node.get_children())
        num = node.get_num()

        # CASO BASE - NODO HOJA
        if num_children == 0:
            if node.get_value() == "si" or node.get_value() == "no":
                self.canvas.create_oval(x, y, x + 50, y + 50, outline=Utilities.BLACK, fill=Utilities.WHITE)
                self.canvas.create_text(x, y, text=num, fill=Utilities.BLACK, font=Utilities.FONT_TABLE)
                if node.get_value() == "si":
                    self.canvas.create_text(x+25, y+25, text="+", fill=Utilities.GREEN, font=Utilities.FONT_TITLE)
                else:
                    self.canvas.create_text(x + 25, y + 25, text="-", fill=Utilities.RED, font=Utilities.FONT_TITLE)
            else:
                self.canvas.create_oval(x, y, x+50, y+50, outline=Utilities.BLACK, fill=Utilities.LIGHT_GREEN)
                num = str(num) + ". " + node.get_value()
                self.canvas.create_text(x-20, y-10, text=num, fill=Utilities.BLACK, font=Utilities.FONT_TABLE)

        # CASO RECURSIVO
        else:
            # Calcular posiciones de los hijos
            new_x = x - (num_children // 2) * Utilities.HORIZONTAL_DIST
            new_y = y + Utilities.VERTICAL_DIST
            for c in node.get_children().keys():
                self.canvas.create_line(x+25, y+25, new_x+25, new_y+25, fill=Utilities.BLACK)
                self.canvas.create_text((x+new_x+50)//2, (y+new_y+50)//2, text=c,  fill=Utilities.BLACK, font=Utilities.FONT_TABLE)
                self.draw(node.get_children()[c], (new_x, new_y))
                new_x += Utilities.HORIZONTAL_DIST
                if num_children % 2 == 0 and new_x == x:
                    new_x += Utilities.HORIZONTAL_DIST
            self.canvas.create_oval(x, y, x + 50, y + 50, outline=Utilities.BLACK, fill=Utilities.LIGHT_GREEN)
            num = str(num) + ". " + node.get_value()
            self.canvas.create_text(x-20, y-10, text=num, fill=Utilities.BLACK, font=Utilities.FONT_TABLE)

    # Métodos públicos:
    def draw_tree(self):
        self.draw(self.root, (270, 20))

    def print(self, node):
        print(node.value)
        for c in node.get_children().keys():
            self.print(node.get_children()[c])

    def print_tree(self):
        self.print(self.root)
