import pygame
import sys

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30
done = False
white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

bg = (127,127,127) 

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
    # er zijn nog veel meer types events
        window.fill(bg)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        font = pygame.font.SysFont("Arial", 36)
    txtsurf = font.render("Hello, World", True, white)
    window.blit(txtsurf,(200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))
    # je zou hier ook update() kunnen tegenkomen
    # maar dat is niet voor full-screen updates
    # vereist meer fine-tuning
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)