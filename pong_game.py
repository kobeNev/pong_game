import pygame
import sys

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
    # er zijn nog veel meer types events
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # je zou hier ook update() kunnen tegenkomen
    # maar dat is niet voor full-screen updates
    # vereist meer fine-tuning
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)