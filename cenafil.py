import threading
import time
import random
from tenedor import Tenedor
import tkinter as tk
from math import sin, cos, pi
from filosofo import Filosofo

# Constantes para posiciones de los filósofos y los tenedores
POSICIONES_FILOSOFOS = [(int(300 + 200*cos(2*pi/5*i)), int(300 + 200*sin(2*pi/5*i))) for i in range(5)]
POSICIONES_TENEDORES = [(int(275 + 200*cos(2*pi/5*i+pi/5)), int(275 + 200*sin(2*pi/5*i+pi/5))) for i in range(5)]


class CenaFilosofos:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cena de los Filósofos")
        self.canvas = tk.Canvas(self.ventana, width=700, height= 700, bg='white')
        self.canvas.pack()
        self.filosofos = []
        self.tenedores = []
        for i in range(5):
            tenedor_izq = Tenedor(i,self)
            tenedor_der = Tenedor((i + 1) % 5,self)
            filosofo = Filosofo(i, tenedor_izq, tenedor_der, self)
            self.filosofos.append(filosofo)
            self.tenedores.append(tenedor_izq)
            self.tenedores.append(tenedor_der)
            self.dibujar_filosofo(i, "Pensando", 'white')
            self.dibujar_tenedor(i)
            
        self.contadores = []

        texto_explicativo= 'Rosa: Hambriento\nAmarillo: Comiendo\nAzul: Pensando\nAzul oscuro: Tendor en uso\nGris: Tenedor libre'
        texto_explicativo= tk.Label(self.ventana, text=texto_explicativo, bg='white')
        texto_explicativo.pack()
    

        for i in range(5):
            contador = tk.Label(self.ventana, text="Filósofo " + str(i) + ": 0", bg='white')
            #ponemos el contador a la derecha de la ventana centrado
            contador.place(x=600, y=50+50*i)
            self.contadores.append(contador)
        

    def dibujar_filosofo(self, id, estado, color):
        x, y = POSICIONES_FILOSOFOS[id]
        self.canvas.create_oval(x-40, y-40, x+40, y+40, fill=color, outline='black')
        self.canvas.create_text(x, y, text="Filósofo " + str(id) + "\n" + estado)

    def dibujar_tenedor(self, id):
        x, y = POSICIONES_TENEDORES[id]
        color = self.tenedores[id].color()
        self.canvas.create_rectangle(x-10, y-10, x+10, y+10, fill=color)
        

    def actualizar_filosofo(self, id, estado, color):
        self.canvas.delete("filosofo"+str(id))
        self.dibujar_filosofo(id, estado, color)

    def actualizar_contador(self, id, comidas):
        self.contadores[id].configure(text="Filósofo " + str(id) + ": " + str(comidas))

    def iniciar_cena(self):
        for filosofo in self.filosofos:
            filosofo.start()
        self.ventana.mainloop()