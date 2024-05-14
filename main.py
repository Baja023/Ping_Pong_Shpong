import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Основные параметры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Пинг-Понг")

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)

# Элементы игры
ball_size = 20
paddle_width, paddle_height = 10, 100
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)
paddle1 = pygame.Rect(10, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle2 = pygame.Rect(width - 10 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Скорость элементов
ball_speed_x, ball_speed_y = 7 * random.choice((1, -1)), 7 * random.choice((1, -1))
paddle_speed = 10
computer_difficulty = 0.2  # 0.1 - легко, 0.2 - нормально, 0.3 - сложно

# Счёт
score_font = pygame.font.Font(None, 36)
score1, score2 = 0, 0

# Игровой цикл
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s]:
        paddle1.y += paddle_speed
    if keys[pygame.K_UP]:
        paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle2.y += paddle_speed

    # Управление компьютером (раскомментируйте для игры против компьютера)
    # if ball.x > width // 2:
    #     if paddle2.centery < ball.centery:
    #         paddle2.y += paddle_speed * computer_difficulty
    #     if paddle2.centery > ball.centery:
    #         paddle2.y -= paddle_speed * computer_difficulty

    # Движение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Столкновения
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # За пределы поля
    if ball.left <= 0:
        score2 += 1
        ball.center = (width // 2, height // 2)
        ball_speed_x *= random.choice((1, -1))
    if ball.right >= width:
        score1 += 1
        ball.center = (width // 2, height // 2)
        ball_speed_x *= random.choice((1, -1))

    # Отрисовка
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)
    pygame.draw.ellipse(screen, white, ball)
    score_text = score_font.render(f"{score1} : {score2}", True, white)
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
