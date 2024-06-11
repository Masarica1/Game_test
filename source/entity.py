import json
from typing import Sequence

import pygame
from pygame import sprite

with open('../resource/setting.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    window_w = data['window_w']
    window_h = data['window_h']


class Player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../resource/player/player_100.png')
        self.rect = self.image.get_rect()
        self.vel: list[float] = [0., 0.]

        self.weight = 100

        self.rect.bottom = window_h
        self.rect.centerx = window_w / 2

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

        self.collide()

    def collide(self):
        for food in sprite.spritecollide(self, food_group, True):
            self.weight += food.weight


class Chicken(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../resource/food/chicken.png')
        self.rect = self.image.get_rect()
        self.weight = 5


# window setting
window = pygame.display.set_mode((window_w, window_h))

# entity setting
player = Player()
food_group = pygame.sprite.Group()

food_1 = Chicken()
food_1.rect.x = 100
food_1.rect.bottom = window_h
# noinspection PyTypeChecker
food_group.add(food_1)

