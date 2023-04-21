import threading
import time
import random
import tkinter as tk

# Constantes para colores
BLANCO = "#FFFFFF"
NEGRO = "#000000"
GRIS = "#D3D3D3"
ROJO = "#FF0000"
VERDE = "#008000"

# Constantes para posiciones de los filósofos y los tenedores
POSICIONES_FILOSOFOS = [(300, 100), (450, 250), (450, 450), (300, 600), (100, 450), (100, 250)]
POSICIONES_TENEDORES = [(250, 150), (400, 300), (450, 500), (300, 550), (150, 400), (100, 200)]

class Tenedor:
    def __init__(self, id):
        self.id = id
        self.tenedor = threading.Lock()

    def tomar(self, filosofo, tenedor):
        if self.tenedor.acquire(blocking=False):
            print("Filósofo", filosofo, "tomó tenedor", tenedor)
            return True
        return False

    def liberar(self, filosofo, tenedor):
        self.tenedor.release()
        print("Filósofo", filosofo, "liberó tenedor", tenedor)

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
            self.cena.actualizar_filosofo(self.id, "Esperando", GRIS)
            tenedor_izq_tomado = self.tenedor_izq.tomar(self.id, "izquierdo")
            tenedor_der_tomado = self.tenedor_der.tomar(self.id, "derecho")
            if tenedor_izq_tomado and tenedor_der_tomado:
                self.cena.actualizar_filosofo(self.id, "Comiendo", VERDE)
                self.comidas += 1
                self.cena.actualizar_contador(self.id, self.comidas)
                time.sleep(random.randint(1, 5))
                self.tenedor_der.liberar(self.id, "derecho")
                self.tenedor_izq.liberar(self.id, "izquierdo")
                self.cena.actualizar_filosofo(self.id, "Pensando", ROJO)
            else:
                if tenedor_izq_tomado:
                    self.tenedor_izq.liberar(self.id, "izquierdo")
                if tenedor_der_tomado:
                    self.tenedor_der.liberar(self.id, "derecho")

class CenaFilosofos:
    def __init__(self):
        self.ventana = tk.Tk()
        self.canvas = tk.Canvas(self.ventana, width=600, height=700, bg=BLANCO)
        self.canvas.pack()
        self.filosofos = []
        self.tenedores = []
        for i in range(6):
            tenedor_izq = Tenedor(i)
            tenedor_der = Tenedor((i + 1) % 6)
            filosofo = Filosofo(i, tenedor_izq, tenedor_der, self)
            self.filosofos.append(filosofo)
            self.tenedores.append(tenedor_izq)
            self.tenedores.append(tenedor_der)
            self.dibujar_filosofo(i, "Pensando", ROJO)
            self.dibujar_tenedor(i)
        self.contadores = []
        for i in range(6):
            contador = tk.Label(self.ventana, text="Filósofo " + str(i) + ": 0", bg=BLANCO)
            contador.place(x=520, y=100 + i * 75)
            self.contadores.append(contador)

    def dibujar_filosofo(self, id, estado, color):
        x, y = POSICIONES_FILOSOFOS[id]
        self.canvas.create_oval(x-25, y-25, x+25, y+25, fill=color, outline=NEGRO)
        self.canvas.create_text(x, y, text="Filósofo " + str(id) + "\n" + estado)

    def dibujar_tenedor(self, id):
        x, y = POSICIONES_TENEDORES[id]
        self.canvas.create_rectangle(x-10, y-10, x+10, y+10, fill=NEGRO)

    def actualizar_filosofo(self, id, estado, color):
        self.canvas.delete("filosofo"+str(id))
        self.dibujar_filosofo(id, estado, color)

    def actualizar_contador(self, id, comidas):
        self.contadores[id].configure(text="Filósofo " + str(id) + ": " + str(comidas))

    def iniciar_cena(self):
        for filosofo in self.filosofos:
            filosofo.start()
        self.ventana.mainloop()

if __name__ == "__main__":
    cena = CenaFilosofos()
    cena.iniciar_cena()
