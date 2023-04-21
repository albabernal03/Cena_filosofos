#RESOLUCIÓN DE LA CENA DE LOS FILOSOFOS UTILIZANDO SEMAFOROS, ADEMÁS SOLUCION SE PROPORCIONARA CON VENTANA GRAFICA

import threading
import time
import tkinter as tk

class Filosofo():
    def __init__(self, nombre, tenedorIzq, tenedorDer, ventana):
        self.nombre = nombre
        self.tenedorIzq = tenedorIzq
        self.tenedorDer = tenedorDer
        self.ventana = ventana
        self.estado = "PENSANDO"
        self.numComidas = 0

