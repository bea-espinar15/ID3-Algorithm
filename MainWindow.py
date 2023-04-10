
#
#   CLASE MAIN WINDOW
#   -----------------
#   Clase que dibuja la interfaz e implementa las funcionalidades
#   de los botones. Atributos:
#   · main_window = ventana principal, objeto raíz de la GUI
#   · attributes_input = lista de atributos del fichero de entrada
#   · data_input = matriz de datos del fichero de entrada
#   · main_frame = frame principal de la aplicación
#   · middle_frame = frame que contiene el lienzo para dibujar el
#     árbol de decisión
#   · canvas = lienzo donde se pinta el árbol de decisión
#

import tkinter as tk
import Utilities
from Table import Table
from ID3 import ID3
from Tree import Tree
from Info import Info
from Rules import Rules
from Decision import Decision


class MainWindow:

    # Constructor:
    def __init__(self, attributes_input, data_input):
        self.main_window = tk.Tk()
        self.attributes_input = attributes_input
        self.data_input = data_input
        self.main_frame = None
        self.middle_frame = None
        self.canvas = None
        self.basic_button = None
        self.complete_button = None
        self.info_alg = None
        self.rules = None
        self.decision = None
        self.init_gui()

    # Métodos privados:

    # Funciones de los botones:
    # -------------------------

    # Reinicia la aplicación
    def reset(self):
        self.main_frame.destroy()
        self.init_gui()

    # Ejecuta el algoritmo y dibuja el árbol solución
    def ex_algorithm(self, basic):
        alg = ID3(self.attributes_input, self.data_input, basic, self.info_alg, self.rules)
        root = alg.algorithm()
        tree = Tree(root, self.canvas)
        tree.draw_tree()
        # Deshabilitar botones del algoritmo
        self.basic_button.config(state="disabled")
        self.complete_button.config(state="disabled")
        if not basic:
            # Activar botón decisión
            self.decision.activate_button()
            self.decision.set_root(root)

    # Termina la aplicación
    def exit(self):
        self.main_window.destroy()

    # Pintar paneles:
    # ---------------

    # Inicializar (pintar) el header
    def init_header(self):
        header_frame = tk.Frame(self.main_frame, height=80, bg=Utilities.LIGHT_GREEN)
        header_frame.pack(fill=tk.X)
        # Label título
        title_label = tk.Label(header_frame, text="Algoritmo ID3", font=Utilities.FONT_TITLE)
        title_label.config(highlightthickness=0, bd=0, bg=header_frame["bg"])
        title_label.pack(pady=20)

    # Inicializar (pintar) el panel de contenido principal
    def init_content(self):
        content_frame = tk.Frame(self.main_frame, bg=Utilities.WHITE)
        content_frame.pack(expand=True, fill=tk.BOTH)

        # -------------- LEFT -------------

        # -------------- TABLA ------------
        # Frame de tabla input
        left_frame = tk.Frame(content_frame, bg=content_frame["bg"])
        left_frame.pack(side=tk.LEFT, expand=False, fill=tk.BOTH)
        # Label título
        label_input_frame = tk.Frame(left_frame, bg=left_frame["bg"])
        label_input_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        input_label = tk.Label(label_input_frame, text="ENTRADA", font=Utilities.FONT_SUBTITLE)
        input_label.config(highlightthickness=0, bd=0, bg=label_input_frame["bg"])
        input_label.pack(pady=30)
        # Tabla
        table_frame = tk.Frame(left_frame, bg=left_frame["bg"])
        table_frame.configure(borderwidth=1, relief="solid")
        table_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH, padx=30)
        Table(self.attributes_input, self.data_input, table_frame)

        # -------------- REGLAS ------------
        # Label título
        rules_label = tk.Label(left_frame, text="REGLAS", font=Utilities.FONT_SUBSUBTITLE, justify="left")
        rules_label.config(highlightthickness=0, bd=0, bg=left_frame["bg"])
        rules_label.pack(side=tk.TOP, padx=30, pady=20, anchor=tk.W)
        # Rellenar reglas
        rules_frame = tk.Frame(left_frame, bg=left_frame["bg"])
        rules_frame.pack(side=tk.TOP, padx=30, expand=True, fill=tk.BOTH)
        rules_frame.pack_propagate(False)
        self.rules = Rules(rules_frame)
        # Borde frame
        empty_frame = tk.Frame(left_frame, height=40, bg=left_frame["bg"])
        empty_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # -------------- MIDDLE -------------

        # -------------- ÁRBOL ------------
        # Frame de árbol de decisión
        self.middle_frame = tk.Frame(content_frame, bg=content_frame["bg"])
        self.middle_frame.pack(side=tk.LEFT, expand=False, fill=tk.BOTH)
        # Label título
        tree_label = tk.Label(self.middle_frame, text="ÁRBOL DE DECISIÓN", font=Utilities.FONT_SUBTITLE)
        tree_label.config(highlightthickness=0, bd=0, bg=self.middle_frame["bg"])
        tree_label.pack(pady=30)
        # Lienzo para pintar el árbol
        self.canvas = tk.Canvas(self.middle_frame, width=520, height=300, bg=self.middle_frame["bg"])
        self.canvas.config(highlightthickness=0)
        self.canvas.pack(side=tk.TOP, padx=0, expand=False, fill=tk.X)

        # -------------- DECISIÓN ------------
        # Label título
        decision_label = tk.Label(self.middle_frame, text="DECISIÓN", font=Utilities.FONT_SUBSUBTITLE, justify="left")
        decision_label.config(highlightthickness=0, bd=0, bg=self.middle_frame["bg"])
        decision_label.pack(side=tk.TOP, pady=10, anchor=tk.W)
        # Panel decisión
        decision_frame = tk.Frame(self.middle_frame, bg=self.middle_frame["bg"])
        decision_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        decision_frame.pack_propagate(False)
        self.decision = Decision(decision_frame)
        self.decision.draw_decision()
        # Borde frame
        empty_frame = tk.Frame(self.middle_frame, height=40, bg=left_frame["bg"])
        empty_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # -------------- RIGHT -------------
        # Frame de info algoritmo
        right_frame = tk.Frame(content_frame, bg=content_frame["bg"])
        right_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        # Label título
        label_alg_frame = tk.Frame(right_frame, bg=right_frame["bg"])
        label_alg_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        alg_label = tk.Label(label_alg_frame, text="ALGORITMO", font=Utilities.FONT_SUBTITLE)
        alg_label.config(highlightthickness=0, bd=0, bg=label_alg_frame["bg"])
        alg_label.pack(pady=30)
        # Información del algoritmo
        info_frame = tk.Frame(right_frame, bg=right_frame["bg"])
        info_frame.pack(side=tk.TOP, expand=True, padx=30, fill=tk.BOTH)
        # Canvas info
        canvas_info = tk.Canvas(info_frame, borderwidth=0, highlightthickness=0, bg=info_frame["bg"])
        aux_frame_2 = tk.Frame(canvas_info, bg=info_frame["bg"])
        scrollbar_2 = tk.Scrollbar(info_frame, orient="vertical", command=canvas_info.yview)
        scrollbar_2.pack(side=tk.RIGHT, fill=tk.Y, padx=10)
        canvas_info.configure(yscrollcommand=scrollbar_2.set)
        canvas_info.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # Asociamos frame y scrollbar al canvas
        aux_frame_2.bind("<Configure>", lambda e: canvas_info.configure(scrollregion=canvas_info.bbox("all")))
        canvas_info.create_window((0, 0), window=aux_frame_2, anchor="nw")
        # Rellenar info
        self.info_alg = Info(aux_frame_2)
        # Borde frame
        empty_frame_2 = tk.Frame(right_frame, height=40, bg=right_frame["bg"])
        empty_frame_2.pack(side=tk.BOTTOM, fill=tk.X)

    # Inicializar (pintar) el footer
    def init_footer(self):
        footer_frame = tk.Frame(self.main_frame, height=100, bg=Utilities.LIGHT_GREEN)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Botón reset
        reset_button = tk.Button(footer_frame, text="RESET", width=12, height=2, font=Utilities.FONT_BUTTON,
                                 bg=Utilities.GREEN, command=self.reset)
        reset_button.pack(side="left", padx=168, pady=10)
        reset_button.config(bd=2, relief=tk.GROOVE)

        # Botón ID3 básico
        self.basic_button = tk.Button(footer_frame, text="ID3 Básico", width=20, height=2, font=Utilities.FONT_BUTTON,
                                 bg=Utilities.GREEN, command=lambda: self.ex_algorithm(True))
        self.basic_button.pack(side="left", padx=25, pady=10)
        self.basic_button.config(bd=2, relief=tk.GROOVE)

        # Botón ID3 completo
        self.complete_button = tk.Button(footer_frame, text="ID3 Completo", width=20, height=2, font=Utilities.FONT_BUTTON,
                                    bg=Utilities.GREEN, command=lambda: self.ex_algorithm(False))
        self.complete_button.pack(side="left", padx=25, pady=10)
        self.complete_button.config(bd=2, relief=tk.GROOVE)

        # Botón salir
        exit_button = tk.Button(footer_frame, text="SALIR", width=12, height=2, font=Utilities.FONT_BUTTON,
                                bg=Utilities.GREEN, command=self.exit)
        exit_button.pack(side="left", padx=168, pady=10)
        exit_button.config(bd=2, relief=tk.GROOVE)

        footer_frame.pack_propagate(False)

    # Pintar interfaz gráfica
    def init_gui(self):
        self.main_window.title("ID3 Algorithm")
        self.main_window.geometry(Utilities.DIM)

        # -------------- MAIN ----------------
        self.main_frame = tk.Frame(self.main_window, highlightthickness=2, highlightbackground=Utilities.BLACK)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # -------------- HEADER --------------
        self.init_header()
        # Borde frame
        header_border = tk.Frame(self.main_frame, height=2, bg=Utilities.GRAY)
        header_border.pack(fill=tk.X, side=tk.TOP)

        # -------------- CONTENT -------------
        self.init_content()

        # ---------- FOOTER -----------
        self.init_footer()
        # Borde frame
        footer_border = tk.Frame(self.main_frame, height=2, bg=Utilities.GRAY)
        footer_border.pack(fill=tk.X, side=tk.BOTTOM)

        self.main_window.mainloop()
