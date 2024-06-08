from entity import *


def uab():
    window.fill((255, 255, 255))

    player.update()

    window.blit(player.image, player.rect)


def event_precesser():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False


running = True
