
#
#   CLASE MAIN
#   ----------
#   Clase que inicia la aplicación y lee los datos de entrada
#

import numpy as np
from MainWindow import MainWindow


def main():

    # Leer atributos del fichero
    attributes_file = open('input_files/AtributosJuego.txt', 'r')
    attributes_file = attributes_file.read()
    attributes = []
    while ',' in attributes_file:
        attributes.append(attributes_file.split(',', 1)[0])
        attributes_file = attributes_file.split(',', 1)[1]
    attributes.append(attributes_file.strip())

    # Leer datos de la tabla del fichero
    data_file = open('input_files/Juego.txt', 'r')
    lines = data_file.readlines()
    content = []
    i = 0
    for line in lines:
        line = line.strip()
        content.append([])
        while ',' in line:
            content[i].append(line.split(',', 1)[0])
            line = line.split(',', 1)[1]
        content[i].append(line.strip())
        i += 1

    # Creamos la matriz con los datos leídos
    rows = len(lines)
    cols = len(attributes)
    data = np.empty((rows, cols), dtype=object)
    for i in range(len(content)):
        for j in range(len(content[i])):
            data[i, j] = content[i][j]

    # Iniciamos la aplicación
    MainWindow(attributes, data)


main()
