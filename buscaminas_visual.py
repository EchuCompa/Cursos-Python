# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:56:28 2020

@author: Diego
"""
import buscaminas
from functools import partial
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox

def actualizar_botones(mapa, layout):
    for i in range(mapa.shape[0]):
        for j in range(mapa.shape[1]):
            b = layout.itemAtPosition(i,j).widget()
            if mapa[(i,j)] != ".":
                b.setText(mapa[(i,j)])
                b.setStyleSheet("color:rgb(0,0,0)")
                b.setStyleSheet("background-color:rgb(255,255,255)")
                b.setChecked(True)

def on_button_clicked(i, j, juego, app, layout, minas):
    if juego[1] is None:
        fi, co = juego[0].shape
        oculto = buscaminas.crear_tablero_minado(fi,co, minas, (i, j))
        juego[1] = oculto

    en_carrera = buscaminas.tocar((i,j), juego[0], juego[1])
    sigo_jugando = buscaminas.seguir_jugando(juego[0], juego[1])

    actualizar_botones(juego[0], layout)
    if not (en_carrera and sigo_jugando):
        alert = QMessageBox()
        if not en_carrera:
            msg = "Kabuuum!! Mejor suerte la próxima ;-)"
        else:
            msg = "Ganaste!! Animal, bestia, master, crack, champion!!"

        alert.setText(msg)
        alert.exec_()
        app.exit()

def jugar_partida_visual(fi = 10, co = 10, minas = 1):
    comienzo=True
    oculto = buscaminas.crear_tablero_minado(fi,co, minas, (-1, -1))
    mapa = buscaminas.crear_mapa(oculto)
    juego = [mapa, None]

    app = QApplication([])
    window = QWidget()

    layout = QGridLayout()
    for i in range(fi):
        for j in range(co):
            b = QPushButton(" ".format(i,j))
            b.setCheckable(True)
            layout.addWidget(b ,i, j)
            b.clicked.connect(partial(on_button_clicked, i, j, juego, app, layout, minas))

    window.setLayout(layout)
    window.show()
    app.exec_()

if __name__ == "__main__":
    fil = int(int(input("Introduzca la cantidad de filas: ")))
    col = int(int(input("Introduzca la cantidad de columnas: ")))
    minas = int(int(input("Introduzca la cantidad de minas: ")))
    jugar_partida_visual(fil, col, minas)








