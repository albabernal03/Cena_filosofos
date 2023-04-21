
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