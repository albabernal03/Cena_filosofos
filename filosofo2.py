import pygame
import threading
import time
import random

# Definimos los colores para representar el estado de los filósofos
COLORS = {
    'Thinking': (255, 255, 255),
    'Hungry': (255, 255, 0),
    'Eating': (0, 255, 0),
    'Done': (0, 0, 0),
}

# Definimos el tamaño de la ventana y de los objetos gráficos
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
PHILOSOPHER_RADIUS = 30
PHILOSOPHER_DISTANCE = 150
FORK_RADIUS = 10

# Creamos la clase para representar a los filósofos
class Philosopher:

    def __init__(self, name, position, forks, screen):
        self.name = name
        self.position = position
        self.forks = forks
        self.screen = screen
        self.state = 'Thinking'

    def draw(self):
        color = COLORS[self.state]
        x, y = self.position
        pygame.draw.circle(self.screen, color, (x, y), PHILOSOPHER_RADIUS)

    def pickup_forks(self):
        left_fork, right_fork = self.forks
        # Adquirimos los semáforos para los tenedores
        left_fork.acquire()
        right_fork.acquire()
        self.state = 'Eating'

    def putdown_forks(self):
        left_fork, right_fork = self.forks
        # Liberamos los semáforos para los tenedores
        left_fork.release()
        right_fork.release()
        self.state = 'Thinking'

    def think(self):
        self.state = 'Thinking'
        time.sleep(random.uniform(1, 3))

    def eat(self):
        self.state = 'Hungry'
        time.sleep(random.uniform(1, 3))
        self.pickup_forks()
        self.state = 'Eating'
        time.sleep(random.uniform(1, 3))
        self.putdown_forks()
        self.state = 'Done'

    def run(self):
        while True:
            self.think()
            self.eat()

# Inicializamos Pygame y creamos la ventana
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Philosophers")

# Creamos los semáforos para los tenedores
forks = [threading.Semaphore(1) for _ in range(5)]

# Creamos los objetos gráficos para los filósofos y los colocamos en la mesa
philosophers = []
for i in range(5):
    x = int(WINDOW_WIDTH / 2 + PHILOSOPHER_DISTANCE * math.cos(math.pi * i / 2))
    y = int(WINDOW_HEIGHT / 2 + PHILOSOPHER_DISTANCE * math.sin(math.pi * i / 2))
    philosopher = Philosopher(f'Philosopher {i}', (x, y), (forks[i], forks[(i + 1) % 5]), screen)
    philosophers.append(philosopher)

# Iniciamos los hilos para cada filósofo
threads = []
for philosopher in philosophers:
    thread = threading.Thread(target=philosopher.run)
    threads.append(thread)
    thread.start()

# Ejecutamos el ciclo principal de Pygame para mostrar la ventana
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for philosopher in philosophers:
        philosopher.draw()
    pygame.display.flip()

# Esperamos a que terminen los hilos
for thread in threads:
    thread.join()

# Cerramos Pygame
pygame.quit()

