import pygame
from pygame import sprite


class Player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./resource/player_100.png')
        self.rect = self.image.get_rect()
        self.vel: list[float] = [0., 0.]

        self.rect.bottom = window_h

    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

        # 중력 가속도
        if self.rect.bottom < window_h:
            self.vel[1] += 1

        # 키 조작
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vel[0] -= 0.5
        if keys[pygame.K_d]:
            self.vel[0] += 0.5

        if keys[pygame.K_SPACE] and (self.rect.bottom == window_h):
            self.vel[1] -= 15

        # 객체 이동 제한
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel[0] = 0
        if self.rect.right > window_w:
            self.rect.right = window_w
            self.vel[0] = 0
        if self.rect.bottom > window_h:
            self.rect.bottom = window_h
            self.vel[1] = 20


# window setting
window_w, window_h = 1200, 900
window = pygame.display.set_mode((window_w, window_h))

# entity setting
player = Player()
