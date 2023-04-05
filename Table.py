
import tkinter as tk

class Table:

    def __init__(self):
        atributosJuego = open('input_files/AtributosJuego.txt', 'r')
        juego = open('input_files/Juego.txt', 'r')
        titulos = []
        for line in atributosJuego:
            word = line.split(',', 1)[0]
            titulos.append(word)
