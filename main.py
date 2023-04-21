import threading
import time
import random
import tkinter as tk
from math import sin, cos, pi
from cenafil import *
from filosofo import*
from tenedor import*

def iniciar():
    cena = CenaFilosofos()
    cena.iniciar_cena()

