import pygame
from constantes import *
from nave import Nave
from explosiones import Explosion 
from enemigos import Enemigos
from funciones import *
from base_de_datos import *

crear_tablas_db()
posicion_imagen = (0,0)

pygame.init()
pygame.mixer.init()

def agregar_ememigos():
    all_sprites.add(enemigo)
    enemigos_lista.add(enemigo)
        
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) 
pygame.display.set_caption("GALAGA") 

fondo = pygame.image.load("Imagenes/91655.webp") 
fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

# ---------------- CARGAR SONIDOS -------------------:
laser_music = pygame.mixer.Sound("Sonidos/laser_music.wav") # Cargo el sonido del laser.
explosion_music = pygame.mixer.Sound("Sonidos/explosion.wav") # Cargo el sonido de la colision.
pygame.mixer.music.load("Sonidos/music.wav") # Cargo la musica general del juego.
pygame.mixer.music.set_volume(0.2) # Le doy volumen a la musica general.
pygame.mixer.music.play(loops =- 1) # Cargo la musica en un loop para que se reproduzca siempre.

fuente = pygame.font.SysFont("Arial", 26)
clock = pygame.time.Clock()
score = 0
nivel_actual = 1
ingreso = " "
textbox_rect = pygame.Rect((250, 470), (300,32))

# ------------------- EXPLOSIONES IMG ----------------------:
explosion_img = []
for i in range(5):
	archivo_img = "Imagenes/regularExplosion0{}.png".format(i)
	img = pygame.image.load(archivo_img) 
	img = pygame.transform.scale(img, (70, 70))
	explosion_img.append(img) 

# ------------------- ENEMIGOS IMG ----------------------:
escala_enemigos = (50,50)
enemigos_images = []
enemigos_lista = ["Imagenes/Enemigo.png", "Imagenes/Enemigo.png"]
for img in enemigos_lista:
    enemigos_images.append(pygame.image.load(img))

# ------------------- LISTA POR GRUPOS ----------------------:
all_sprites = pygame.sprite.Group()
enemigos_lista = pygame.sprite.Group()
laser_lista = pygame.sprite.Group()

# ----------------- CREO LA NAVE --------------------:
nave = Nave()
all_sprites.add(nave)

# ----------------- CREO LOS ENEMIGOS --------------------:
for i in range(8):
    enemigo = Enemigos(enemigos_images, nivel_actual, escala_enemigos)
    agregar_ememigos() 

#  -------------- EMPIEZA A CORRER EL JUEGO --------------:
ranking = True
menu = True
flag_correr = True
while flag_correr:
    if menu:
        mostrar_menu(pantalla, posicion_imagen, clock)
        menu = False
    
    clock.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_correr = False
        
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                nave.disparar(all_sprites, laser_lista, laser_music)

    all_sprites.update()

    # Verifica si la vida de la nave es menor o igual a 0
    if nave.vida <= 0:
        pantalla_final(pantalla, fondo, posicion_imagen, score, textbox_rect, fuente, ingreso)
        flag_correr = False
        pygame.display.flip()

    else:
        # ----------------- COLISIONES (ENEMIGOS CONTRA EL LASER) ------------:
        hits = pygame.sprite.groupcollide(enemigos_lista, laser_lista, True, True)
        for hit in hits:
            enemigo = Enemigos(enemigos_images, nivel_actual, escala_enemigos)
            agregar_ememigos()
            score += 10
            explosion_music.play() 
            explosion = Explosion(hit.rect.center, explosion_img)
            all_sprites.add(explosion)
    
        # ----------------- COLISIONES (ENEMIGOS CONTRA LA NAVE) ------------:
        hits = pygame.sprite.spritecollide(nave, enemigos_lista, True)
        for hit in hits:
            nave.vida -= 25 # Le voy restando de a 25 la vida de la nave.
            agregar_ememigos()

        # ------------------ NIVELES ------------------------------:
        if score >= 300 and nivel_actual == 1:
            nivel_actual = 2
            escala_enemigos = (70,70)
            nave.vida = 100
            dibujar_vida(pantalla, 5, 5, nave.vida)

        if score >= 700 and nivel_actual == 2:
            nivel_actual = 3
            escala_enemigos = (90,90)
            nave.vida = 100
            dibujar_vida(pantalla, 5, 5, nave.vida)


        # ---------------- BLITEO EL FONDO ----------------:
        pantalla.blit(fondo, (posicion_imagen))

        # -------------- DIBUJO TODOS LOS SPRITES --------------:
        all_sprites.draw(pantalla)

        # ------------ MOSTRAR PUNTAJE ---------:
        dibujar_texto(pantalla, str(score), 25, ANCHO_VENTANA // 2, 10)

        # ----------  MOSTRAR VIDA -------------:
        dibujar_vida(pantalla, 5, 5, nave.vida)

        # ----------  MOSTRAR NIVEL -------------:
        dibujar_texto(pantalla, f"LEVEL {nivel_actual}", "Impact", 750, 5)



    pygame.display.flip() #Va actualizando la pagina

pygame.quit() 
