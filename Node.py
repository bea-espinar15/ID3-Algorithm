
#
#   CLASE NODO
#   ----------
#   Un nodo representa el estado del algoritmo en un momento concreto:
#   · num = nº asociado al nodo (para representarlo y distinguirlo al mostrar su info)
#   · attributes = lista de atributos disponibles en ese nivel del árbol
#   · data = tabla (matriz) de valores correspondiente a los <attributes> en ese nivel del árbol
#   · merits = diccionario {atributo:mérito} ORDENADO crecientemente por mérito, con los
#              <attributes> en ese nivel del árbol
#   · value = atributo mejor (con menor mérito) que se elige para expander el nodo
#   · children = diccionario {valor_atributo:nodo} con los hijos del nodo, para cada posible
#                valor del atributo <value>, se genera un nodo hijo con los correspondientes
#                <attributes> y <data>
#

from sortedcontainers import SortedDict


class Node:

    # Constructor:
    def __init__(self, num, attributes, data):
        self.num = num
        self.attributes = attributes
        self.data = data
        self.merits = SortedDict()
        self.value = None
        self.children = {}

    # Getters:
    def get_num(self):
        return self.num

    def get_value(self):
        return self.value

    def get_merits(self):
        return self.merits

    def get_children(self):
        return self.children

    # Setters:
    def set_value(self, value):
        self.value = value

    def set_merits(self, merits):
        self.merits = merits

    def set_children(self, attr, child):
        self.children[attr] = child
