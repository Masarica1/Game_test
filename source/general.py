from entity import *
import font


def uab():
    window.fill((255, 255, 255))

    # player
    player.update()
    window.blit(player.image, player.rect)

    # font
    font.weight_font.text_convert(f'Weight: {player.weight}')
    window.blit(font.weight_font.text, font.weight_font.rect)

    # food
    food_group.draw(window)


def event_precesser():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False


running = True
