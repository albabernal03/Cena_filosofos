import threading

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
