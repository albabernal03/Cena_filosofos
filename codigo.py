import threading
import random
import time
import tkinter as tk


#Establecemos la posición de los filósofos y los tenedores

POSICIONES_FILOSOFOS = [(300, 100), (450, 250), (450, 450), (300, 600), (100, 450), (100, 250)] #Lo hemos puesto en mayuscula ya que son variables fijas
POSICIONES_TENEDORES = [(250, 150), (400, 300), (450, 500), (300, 550), (150, 400), (100, 200)]

class Tenedor: #tenemos tanto el de la derecha como el de la izquierda y se necesitan ambos para comer
    def __init__(self, id):
        self.id = id #esto nos indica el id del tenedor, es decir, si es el de la derecha o el de la izquierda
        self.tenedor = threading.Lock() #creamos un lock para que no se pueda acceder a la vez a los tenedores 

    def tomar(self, filosofo, tenedor): #metodo para tomar el tenedor
        if self.tenedor.acquire(blocking=False): #si el tenedor se puede adquirir, es decir, si no está ocupado
            print("Filósofo", filosofo, "tomó tenedor", tenedor) #imprimimos que el filosofo ha tomado el tenedor
            return True #devolvemos true
        return False #si no se puede adquirir el tenedor, devolvemos false
    
    def liberar(self, filosofo, tenedor):
        self.tenedor.release()
        print("Filósofo", filosofo, "liberó tenedor", tenedor)

class Filosofo(threading.Thread): #creamos la clase filosofo
    def __init__(self, id, tenedor_izq, tenedor_der, cena): #le pasamos el id, el tenedor izquierdo, el tenedor derecho y la cena
        threading.Thread.__init__(self) #inicializamos el hilo
        self.id = id #le pasamos el id del filosofo
        self.tenedor_izq = tenedor_izq #le pasamos el tenedor izquierdo
        self.tenedor_der = tenedor_der #le pasamos el tenedor derecho
        self.cena = cena #le pasamos la cena
        self.comidas = 0 #inicializamos el numero de comidas a 0

    def run(self): #metodo run
        while True: #bucle infinito
            time.sleep(random.randint(1, 5)) #tiempo aleatorio entre 1 y 5
            self.cena.actualizar_filosofo(self.id, "Hambriento", 'red') #actualizamos el estado del filosofo a hambriento
            tenedor_izq_tomado = self.tenedor_izq.tomar(self.id, "izquierdo") #tomamos el tenedor izquierdo
            tenedor_der_tomado = self.tenedor_der.tomar(self.id, "derecho") #tomamos el tenedor derecho
            if tenedor_izq_tomado and tenedor_der_tomado: #si se han tomado ambos tenedores
                self.cena.actualizar_filosofo(self.id, "Comiendo", 'yellow') #actualizamos el estado del filosofo a comiendo
                time.sleep(random.randint(1, 5)) #tiempo aleatorio entre 1 y 5
                self.tenedor_izq.liberar(self.id, "izquierdo") #liberamos el tenedor izquierdo
                self.tenedor_der.liberar(self.id, "derecho") #liberamos el tenedor derecho
                self.comidas += 1 #aumentamos el numero de comidas
                self.cena.actualizar_filosofo(self.id, "Pensando", 'white') #actualizamos el estado del filosofo a pensando
            else:
                if tenedor_der_tomado:
                    self.tenedor_der.liberar(self.id, "derecho")
                if tenedor_izq_tomado:
                    self.tenedor_izq.liberar(self.id, "izquierdo")

                    
            

            


    




    
