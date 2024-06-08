from typing import Sequence

import pygame
from pygame import sprite


class Player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./resource/player/player_100_right.png')
        self.rect = self.image.get_rect()
        self.vel: list[float] = [0., 0.]

        self.rect.centerx, self.rect.centery = window_w, window_h

    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

        # 중력 가속도
        if ((self.rect.bottom < window_h) and (gravity > 0)) or ((self.rect.top > 0) and (gravity < 0)):
            self.vel[1] += gravity

        # 키 조작
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vel[0] -= 0.5
        if keys[pygame.K_d]:
            self.vel[0] += 0.5

        if keys[pygame.K_SPACE] and ((self.rect.bottom == window_h) or (self.rect.top == 0)):
            self.vel[1] -= 15 * gravity

        # 객체 이동 제한
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel[0] = 0
        if self.rect.right > window_w:
            self.rect.right = window_w
            self.vel[0] = 0
        if (self.rect.bottom > window_h) and (gravity > 0):
            self.rect.bottom = window_h
            self.vel[1] = 0
        if (self.rect.top < 0) and (gravity < 0):
            self.rect.top = 0
            self.vel[1] = 0

        self.collide()
        self.image_update()

    def collide(self):
        if self.rect.colliderect(trampoline.rect):
            if not trampoline.collide_checker:
                self.vel[1] -= 35
                trampoline.collide_checker = True
        else:
            trampoline.collide_checker = False

        if self.rect.colliderect(portal.rect):
            [self.rect.x, self.rect.y] = portal.target_position

        if self.rect.colliderect(mirror.rect):
            if not mirror.collide_checker:
                global gravity
                gravity *= -1
                mirror.collide_checker = True

        else:
            mirror.collide_checker = False

    def image_update(self):
        if gravity > 0:
            if self.vel[0] > 0:
                self.image = pygame.image.load('./resource/player/player_100_right.png')
            elif self.vel[0] < 0:
                self.image = pygame.image.load('./resource/player/player_100_left.png')
        else:
            self.image = pygame.image.load('./resource/player/player_100_reversed.png')


class Trampoline(sprite.Sprite):
    def __init__(self, position: Sequence[int]):
        super().__init__()
        self.image = pygame.image.load('./resource/trampoline.png')
        self.rect = self.image.get_rect()

        self.collide_checker = False

        [self.rect.x, self.rect.y] = position


class Portal(sprite.Sprite):
    def __init__(self, target_position: Sequence[int]):
        super().__init__()
        self.image = pygame.image.load('./resource/portal.png')
        self.rect = self.image.get_rect()

        self.target_position = target_position


class Mirror(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./resource/mirror.png')
        self.rect = self.image.get_rect()

        self.collide_checker = False


# global parameter
gravity = 1

# window setting
window_w, window_h = 1200, 900
window = pygame.display.set_mode((window_w, window_h))

# entity setting
player: Player = Player()
trampoline: Trampoline = Trampoline((window_w - 300, window_h - 55))

portal: Portal = Portal([window_w / 2, 100])
portal.rect.bottom = window_h
portal.rect.left = 0

mirror = Mirror()
mirror.rect.centerx, mirror.rect.bottom = window_w / 3, window_h
