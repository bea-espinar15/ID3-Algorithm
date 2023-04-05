
import tkinter as tk

class Table:

    def __init__(self, attributes_input, data_input, table_frame):
        self.attributes = attributes_input
        self.data = data_input
        self.frame = table_frame
        self.init_GUI()

    def init_GUI(self):
        table = tk.Listbox(self.frame, width=50, height=10)
        table.grid(row=0, column=0, padx=10, pady=10)
        for header in self.attributes:
            table.insert(tk.END, header)

        for row in self.data:
            table.insert(tk.END, row)

        table.configure(bg="white", fg="black", font=("console", 12))
