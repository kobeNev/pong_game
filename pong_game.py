import pygame
import sys
from collections import namedtuple

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30

Rectangle = namedtuple("Rectangle", ["width", "height"])
Point = namedtuple("Point", ["x", "y"])
rectangle = Rectangle(width=30, height=30)
point = Point(x=0, y=200)

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
    global point
    global direction

    if direction == -1:
        new_point = Point(x=point.x - 5, y=point.y)
    elif direction == +1:
        new_point = Point(x=point.x + 5, y=point.y)

    if point.x <= 0:
        direction = +1
    elif point.x >= WINDOW_WIDTH - 30:
        direction = -1
    
    point = new_point

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True

    window.fill(white)

    ball = pygame.Surface((rectangle.width, rectangle.height))
    # round_ball = pygame.draw.circle(ball, (0, 0, 0), (50, 50), 50)
    ball.fill(blue)

    update_ball_position()
    window.blit(ball, (point.x, point.y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
