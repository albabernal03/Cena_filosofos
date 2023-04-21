import threading


class Tenedor:
    def __init__(self, id,cena):
        self.id = id #esto nos 
        self.tenedor = threading.Lock()
        self.en_uso= False
        self.cena = cena
      

    def tomar(self, filosofo, tenedor):
        if self.tenedor.acquire(blocking=False):
            print("Filósofo", filosofo, "tomó tenedor", tenedor)
            self.en_uso= True
            self.cena.dibujar_tenedor(self.id)
            return True
        return False

    def liberar(self, filosofo, tenedor):
        self.tenedor.release()
        self.en_uso= False
        print("Filósofo", filosofo, "liberó tenedor", tenedor)
        self.cena.dibujar_tenedor(self.id)
        

    def color(self):
        if self.en_uso:
            return 'blue'
        else:
            return 'grey'