import pygame
import sys

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30

x = 200
y = 150
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
bg = (127, 127, 127)
FONT_SIZE = 36
direction = -1

pygame.init()
pygame.display.set_caption("Moving ball")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


def update_ball_position():
    global x
    global direction

    if direction == -1:
        x -= 5
    elif direction == +1:
        x += 5

    if x <= 0:
        direction = +1
    elif x >= WINDOW_WIDTH - 30:
        direction = -1

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True

    window.fill(white)

    ball = pygame.Surface((30, 30))
    # round_ball = pygame.draw.circle(ball, (0, 0, 0), (50, 50), 50)
    ball.fill(blue)

    update_ball_position()
    window.blit(ball, (x, y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
