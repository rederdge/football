import random
import pygame
import sys

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 800, 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

background_img = pygame.image.load("football_place.png")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

player1_img = pygame.image.load("fplayer.png")
player2_img = pygame.image.load("splayer.png")
ball_img = pygame.image.load("ball.png")

player_size = 40
ball_size = 30
goal_size = (10, 100)

player1 = pygame.Rect(100, HEIGHT // 2, player_size, player_size)
player2 = pygame.Rect(WIDTH - 140, HEIGHT // 2, player_size, player_size)
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, ball_size, ball_size)
goal1 = pygame.Rect(0, HEIGHT // 2 - goal_size[1] // 2, * goal_size)
goal2 = pygame.Rect(WIDTH - goal_size[0], HEIGHT // 2 - goal_size[1] // 2, * goal_size)


ball_speed = [4, 4]
speed = 5

score1 = 0
score2 = 0
start_ticks = pygame.time.get_ticks()
font = pygame.font.SysFont(None, 48)

running = True
while running:
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # Гравець 1 — обмеження по полю
    if keys[pygame.K_w] and player1.top > 0: player1.y -= speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT: player1.y += speed
    if keys[pygame.K_a] and player1.left > 0: player1.x -= speed
    if keys[pygame.K_d] and player1.right < WIDTH: player1.x += speed

    # Гравець 2 — обмеження по полю
    if keys[pygame.K_UP] and player2.top > 0: player2.y -= speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT: player2.y += speed
    if keys[pygame.K_LEFT] and player2.left > 0: player2.x -= speed
    if keys[pygame.K_RIGHT] and player2.right < WIDTH: player2.x += speed

    # Рух м'яча
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Відскок м'яча від стінок
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] *= -1

    # Відскок м'яча від гравців
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] *= -1

    # Гол
    if ball.colliderect(goal1):
        print('Гравець 2 забив гол!')
        score2 += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed[0] = abs(ball_speed[0])
    elif ball.colliderect(goal2):
        print("Гравець 1 забив гол!")
        score1 += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed[0] = -abs(ball_speed[0])

    # Вивід рахунку та часу
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    minutes = seconds // 60
    sec = seconds % 60
    time_str = f"{minutes:02}:{sec:02}"

    score_text = font.render(f"{score1} : {score2}", True, BLACK)
    time_text = font.render(time_str, True, BLACK)
    # Рахунок по центру зверху
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))
    # Час під рахунком
    screen.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, 10 + score_text.get_height() + 5))

    screen.blit(pygame.transform.scale(player1_img, (player_size, player_size)), player1.topleft)
    screen.blit(pygame.transform.scale(player2_img, (player_size, player_size)), player2.topleft)
    screen.blit(pygame.transform.scale(ball_img, (ball_size, ball_size)), ball.topleft)
    pygame.draw.rect(screen, WHITE, goal1)
    pygame.draw.rect(screen, WHITE, goal2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


















