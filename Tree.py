
#
#   CLASE ÁRBOL DE DECISIÓN
#   -----------------------
#   Clase que dibuja el árbol de decisión una vez terminado el algoritmo
#   · root = nodo raíz del árbol a partir del cual lo dibuja
#

class Tree:

    # Constructor:
    def __init__(self, root):
        self.root = root

    # Métodos privados:
    def draw(self, node):
        # node.draw()
        for c in node.get_children().keys():
            # node.draw_line(c)
            self.draw(node.get_children()[c])

    # Métodos públicos:
    def draw_tree(self):
        self.draw(self.root)
