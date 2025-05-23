import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuración de las paletas y la pelota
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10

# Posiciones iniciales
player1_pos = [10, HEIGHT // 2 - PADDLE_HEIGHT // 2]
player2_pos = [WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2]
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [4, 4]

# Velocidad de las paletas
paddle_speed = 6

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Puntuaciones
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)

# Bucle principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles de las paletas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_pos[1] > 0:
        player1_pos[1] -= paddle_speed
    if keys[pygame.K_s] and player1_pos[1] < HEIGHT - PADDLE_HEIGHT:
        player1_pos[1] += paddle_speed
    if keys[pygame.K_UP] and player2_pos[1] > 0:
        player2_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and player2_pos[1] < HEIGHT - PADDLE_HEIGHT:
        player2_pos[1] += paddle_speed

    # Movimiento de la pelota
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Colisión con la parte superior e inferior
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - BALL_SIZE:
        ball_speed[1] = -ball_speed[1]

    # Colisión con las paletas
    if (ball_pos[0] <= player1_pos[0] + PADDLE_WIDTH and
        player1_pos[1] < ball_pos[1] < player1_pos[1] + PADDLE_HEIGHT):
        ball_speed[0] = -ball_speed[0]

    if (ball_pos[0] >= player2_pos[0] - BALL_SIZE and
        player2_pos[1] < ball_pos[1] < player2_pos[1] + PADDLE_HEIGHT):
        ball_speed[0] = -ball_speed[0]

    # Puntuación y reinicio de la pelota
    if ball_pos[0] <= 0:
        player2_score += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [4, 4]
    if ball_pos[0] >= WIDTH:
        player1_score += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [-4, -4]

    # Dibujar en la pantalla
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (*player1_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (*player2_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (*ball_pos, BALL_SIZE, BALL_SIZE))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Mostrar puntuaciones
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (WIDTH // 4, 20))
    screen.blit(player2_text, (WIDTH * 3 // 4, 20))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    clock.tick(60)