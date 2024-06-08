import pygame

import general

pygame.init()

# time & event setting
clock = pygame.time.Clock()


while general.running:
    general.event_precesser()
    general.uab()

    clock.tick(60)
    pygame.display.update()
pygame.quit()
