import pygame
from constantes import *
from base_de_datos import *

# Función para dibujar texto en la pantalla
def dibujar_texto(surface, texto, fuente, x, y):
    fuente = pygame.font.SysFont("Impact", 30)
    texto_surface = fuente.render(texto, True, COLOR_ROJO)
    texto_rect = texto_surface.get_rect()
    texto_rect.midtop = (x, y)
    surface.blit(texto_surface, texto_rect)

# Función para dibujar la barra de vida en la pantalla
def dibujar_vida(surface, x, y, porcentaje):
    # Definir dimensiones de la barra de vida
    barra_vida_largo = 100
    barra_vida_alto = 10
    # Calcular la longitud de la barra de vida basada en el porcentaje proporcionado
    cantidad_vida = (porcentaje / 100) * barra_vida_largo
    # Crear rectángulos para la barra de vida y el borde
    borde = pygame.Rect(x, y, barra_vida_largo, barra_vida_alto)
    cantidad_vida = pygame.Rect(x, y, cantidad_vida, barra_vida_alto)
    # Dibujar la barra de vida y el borde en la pantalla
    pygame.draw.rect(surface, COLOR_VERDE, cantidad_vida)
    pygame.draw.rect(surface, COLOR_BLANCO, borde, 2)

# Función para mostrar el menú principal del juego
def mostrar_menu(pantalla, posicion_imagen, clock):
    # Cargar imágenes y fondo para el menú
    fondo = pygame.image.load("Imagenes/91655.webp") 
    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    imagen_play = pygame.image.load("Imagenes/Play.jpg")
    imagen_play = pygame.transform.scale(imagen_play, (200, 80))

    imagen_ranking = pygame.image.load("Imagenes/Ranking.jpg")
    imagen_ranking = pygame.transform.scale(imagen_ranking, (200, 80))

    # Mostrar elementos en la pantalla
    pantalla.blit(fondo, (posicion_imagen))
    pantalla.blit(imagen_play , ((300, 170)))
    pantalla.blit(imagen_ranking , (300, 290))
    dibujar_texto(pantalla, "GALAGA", 65, ANCHO_VENTANA // 2, ALTO_VENTANA // 6)
    pygame.display.flip()

    # Esperar a que el usuario realice una acción
    esperar = True
    while esperar:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Obtener la posición del clic del mouse
                posicion_click = list(evento.pos)
                # Verificar si se hizo clic en "Play" o "Ranking"
                if 300 <= posicion_click[0] <= 500 and 170 <= posicion_click[1] <= 250:
                    esperar = False
                elif 300 <= posicion_click[0] <= 500 and 290 <= posicion_click[1] <= 370:
                    mostrar_ranking(pantalla, posicion_imagen, clock)

# Función para mostrar el ranking de jugadores
def mostrar_ranking(pantalla, posicion_imagen, clock):
    # Cargar imágenes y fondo para la pantalla de ranking
    fondo = pygame.image.load("Imagenes/91655.webp") 
    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    pantalla.blit(fondo, (posicion_imagen))

    # Obtener el ranking de jugadores
    ranking = obtener_ranking()

    # Mostrar el ranking en la pantalla
    dibujar_texto(pantalla, "Precione ESC para volver al menu", "Impact", ANCHO_VENTANA // 2, ALTO_VENTANA - 500)

    y_pos = 200  
    for i, (ingreso, score) in enumerate(ranking, start=1):
        texto = f"{i}. {ingreso}: {score}"
        dibujar_texto(pantalla, texto, "Impact", ANCHO_VENTANA // 2, y_pos)
        y_pos += 50 

    pygame.display.flip()

    # Esperar a que el usuario realice una acción
    esperar = True
    while esperar:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    esperar = False
                    mostrar_menu(pantalla, posicion_imagen, clock)

# Función para mostrar la pantalla final del juego
def pantalla_final(pantalla, fondo, posicion_imagen, score, textbox_rect, fuente, ingreso):
    pantalla.blit(fondo, (posicion_imagen))
    # Mostrar información sobre el juego terminado
    dibujar_texto(pantalla, "¡Juego Terminado!", "Impact", ANCHO_VENTANA // 2, ALTO_VENTANA // 3)
    dibujar_texto(pantalla, f"Score: {score}", "Impact", ANCHO_VENTANA // 2, ALTO_VENTANA // 2)
    dibujar_texto(pantalla, "Ingresar nombre: ", "Impact", ANCHO_VENTANA // 2, ALTO_VENTANA - 200)
    dibujar_texto(pantalla, "Precione ESC para salir", "Impact", ANCHO_VENTANA // 2, ALTO_VENTANA - 50)

    esperar_tecla = True
    
    while esperar_tecla:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                esperar_tecla = False

            elif evento.type == pygame.KEYDOWN:
                # Manejar eventos de teclado
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1] 
                elif evento.key == pygame.K_RETURN:
                    insertar_jugadores(ingreso, score)
                    print("Texto ingresado:", ingreso)
                elif evento.key == pygame.K_ESCAPE:
                    esperar_tecla = False
                    print("Saliste del Juego")
                else:
                    ingreso += evento.unicode

        # Dibujar el cuadro de texto para ingresar el nombre
        pygame.draw.rect(pantalla, COLOR_BLANCO, textbox_rect, 2)
        font_input_surface = fuente.render(ingreso, True, COLOR_BLANCO)
        pantalla.blit(font_input_surface, (textbox_rect.x + 5, textbox_rect.y + 5))
        pygame.display.flip()


