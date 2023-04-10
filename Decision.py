
#
#   CLASE DECISIÓN
#   --------------
#   Clase que permite introducir datos al usuario y ver
#   qué decisión se toma
#

import tkinter as tk


class Decision:

    # Constructor:
    def __init__(self, frame, executed):
        self.frame = frame
        self.executed = executed
        self.selected_options = [None] * 4
        self.input = [0] * 4

    # Métodos privados:
    def on_select_0(self, event):
        self.input[0] = self.selected_options[0].get()

    def on_select_1(self, event):
        self.input[1] = self.selected_options[1].get()

    def on_select_2(self, event):
        self.input[2] = self.selected_options[2].get()

    def on_select_3(self, event):
        self.input[3] = self.selected_options[3].get()

    # Métodos públicos:

    # Setter
    def set_executed(self, executed):
        self.executed = executed

    # Dibujar panel
    def draw_decision(self):
        pass
        # ------ TiempoExterior ------
        attr0_options = ["soleado", "nublado", "lluvioso"]
        self.selected_options[0] = tk.StringVar(value=attr0_options[0])
        combo0 = tk.OptionMenu(self.frame, self.selected_options[0], *attr0_options, command=self.on_select_0)
        combo0.pack()

        # ------- Temperatura - ------
        attr1_options = ["caluroso", "templado", "frio"]
        self.selected_options[1] = tk.StringVar(value=attr1_options[0])
        combo1 = tk.OptionMenu(self.frame, self.selected_options[1], *attr1_options, command=self.on_select_1)
        combo1.pack()

        # ------ TiempoExterior - -----
        attr2_options = ["alta", "normal"]
        self.selected_options[2] = tk.StringVar(value=attr2_options[0])
        combo2 = tk.OptionMenu(self.frame, self.selected_options[2], *attr2_options, command=self.on_select_2)
        combo2.pack()

        # ------ Viento - -----
        attr3_options = ["verdad", "falso"]
        self.selected_options[3] = tk.StringVar(value=attr3_options[0])
        combo3 = tk.OptionMenu(self.frame, self.selected_options[3], *attr3_options, command=self.on_select_3)
        combo3.pack()
