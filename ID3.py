
#
#   CLASE ALGORITMO ID3
#   -------------------
#   Clase para representar el algoritmo. Atributos:
#   · num = nº de nodos visitados + 1 (para poder numerar los nodos según se van creando)
#   · attributes_input = lista de atributos iniciales
#   · data_input = matriz de datos iniciales
#   · basic = ¿versión básica del algoritmo? (la versión básica sólo implementa 1 nivel de
#             recursividad, si basic = false entonces se ejecuta el algoritmo completo)
#

import math
import numpy as np
from Node import Node


class ID3:

    # Constructor:
    def __init__(self, attributes_input, data_input, basic, info_alg, rules):
        self.num = 1
        self.attributes_input = attributes_input
        self.data_input = data_input
        self.basic = basic
        self.info = info_alg
        self.rules = rules

    # Métodos privados:

    # Función infor()
    @staticmethod
    def infor(p, n):
        if p == 0 or n == 0:  # No existe log_2(0)
            return 0
        else:
            return (-p * math.log(p, 2)) - (n * math.log(n, 2))

    # Calcula el mérito de los atributos <attributes> que tienen los valores <data>
    # merito de un atributo = sum_i=1_N(r_i * infor(p_i,n_i))
    @staticmethod
    def calculate_merits(attributes, data):

        merits = {}
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
                p[v] = (np.count_nonzero((data[:, i] == v) & (data[:, -1] == "si"))) / a[v]
                n[v] = (np.count_nonzero((data[:, i] == v) & (data[:, -1] == "no"))) / a[v]
                r[v] = a[v] / n_total

                # Actualizamos el mérito
                merit = merit + (r[v] * ID3.infor(p[v], n[v]))
            # Añadimos el mérito al atributo i
            merits[attributes[i]] = merit

        # Ordenamos los méritos
        merits = {k: v for k, v in sorted(merits.items(), key=lambda item: item[1])}
        return merits

    # Función recursiva que implementa el algoritmo, dados los atributos
    # <attributes> con los valores <data>
    def id3_algorithm(self, attributes, data):

        # Creamos el nodo raíz
        root = Node(self.num, attributes, data)

        # CASOS BASE: todos los ejemplares tienen el mismo valor de decisión
        if not np.any(data[:, -1] == "si"):
            root.set_value("no")
            # Imprimir info
            self.info.draw_text(root.get_num(), False)
        elif not np.any(data[:, -1] == "no"):
            root.set_value("si")
            # Imprimir info
            self.info.draw_text(root.get_num(), True)

        # CASO RECURSIVO: hay ejemplares positivos y ejemplares negativos
        else:
            # Calculamos méritos de los atributos y escogemos el mejor (menor mérito)
            root.set_merits(self.calculate_merits(attributes, data))
            best_attr = next(iter(root.get_merits()))
            root.set_value(best_attr)
            # Imprimir info
            self.info.draw_list(root.get_num(), root.get_merits())

            # Preparamos llamadas recursivas

            # Eliminamos el atributo
            children_attr = attributes.copy()
            children_attr.remove(best_attr)
            best_index = attributes.index(best_attr)
            # Obtenemos valores que toma el atributo seleccionado
            values = np.unique(data[:, best_index])
            for v in values:
                self.num = self.num + 1
                # Nos quedamos con las filas que tengan ese valor del atributo
                mask_fila = data[:, best_index] == v
                aux = data[mask_fila, :]
                # Eliminamos la columna del atributo seleccionado
                mask_col = np.ones(aux.shape[1], dtype=bool)
                mask_col[best_index] = False
                child_data = aux[:, mask_col]
                # Imprimir info
                self.info.draw_table(v, children_attr, child_data)
                # La versión básica se queda aquí, no implementa más niveles de recursividad
                if not self.basic:
                    # Llamada recursiva
                    child = self.id3_algorithm(children_attr, child_data)
                    # Añadimos el hijo a la raíz
                    root.set_children(v, child)

        return root

    # Métodos públicos:
    def algorithm(self):
        root = self.id3_algorithm(self.attributes_input, self.data_input)
        self.rules.draw_rules(root, self.basic)
        return root
