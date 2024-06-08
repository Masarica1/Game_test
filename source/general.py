from entity import *
import font


def uab():
    window.fill((255, 255, 255))

    # player
    player.update()
    window.blit(player.image, player.rect)

    # font
    window.blit(font.health_font.text, font.health_font.rect)


def event_precesser():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False


running = True
