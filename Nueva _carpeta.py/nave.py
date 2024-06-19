import pygame
from constantes import *
from laser import Laser


# Clase para representar la nave del jugador en el juego
class Nave(pygame.sprite.Sprite):
    def __init__(self) -> None:
        # Llamar al constructor de la clase base
        super().__init__()

        # Cargar la imagen de la nave desde un archivo y escalarla
        self.image = pygame.image.load("Imagenes/1.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        # Obtener el rectángulo que rodea la imagen
        self.rect = self.image.get_rect()

        # Establecer la posición inicial de la nave en la parte inferior central de la pantalla
        self.rect.centerx = ANCHO_VENTANA // 2
        self.rect.bottom = ALTO_VENTANA - 10

        # Velocidad inicial en el eje x (horizontal)
        self.speed_x = 0

        # Puntos de vida de la nave
        self.vida = 100

    # Método para actualizar la posición de la nave en cada fotograma
    def update(self):
        # Reiniciar la velocidad en el eje x
        self.speed_x = 0

        # Obtener el estado de las teclas presionadas
        keys = pygame.key.get_pressed()

        # Mover la nave a la izquierda si se presiona la tecla izquierda
        if keys[pygame.K_LEFT]:
            self.speed_x = -10
            self.rect.x += self.speed_x

        # Mover la nave a la derecha si se presiona la tecla derecha
        if keys[pygame.K_RIGHT]:
            self.speed_x = 10
            self.rect.x += self.speed_x

        # Limitar la posición de la nave para que no salga de los bordes de la pantalla
        if self.rect.right > ANCHO_VENTANA:
            self.rect.right = ANCHO_VENTANA
        if self.rect.left < 0:
            self.rect.left = 0

    # Método para que la nave dispare un láser
    def disparar(self, all_sprites, laser_lista, laser_music):
        # Crear un objeto láser en la posición superior central de la nave
        laser = Laser(self.rect.centerx, self.rect.top)

        # Agregar el láser a los grupos de sprites
        all_sprites.add(laser)
        laser_lista.add(laser)

        # Reproducir el sonido del láser
        laser_music.play()