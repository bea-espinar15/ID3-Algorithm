
#
#   CLASE MAIN WINDOW
#   -----------------
#   /RELLENAR/
#

import tkinter as tk
import Utilities
from Table import Table
from ID3 import ID3
from Tree import Tree


class MainWindow:

    # Constructor:
    def __init__(self, attributes_input, data_input):
        self.main_window = tk.Tk()
        self.attributes_input = attributes_input
        self.data_input = data_input
        self.middle_frame = None
        self.canvas = None
        self.init_gui()

    # Métodos privados:

    # Funciones de los botones:
    # -------------------------

    # Reinicia la aplicación
    def reset(self):
        self.main_window.destroy()
        self.main_window = tk.Tk()
        self.init_gui()

    # Ejecuta el algoritmo
    def ex_algorithm(self, basic):
        alg = ID3(self.attributes_input, self.data_input, basic)
        root = alg.algorithm()
        tree = Tree(root, self.canvas)
        tree.print_tree()
        tree.draw_tree()

    # Termina la aplicación
    def exit(self):
        self.main_window.destroy()

    # Pintar paneles:
    # ---------------

    # Inicializar (pintar) el header
    @staticmethod
    def init_header(main_frame):
        header_frame = tk.Frame(main_frame, height=80, bg=Utilities.LIGHT_GREEN)
        header_frame.pack(fill=tk.X)
        # Label título
        title_label = tk.Label(header_frame, text="Algoritmo ID3", font=Utilities.FONT_TITLE)
        title_label.config(highlightthickness=0, bd=0, bg=header_frame["bg"])
        title_label.pack(pady=20)

    # Inicializar (pintar) el panel de contenido principal
    def init_content(self, main_frame):
        content_frame = tk.Frame(main_frame, bg=Utilities.WHITE)
        content_frame.pack(expand=True, fill=tk.BOTH)

        # -------------- CONTENT AREAS -------------
        # Frame de tabla input
        left_frame = tk.Frame(content_frame, bg=content_frame["bg"])
        left_frame.pack(side=tk.LEFT, expand=False, fill=tk.BOTH)
        label_frame = tk.Frame(left_frame, bg=left_frame["bg"])
        label_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        input_label = tk.Label(label_frame, text="ENTRADA", font=Utilities.FONT_SUBTITLE)
        input_label.config(highlightthickness=0, bd=0, bg=label_frame["bg"])
        input_label.pack(pady=30)
        table_frame = tk.Frame(left_frame, bg=left_frame["bg"])
        table_frame.configure(borderwidth=1, relief="solid")
        table_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH, padx=40)
        Table(self.attributes_input, self.data_input, table_frame)

        # Frame de árbol de decisión
        self.middle_frame = tk.Frame(content_frame, bg=content_frame["bg"])
        self.middle_frame.pack(side=tk.LEFT, expand=False, fill=tk.BOTH)
        tree_label = tk.Label(self.middle_frame, text="ÁRBOL DE DECISIÓN", font=Utilities.FONT_SUBTITLE)
        tree_label.config(highlightthickness=0, bd=0, bg=self.middle_frame["bg"])
        tree_label.pack(pady=30)
        # Lienzo para pintar el árbol
        self.canvas = tk.Canvas(self.middle_frame, width=600, height=500, bg=self.middle_frame["bg"])
        self.canvas.pack(padx=40, expand=True, fill=tk.X)

        # Frame de info algoritmo
        right_frame = tk.Frame(content_frame, bg=content_frame["bg"])
        right_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        alg_label = tk.Label(right_frame, text="ALGORITMO", font=Utilities.FONT_SUBTITLE)
        alg_label.config(highlightthickness=0, bd=0, bg=right_frame["bg"])
        alg_label.pack(pady=30)

    # Inicializar (pintar) el footer
    def init_footer(self, main_frame):
        footer_frame = tk.Frame(main_frame, height=100, bg=Utilities.LIGHT_GREEN)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Botón reset
        reset_button = tk.Button(footer_frame, text="RESET", width=12, height=2, font=Utilities.FONT_BUTTON,
                                 bg=Utilities.GREEN, command=self.reset)
        reset_button.pack(side="left", padx=230, pady=10)
        reset_button.config(bd=2, relief=tk.GROOVE)

        # Botón ID3 básico
        basic_button = tk.Button(footer_frame, text="ID3 Básico", width=20, height=2, font=Utilities.FONT_BUTTON,
                                 bg=Utilities.GREEN, command=lambda: self.ex_algorithm(True))
        basic_button.pack(side="left", padx=30, pady=10)
        basic_button.config(bd=2, relief=tk.GROOVE)

        # Botón ID3 completo
        complete_button = tk.Button(footer_frame, text="ID3 Completo", width=20, height=2, font=Utilities.FONT_BUTTON,
                                    bg=Utilities.GREEN, command=lambda: self.ex_algorithm(False))
        complete_button.pack(side="left", padx=30, pady=10)
        complete_button.config(bd=2, relief=tk.GROOVE)

        # Botón salir
        exit_button = tk.Button(footer_frame, text="SALIR", width=12, height=2, font=Utilities.FONT_BUTTON,
                                bg=Utilities.GREEN, command=self.exit)
        exit_button.pack(side="left", padx=230, pady=10)
        exit_button.config(bd=2, relief=tk.GROOVE)

        footer_frame.pack_propagate(False)

    # Pintar interfaz gráfica
    def init_gui(self):
        self.main_window.title("ID3 Algorithm")
        self.main_window.geometry(Utilities.DIM)

        # -------------- MAIN ----------------
        main_frame = tk.Frame(self.main_window, highlightthickness=2, highlightbackground=Utilities.BLACK)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # -------------- HEADER --------------
        MainWindow.init_header(main_frame)
        # Borde frame
        header_border = tk.Frame(main_frame, height=2, bg=Utilities.GRAY)
        header_border.pack(fill=tk.X, side=tk.TOP)

        # -------------- CONTENT -------------
        self.init_content(main_frame)

        # ---------- FOOTER -----------
        self.init_footer(main_frame)
        # Borde frame
        footer_border = tk.Frame(main_frame, height=2, bg=Utilities.GRAY)
        footer_border.pack(fill=tk.X, side=tk.BOTTOM)

        self.main_window.mainloop()
