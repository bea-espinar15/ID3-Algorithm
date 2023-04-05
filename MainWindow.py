
#
#   CLASE MAIN WINDOW
#   -----------------
#   /RELLENAR/
#

import tkinter as tk
import Utilities


class MainWindow:

    # Constructor:
    def __init__(self):
        self.main_window = tk.Tk()
        self.init_gui()

    # Métodos privados:

    # Reinicia la aplicación
    def reset(self):
        self.main_window.destroy()
        self.main_window = tk.Tk()
        self.init_gui()

    # Ejecuta el algoritmo con un sólo nivel de recursividad
    @staticmethod
    def basic():
        pass

    # Ejecuta el algoritmo completo
    @staticmethod
    def complete():
        pass

    # Termina la aplicación
    def exit(self):
        self.main_window.destroy()

    # Inicializar (pintar) el header
    @staticmethod
    def init_header(main_frame):
        header_frame = tk.Frame(main_frame, height=80, bg=Utilities.LIGHT_GREEN)
        header_frame.pack(fill=tk.X)
        # Label título
        title_label = tk.Label(header_frame, text="Algoritmo ID3", font=Utilities.font_title)
        title_label.config(highlightthickness=0, bd=0, bg=header_frame["bg"])
        title_label.pack(pady=20)

    # Inicializar (pintar) el panel de contenido principal
    @staticmethod
    def init_content(main_frame):
        content_frame = tk.Frame(main_frame, bg=Utilities.WHITE)
        content_frame.pack(expand=True, fill=tk.BOTH)

        # -------------- CONTENT AREAS -------------
        # Frame de tabla input
        left_frame = tk.Frame(content_frame, bg=Utilities.WHITE)
        left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        input_label = tk.Label(left_frame, text="ENTRADA", font=Utilities.font_subtitle)
        input_label.config(highlightthickness=0, bd=0, bg=left_frame["bg"])
        input_label.pack(pady=30)

        # Frame de árbol de decisión
        middle_frame = tk.Frame(content_frame, bg=Utilities.WHITE)
        middle_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        tree_label = tk.Label(middle_frame, text="ÁRBOL DE DECISIÓN", font=Utilities.font_subtitle)
        tree_label.config(highlightthickness=0, bd=0, bg=middle_frame["bg"])
        tree_label.pack(pady=30)

        # Frame de info algoritmo
        right_frame = tk.Frame(content_frame, bg=Utilities.WHITE)
        right_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        alg_label = tk.Label(right_frame, text="ALGORITMO", font=Utilities.font_subtitle)
        alg_label.config(highlightthickness=0, bd=0, bg=right_frame["bg"])
        alg_label.pack(pady=30)

    # Inicializar (pintar) el footer
    def init_footer(self, main_frame):
        footer_frame = tk.Frame(main_frame, height=100, bg=Utilities.LIGHT_GREEN)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Botón reset
        reset_button = tk.Button(footer_frame, text="RESET", width=12, height=2, font=Utilities.font_button,
                                 bg=Utilities.GREEN, command=self.reset)
        reset_button.pack(side="left", padx=165, pady=10)
        reset_button.config(bd=2, relief=tk.GROOVE)

        # Botón ID3 básico
        basic_button = tk.Button(footer_frame, text="ID3 Básico", width=20, height=2, font=Utilities.font_button,
                                 bg=Utilities.GREEN, command=MainWindow.basic)
        basic_button.pack(side="left", padx=20, pady=10)
        basic_button.config(bd=2, relief=tk.GROOVE)

        # Botón ID3 completo
        complete_button = tk.Button(footer_frame, text="ID3 Completo", width=20, height=2, font=Utilities.font_button,
                                    bg=Utilities.GREEN, command=MainWindow.complete)
        complete_button.pack(side="left", padx=20, pady=10)
        complete_button.config(bd=2, relief=tk.GROOVE)

        # Botón salir
        exit_button = tk.Button(footer_frame, text="SALIR", width=12, height=2, font=Utilities.font_button,
                                bg=Utilities.GREEN, command=self.exit)
        exit_button.pack(side="left", padx=165, pady=10)
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
        MainWindow.init_content(main_frame)

        # ---------- FOOTER -----------
        self.init_footer(main_frame)
        # Borde frame
        footer_border = tk.Frame(main_frame, height=2, bg=Utilities.GRAY)
        footer_border.pack(fill=tk.X, side=tk.BOTTOM)

        self.main_window.mainloop()
