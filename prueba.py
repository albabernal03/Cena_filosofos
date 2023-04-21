import threading
import time
import random
import tkinter as tk
from math import sin, cos, pi

POSICIONES_FILOSOFOS = [(int(300 + 200*cos(2*pi/5*i)), int(300 + 200*sin(2*pi/5*i))) for i in range(5)]
POSICIONES_TENEDORES = [(int(275 + 200*cos(2*pi/5*i+pi/5)), int(275 + 200*sin(2*pi/5*i+pi/5))) for i in range(5)]


class Filosofo(threading.Thread):
    def __init__(self, id, tenedor_izq, tenedor_der, cena):
        threading.Thread.__init__(self)
        self.id = id
        self.tenedor_izq = tenedor_izq
        self.tenedor_der = tenedor_der
        self.cena = cena
        self.comidas = 0

    def run(self):
        while True:
            time.sleep(random.randint(1, 5))
            self.cena.actualizar_filosofo(self.id, "Hambriento", 'pink')
            tenedor_izq_tomado = self.tenedor_izq.tomar(self.id, "izquierdo")
            tenedor_der_tomado = self.tenedor_der.tomar(self.id, "derecho")
            if tenedor_izq_tomado and tenedor_der_tomado:
                self.cena.actualizar_filosofo(self.id, "Comiendo", 'yellow')
                self.comidas += 1
                self.cena.actualizar_contador(self.id, self.comidas)
                time.sleep(random.randint(1, 5))
                self.tenedor_der.liberar(self.id, "derecho")
                self.tenedor_izq.liberar(self.id, "izquierdo")
                self.cena.actualizar_filosofo(self.id, "Pensando", 'light blue')
            else:
                if tenedor_izq_tomado:
                    self.tenedor_izq.liberar(self.id, "izquierdo")
                if tenedor_der_tomado:
                    self.tenedor_der.liberar(self.id, "derecho")


class CenaFilosofos:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cena de los Filósofos")
        self.canvas = tk.Canvas(self.ventana, width=700, height= 700, bg='white')
        self.canvas.pack()
        self.filosofos = []
        self.tenedores = []
        for i in range(5):
            tenedor_izq = Tenedor(i, self.canvas)
            tenedor_der = Tenedor((i + 1) % 5, self.canvas)
            filosofo = Filosofo(i, tenedor_izq, tenedor_der, self)
            self.filosofos.append(filosofo)
            self.tenedores.append(tenedor_izq)
            self.tenedores.append(tenedor_der)
            self.dibujar_filosofo(i, "Pensando", 'white')
            self.dibujar_tenedor(i)
            tenedor_der.color(self.canvas)
            tenedor_izq.color(self.canvas)

        self.contadores = []

        texto_explicativo= 'Rosa: Hambriento\nAmarillo: Comiendo\nAzul: Pensando'
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

class Tenedor:
    def __init__(self, id,canvas):
        self.id = id #esto nos 
        self.tenedor = threading.Lock()
        self.en_uso= False
        self.canvas= canvas

    def tomar(self, filosofo, tenedor):
        if self.tenedor.acquire(blocking=False):
            print("Filósofo", filosofo, "tomó tenedor", tenedor)
            self.en_uso= True
            return True
        return False

    def liberar(self, filosofo, tenedor):
        self.tenedor.release()
        self.en_uso= False
        print("Filósofo", filosofo, "liberó tenedor", tenedor)
        

    def color(self):
        if self.en_uso:
            self.canvas.itemconfig(self.id, fill='blue')
        else:
            self.canvas.itemconfig(self.id, fill='grey')

    def cambiar_estado(self):
        self.en_uso = not self.en_uso
        self.canvas.itemconfig(self.dibujo, fill=self.color())
        self.canvas.update()



if __name__ == "__main__":
    cena = CenaFilosofos()
    cena.iniciar_cena()