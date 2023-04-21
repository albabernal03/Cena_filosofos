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
    




    
