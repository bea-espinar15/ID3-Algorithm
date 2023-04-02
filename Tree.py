
#
#   CLASE ÁRBOL DE DECISIÓN
#   -----------------------
#   /RELLENAR/
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
