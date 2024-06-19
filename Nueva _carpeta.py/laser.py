import pygame
from constantes import *

# Clase para representar los láseres en el juego
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        # Llamar al constructor de la clase base
        super().__init__()

        # Cargar la imagen del láser desde un archivo
        self.image = pygame.image.load("Imagenes/laser.png")

        # Obtener el rectángulo que rodea la imagen
        self.rect = self.image.get_rect()

        # Establecer la posición inicial del láser
        self.rect.y = y
        self.rect.centerx = x

        # Velocidad del láser en el eje y (hacia arriba)
        self.speed_y = -10
    
    # Método para actualizar la posición del láser en cada fotograma
    def update(self):
        # Mover el láser hacia arriba en el eje y
        self.rect.y += self.speed_y

        # Verificar si el láser ha salido de la pantalla por arriba
        if self.rect.bottom < 0:
            # Eliminar el láser si está fuera de la pantalla
            self.kill()