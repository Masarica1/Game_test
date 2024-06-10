from entity import *


def uab():
    window.fill((255, 255, 255))

    # trampoline
    window.blit(trampoline.image, trampoline.rect)

    # portal
    window.blit(portal.image, portal.rect)

    # mirror
    window.blit(mirror.image, mirror.rect)

    # chimney
    chimney.update()
    window.blit(chimney.siwoo.image, chimney.siwoo.rect)
    window.blit(chimney.image, chimney.rect)

    # player
    player.update()
    window.blit(player.image, player.rect)


def event_precesser():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False


running = True
