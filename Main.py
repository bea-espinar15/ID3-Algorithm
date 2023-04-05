
#
#   CLASE MAIN
#   ----------
#   Clase que inicia la aplicación y lee los datos de entrada
#

atributosJuego = open('input_files/AtributosJuego.txt', 'r')
juego = open('input_files/Juego.txt', 'r')
titulos = []
for line in atributosJuego:
    word = line.split(',', 1)[0]
    titulos.append(word)

from MainWindow import MainWindow

# leer fichero
# attributes y data
MainWindow()
