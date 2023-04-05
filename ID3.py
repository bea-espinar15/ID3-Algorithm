
#
#   CLASE ALGORITMO ID3
#   -------------------
#   /RELLENAR/
#

import math
import numpy as np
from sortedcontainers import SortedDict
from Node import Node


class ID3:

    # Constructor:
    def __init__(self, attributes_input, data_input):
        self.num = 1
        self.attributes_input = attributes_input
        self.data_input = data_input
        self.decision = attributes_input.index("Jugar")

    # Métodos privados:
    @staticmethod
    def infor(p, n):
        return (-p * math.log(p, 2)) - (n * math.log(n, 2))

    def calculate_merits(self, attributes, data):

        # Inicializamos variables:

        merits = SortedDict()
        # Número de ejemplares:
        n_total = data.shape[0]

        for i in range(len(attributes) - 1):
            # Obtenemos los valores que toma el atributo i
            values = np.unique(data[:, i])
            # Inicializamos coeficientes del algoritmo:
            a = {v: None for v in values}
            p = {v: None for v in values}
            n = {v: None for v in values}
            r = {v: None for v in values}
            # Inicializamos el mérito del atributo i
            merit = 0
            # Calculamos a_v, p_v, n_v, r_v
            for v in values:
                a[v] = np.count_nonzero(data[:, i] == v)
                p[v] = np.count_nonzero((data[:, i] == v) & (data[:, self.decision] == "si"))
                n[v] = a[v] - p[v]
                r[v] = a[v] / n_total

                # Actualizamos el mérito
                merit = merit + (r[v] * ID3.infor(p[v], n[v]))
            # Añadimos el mérito al atributo i
            merits[attributes[i]] = merit

        return merits

    def id3_algorithm(self, attributes, data, basic):

        # Creamos el nodo raíz
        root = Node(self.num, attributes, data)

        # CASOS BASE:
        if not np.any(data[:, self.decision] == "si"):
            root.set_value("no")
            # TODO: cout A3 << "Todos los ejemplares son "No"
        elif not np.any(data[:, self.decision] == "no"):
            root.set_value("si")
            # TODO: cout A3 << "Todos los ejemplares son "Si"

        # CASO RECURSIVO:
        else:
            # Calculamos méritos de los atributos y escogemos el menor
            root.set_merits(self.calculate_merits(attributes, data))
            # TODO: mostrar méritos A3
            best_attr, best_merit = root.get_merits().peekitem(0)
            root.set_value(best_attr)

            # Preparamos llamadas recursivas

            # Eliminamos el atributo
            children_attr = attributes.copy()
            children_attr.remove(best_attr)
            # Para cada valor del atributo, cogemos sus filas
            best_index = attributes.index(best_attr)
            values = np.unique(data[:, best_index])
            for v in values:
                self.num = self.num + 1
                mask_fila = data[:, best_index] == v
                mask_col = np.ones(data.shape[1], dtype=bool)
                mask_col[best_index] = False
                child_data = data[mask_fila, mask_col]
                # TODO: mostrar tabla A3
                if not basic:
                    # Llamada recursiva
                    child = self.id3_algorithm(children_attr, child_data, basic)
                    # Añadimos el hijo a la raíz
                    root.set_children(best_attr, child)

        return root

    # Métodos públicos:
    def algorithm(self, basic):
        return self.id3_algorithm(self.attributes_input, self.data_input, basic)
