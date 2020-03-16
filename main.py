import pygame
import os
from Rose import Rose
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = 600,600
screen = pygame.display.set_mode(size)
rose = Rose(screen, size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    rose.draw()
    pygame.display.update()
