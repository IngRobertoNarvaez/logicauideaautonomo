import pygame
import sys
import random

pygame.init()

# ===== Ventana =====
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

clock = pygame.time.Clock()

# ===== Colores =====
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ===== Fuente =====
title_font = pygame.font.Font(None, 72)
menu_font = pygame.font.Font(None, 40)

# ===== Estados =====
MENU = 0
GAME = 1
state = MENU

# ===== Paletas y pelota =====
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
BALL_SPEED = 5
PADDLE_SPEED = 5

player_paddle = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
enemy_paddle = pygame.Rect(WIDTH-50-PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

ball_dx = random.choice([-BALL_SPEED, BALL_SPEED])
ball_dy = random.choice([-BALL_SPEED, BALL_SPEED])

# ===== Puntaje =====
player_score = 0
enemy_score = 0
MAX_SCORE = 5
score_font = pygame.font.Font(None, 50)

# ===== Funciones =====
def draw_menu():
    screen.fill(BLACK)
    title = title_font.render("PONG", True, WHITE)
    play = menu_font.render("1. Jugar", True, WHITE)
    quit_game = menu_font.render("2. Salir", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))
    screen.blit(play, (WIDTH // 2 - play.get_width() // 2, 260))
    screen.blit(quit_game, (WIDTH // 2 - quit_game.get_width() // 2, 310))
    pygame.display.flip()

def reset_ball():
    global ball_dx, ball_dy
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_dx = random.choice([-BALL_SPEED, BALL_SPEED])
    ball_dy = random.choice([-BALL_SPEED, BALL_SPEED])

def main_game():
    global ball_dx, ball_dy, player_score, enemy_score

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED

    # Mov. enemigo simple (IA)
    if enemy_paddle.centery < ball.centery and enemy_paddle.bottom < HEIGHT:
        enemy_paddle.y += PADDLE_SPEED
    if enemy_paddle.centery > ball.centery and enemy_paddle.top > 0:
        enemy_paddle.y -= PADDLE_SPEED

    # Mover pelota
    ball.x += ball_dx
    ball.y += ball_dy

    # Rebote en paredes
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Rebote en paletas
    if ball.colliderect(player_paddle) or ball.colliderect(enemy_paddle):
        ball_dx *= -1

    # Puntaje
    if ball.left <= 0:
        enemy_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        player_score += 1
        reset_ball()

    # Dibujar
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, enemy_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Dibujar puntaje
    score_text = score_font.render(f"{player_score}  |  {enemy_score}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))

    pygame.display.flip()

    # Fin del juego
    if player_score >= MAX_SCORE or enemy_score >= MAX_SCORE:
        winner = "Jugador" if player_score >= MAX_SCORE else "CPU"
        screen.fill(BLACK)
        win_text = title_font.render(f"GANA {winner}", True, WHITE)
        screen.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2 - win_text.get_height()//2))
        pygame.display.flip()
        pygame.time.delay(3000)
        return True  # indica que el juego terminó
    return False

# ===== Bucle principal =====
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if state == MENU:
                if event.key == pygame.K_1:
                    state = GAME
                elif event.key == pygame.K_2:
                    running = False
            elif state == GAME:
                if event.key == pygame.K_ESCAPE:
                    state = MENU

    if state == MENU:
        draw_menu()
    elif state == GAME:
        game_over = main_game()
        if game_over:
            # resetear todo para volver al menú
            player_score = 0
            enemy_score = 0
            reset_ball()
            state = MENU

pygame.quit()
sys.exit()
