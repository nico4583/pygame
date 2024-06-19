import pygame
from constantes import *
import random

# Definir la clase Enemigos que hereda de pygame.sprite.Sprite
class Enemigos(pygame.sprite.Sprite):
    def __init__(self, enemigos_images, nivel_actual, escala_enemigos) -> None:
        # Llamar al constructor de la clase base
        super().__init__()
        
        # Nivel actual del juego
        self.nivel = nivel_actual
        
        # Elegir una imagen aleatoria para el enemigo
        self.image = random.choice(enemigos_images)
        
        # Escalar la imagen al tamaño especificado
        self.image = pygame.transform.scale(self.image, escala_enemigos)
        
        # Obtener el rectángulo que rodea la imagen
        self.rect = self.image.get_rect()
        
        # Establecer la posición inicial del enemigo de manera aleatoria
        self.rect.x = random.randrange(ANCHO_VENTANA - self.rect.width)
        self.rect.y = random.randrange(-200, -40)
        
        # Establecer velocidades iniciales en las direcciones x e y
        self.speed_y = random.randrange(1, 5) * nivel_actual
        self.speed_x = random.randrange(-5, 5) * nivel_actual

    # Método para actualizar la posición del enemigo en cada fotograma
    def update(self):
        # Mover el enemigo hacia abajo (eje y)
        self.rect.y += self.speed_y
        # Mover el enemigo en la dirección x
        self.rect.x += self.speed_x
        
        # Verificar si el enemigo está fuera de la pantalla
        if self.rect.top > ALTO_VENTANA + 10 or self.rect.left < -30 or self.rect.right > ANCHO_VENTANA + 30:
            # Reposicionar el enemigo en la parte superior de la pantalla de manera aleatoria
            self.rect.x = random.randrange(ANCHO_VENTANA - self.rect.width)
            self.rect.y = random.randrange(-140, -40)
            
            # Actualizar las velocidades de manera aleatoria para un nuevo movimiento
            self.speed_y = random.randrange(1, 10) * self.nivel
            self.speed_x = random.randrange(-5, 5) * self.nivel




