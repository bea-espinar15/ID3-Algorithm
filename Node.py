
#
#   CLASE NODO
#   ----------
#   /RELLENAR/
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
