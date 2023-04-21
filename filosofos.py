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
        self.actualizar_ventana()

    def coger_tenedores(self):
        tenedorIzq, tenedorDer = self.tenedorIzq, self.tenedorDer
        while True:
            tenedorIzq.acquire() #Adquiere el tenedor izquierdo
            adq_tenedorIzq = tenedorIzq.locked() #Comprueba si el tenedor izquierdo esta bloqueado
            tenedorDer.acquire() #Adquiere el tenedor derecho
            adq_tenedorDer = tenedorDer.locked() #Comprueba si el tenedor derecho esta bloqueado
            if adq_tenedorIzq and adq_tenedorDer: 
                self.estado="COMIENDO"
                self.numComidas += 1
                self.actualizar_ventana()
                break
