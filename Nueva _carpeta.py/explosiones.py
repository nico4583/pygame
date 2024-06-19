import pygame
from constantes import *

# Definir la clase Explosion que hereda de pygame.sprite.Sprite
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, explosion_img) -> None:
        # Llamar al constructor de la clase base
        super().__init__()
        
        # Lista de imágenes que forman la animación de la explosión
        self.imagenes = explosion_img
        
        # Inicializar la imagen actual con la primera imagen de la lista
        self.image = explosion_img[0]
        
        # Obtener el rectángulo que rodea la imagen
        self.rect = self.image.get_rect()
        
        # Establecer el centro del rectángulo en la posición especificada
        self.rect.center = center
        
        # Inicializar el índice de fotograma actual
        self.frame = 0
        
        # Obtener el tiempo actual en milisegundos
        self.last_update = pygame.time.get_ticks()
        
        # Establecer la tasa de fotogramas (cada cuánto tiempo se cambia de imagen)
        self.frame_rate = 50  

    # Método para actualizar la animación de la explosión en cada fotograma
    def update(self):
        # Obtener el tiempo actual en milisegundos
        tiempo_explosion = pygame.time.get_ticks()
        
        # Verificar si ha pasado el tiempo suficiente desde el último cambio de imagen
        if tiempo_explosion - self.last_update > self.frame_rate:
            # Actualizar el tiempo del último cambio de imagen
            self.last_update = tiempo_explosion
            
            # Incrementar el índice de fotograma
            self.frame += 1
            
            # Verificar si se ha llegado al final de la lista de imágenes
            if self.frame == len(self.imagenes):
                # Si es así, eliminar la explosión (sprite)
                self.kill()
            else:
                # Si no, actualizar la imagen y el rectángulo
                center = self.rect.center
                self.image = self.imagenes[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center