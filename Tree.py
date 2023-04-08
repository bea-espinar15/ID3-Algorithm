
#
#   CLASE ÁRBOL DE DECISIÓN
#   -----------------------
#   Clase que dibuja el árbol de decisión una vez terminado el algoritmo.
#   Atributos:
#   · root = nodo raíz del árbol a partir del cual lo dibuja
#   · canvas = lienzo sobre el que se dibuja el árbol
#

import Utilities


class Tree:

    # Constructor:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas

    # Métodos privados:

    # Función recursiva:
    # · node = raíz del árbol
    # · pos = posición en la que se debe dibujar la raíz
    # · right = ¿es el hijo derecho? (para pintar el texto a la izq o la dcha del nodo)
    def draw(self, node, pos, right):
        x, y = pos
        num_children = len(node.get_children())
        num = node.get_num()

        # CASO BASE - NODO HOJA
        if num_children == 0:
            # Nodo hoja real
            if node.get_value() == "si" or node.get_value() == "no":
                # Dibujar nodo
                self.canvas.create_oval(x, y, x+50, y+50, outline=Utilities.BLACK, fill=Utilities.WHITE)
                # Escribir nombre de nodo
                if right: self.canvas.create_text(x+50, y-5, text=num, fill=Utilities.BLACK, font=Utilities.FONT_TABLE)
                else: self.canvas.create_text(x, y-5, text=num, fill=Utilities.BLACK, font=Utilities.FONT_TABLE)
                # Darle valor + o - al nodo
                if node.get_value() == "si":
                    self.canvas.create_text(x+25, y+25, text="+", fill=Utilities.GREEN, font=Utilities.FONT_TITLE)
                else:
                    self.canvas.create_text(x+25, y+25, text="-", fill=Utilities.RED, font=Utilities.FONT_TITLE)
            # Algoritmo básico, sólo 1 llamada recursiva
            else:
                # Dibujar nodo
                self.canvas.create_oval(x, y, x+50, y+50, outline=Utilities.BLACK, fill=Utilities.LIGHT_GREEN)
                num = str(num) + ". " + node.get_value()
                # Escribir nombre de nodo
                self.canvas.create_text(x-20, y-10, text=num, fill=Utilities.BLACK, font=Utilities.FONT_TABLE)

        # CASO RECURSIVO
        else:
            # Calcular posiciones de los hijos
            hor_dist = num_children * Utilities.HORIZONTAL_DIST
            new_x = x - (num_children // 2) * hor_dist
            new_y = y + Utilities.VERTICAL_DIST
            # Visitar cada hijo
            for c in node.get_children().keys():
                # Dibujar rama con el valor del atributo
                self.canvas.create_line(x+25, y+25, new_x+25, new_y+25, fill=Utilities.BLACK)
                self.canvas.create_text((x+new_x+50)//2, (y+new_y+50)//2, text=c,  fill=Utilities.BLACK, font=Utilities.FONT_TABLE)
                # Llamada recursiva, dibujar hijo
                if new_x > x: right_new = True
                else: right_new = False
                self.draw(node.get_children()[c], (new_x, new_y), right_new)
                # Calcular pos_x del siguiente hijo
                new_x += hor_dist
                if num_children % 2 == 0 and new_x == x:
                    new_x += hor_dist
            # Dibujar nodo
            self.canvas.create_oval(x, y, x + 50, y + 50, outline=Utilities.BLACK, fill=Utilities.LIGHT_GREEN)
            num = str(num) + ". " + node.get_value()
            # Escribir nombre de nodo
            if right: self.canvas.create_text(x+60, y-10, text=num, fill=Utilities.BLACK, font=Utilities.FONT_TABLE)
            else: self.canvas.create_text(x-20, y-10, text=num, fill=Utilities.BLACK, font=Utilities.FONT_TABLE)

    # Métodos públicos:
    def draw_tree(self):
        self.draw(self.root, (270, 20), False)
