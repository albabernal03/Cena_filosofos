#RESOLUCIÓN DE LA CENA DE LOS FILOSOFOS UTILIZANDO SEMAFOROS, ADEMÁS SOLUCION SE PROPORCIONARA CON VENTANA GRAFICA

import threading
import time
import tkinter as tk

#Definimos la posición de los filosofos
posiciones = [(200, 50), (300, 150), (300, 250), (200, 350), (100, 250), (100, 150)]
#Definimos la posición de los tenedores
posiciones_tenedores = [(250, 100), (350, 200), (350, 300), (250, 400), (150, 300), (150, 200)]

