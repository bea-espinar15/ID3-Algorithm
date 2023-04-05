import tkinter as tk


class Table:

    def __init__(self, attributes_input, data_input, table_frame):
        self.attributes = attributes_input
        self.data = data_input
        self.frame = table_frame
        self.init_gui()

    def init_gui(self):
        totalrow = len(self.data)
        totalcolumn = len(self.attributes)

        for i in range(totalrow):
            for j in range(totalcolumn):
                e = Entry(self.frame, width == 22, fg='black', font=('Arial', 15, 'bold'))
                e.grid(row=i, column=j)
                if i == 1:
                    e.insert(END, data[j])
                else:
                    e.insert(END, self.attributes[i][j])
