import json

import pygame

pygame.init()

with open('./resource/setting.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    window_w = data['window_w']
    window_h = data['window_h']


class Font:
    def __init__(self, size: int, text: str):
        super().__init__()
        self.font: pygame.font.Font = pygame.font.Font(None, size)
        self.text: pygame.Surface = self.font.render(text, True, (0, 0, 0))
        self.rect: pygame.Rect = self.text.get_rect()

    def text_convert(self, text: str):
        self.text = self.font.render(text, True, (0, 0, 0))


weight_font = Font(64, 'Weight: ?')
weight_font.rect.right = window_w - 50
weight_font.rect.top = 25
