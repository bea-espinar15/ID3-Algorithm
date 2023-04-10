
#
#   CLASE DECISIÓN
#   --------------
#   Clase que permite introducir datos al usuario y ver
#   qué decisión se toma
#

import tkinter as tk
import Utilities


class Decision:

    # Constructor:
    def __init__(self, frame):
        self.frame = frame
        self.button = None
        self.selected_options = [tk.StringVar() for _ in range(4)]
        self.input = {}
        self.output_label = None
        self.root = None

    # Métodos privados:

    # Calcular decisión
    def decide(self, node):
        # CASO BASE:
        if len(node.get_children()) == 0:
            if node.get_value() == "si": return "Sí"
            else: return "No"

        # CASO RECURSIVO:
        else:
            selected = self.input[node.get_value()]
            return self.decide(node.get_children()[selected])

    # Funcionalidad botón
    def decide_button(self):
        # Cogemos opciones seleccionadas
        self.input["TiempoExterior"] = self.selected_options[0].get()
        self.input["Temperatura"] = self.selected_options[1].get()
        self.input["Humedad"] = self.selected_options[2].get()
        self.input["Viento"] = self.selected_options[3].get()
        # Calculamos decisión
        decision = self.decide(self.root)
        self.output_label.config(text=decision)

    # Métodos públicos:

    # Setters
    def activate_button(self):
        self.button.config(state=tk.NORMAL)

    def set_root(self, root):
        self.root = root

    # Dibujar panel
    def draw_decision(self):
        # ------ TiempoExterior ------
        # Label
        attr0_label = tk.Label(self.frame, text="Tiempo exterior", bg=Utilities.WHITE)
        attr0_label.grid(row=0, column=0, sticky="nsew", padx=15)
        # Option Menu
        attr0_options = ["soleado", "nublado", "lluvioso"]
        self.selected_options[0] = tk.StringVar(value=attr0_options[0])
        combo0 = tk.OptionMenu(self.frame, self.selected_options[0], *attr0_options)
        combo0.grid(row=1, column=0, sticky="nsew", padx=15)

        # ------- Temperatura --------
        # Label
        attr1_label = tk.Label(self.frame, text="Temperatura", bg=Utilities.WHITE)
        attr1_label.grid(row=0, column=1, sticky="nsew", padx=15)
        # Option Menu
        attr1_options = ["caluroso", "templado", "frio"]
        self.selected_options[1] = tk.StringVar(value=attr1_options[0])
        combo1 = tk.OptionMenu(self.frame, self.selected_options[1], *attr1_options)
        combo1.grid(row=1, column=1, sticky="nsew", padx=15)

        # -------- Humedad --------
        # Label
        attr2_label = tk.Label(self.frame, text="Humedad", bg=Utilities.WHITE)
        attr2_label.grid(row=0, column=2, sticky="nsew", padx=15)
        # Option Menu
        attr2_options = ["alta", "normal"]
        self.selected_options[2] = tk.StringVar(value=attr2_options[0])
        combo2 = tk.OptionMenu(self.frame, self.selected_options[2], *attr2_options)
        combo2.grid(row=1, column=2, sticky="nsew", padx=15)

        # ------ Viento -------
        # Label
        attr3_label = tk.Label(self.frame, text="Viento", bg=Utilities.WHITE)
        attr3_label.grid(row=0, column=3, sticky="nsew", padx=15)
        # Option Menu
        attr3_options = ["verdad", "falso"]
        self.selected_options[3] = tk.StringVar(value=attr3_options[0])
        combo3 = tk.OptionMenu(self.frame, self.selected_options[3], *attr3_options)
        combo3.grid(row=1, column=3, sticky="nsew", padx=15)

        # ------- Botón submit -------
        self.button = tk.Button(self.frame, text="¿JUGAR?", height=1, font=Utilities.FONT_TABLE,
                                 bg=Utilities.GREEN, command=self.decide_button, state=tk.DISABLED)
        self.button.grid(row=2, column=1, sticky="nsew", padx=15, pady=15)
        self.button.config(bd=2, relief=tk.GROOVE)

        # ------- Output -------
        self.output_label = tk.Label(self.frame, bg=Utilities.LIGHT_GREEN, borderwidth=1, relief="solid")
        self.output_label.grid(row=2, column=2, sticky="nsew", padx=15, pady=15)
