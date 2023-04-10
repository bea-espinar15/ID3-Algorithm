
#
#   CLASE REGLAS
#   ------------
#   Clase que imprime las reglas resultado del algoritmo
#

import tkinter as tk
import Utilities


class Rules:

    # Constructor:
    def __init__(self, frame):
        self.frame = frame
        self.rules_text = ""
        self.num_rule = 1

    # Métodos privados:

    # Calcula el texto correspondiente al valor del atributo
    @staticmethod
    def create_text(value):
        switcher = {
            "soleado": "el tiempo es soleado",
            "nublado": "el tiempo es nublado",
            "lluvioso": "el tiempo es lluvioso",
            "caluroso": "la temperatura es calurosa",
            "templado": "la temperatura es templada",
            "frio": "la temperatura es fría",
            "alta": "hay mucha humedad",
            "normal": "hay humedad normal",
            "falso": "no hay viento",
            "verdad": "hay viento"
        }
        return switcher[value]

    # Genera las reglas
    def fill_label(self, node, first, rule):
        # CASO BASE:
        if len(node.get_children()) == 0:
            if node.get_value() == "si": rule += " entonces sí se juega"
            else: rule += " entonces no se juega"
            self.rules_text += str(self.num_rule) + ". " + rule + '\n'
            self.num_rule += 1

        # CASO RECURSIVO:
        else:
            if first: rule += "Si "
            else: rule += " y "
            for child in node.get_children().keys():
                new_rule = rule + self.create_text(child)
                # Llamada recursiva
                self.fill_label(node.get_children()[child], False, new_rule)

    # Imprimir reglas
    def draw_rules(self, root, basic):
        if basic:
            self.rules_text = "No se llegan a generar las reglas."
        else:
            # Generamos reglas
            self.fill_label(root, True, "")
        # Creamos scrollbar y text
        scrollbar = tk.Scrollbar(self.frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=10)
        text = tk.Text(self.frame, yscrollcommand=scrollbar.set, wrap="word", width=50, borderwidth=0, font=Utilities.FONT_TABLE)
        text.pack(side=tk.TOP, anchor=tk.W, expand=True, fill=tk.BOTH)
        scrollbar.config(command=text.yview)
        text.insert(tk.END, self.rules_text)
