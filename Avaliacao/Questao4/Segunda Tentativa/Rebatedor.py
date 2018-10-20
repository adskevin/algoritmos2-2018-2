"""Classe rebaterod."""

import pygame


class rebatedor:
    """Objeto rebatedor."""

    def __init__(self, x, y, l, a, color, screen_width, screen_height, screen):
        """Cria um rebatedor."""
        self.x = x
        self.y = y
        self.largura = l
        self.altura = a
        self.color = color
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.movex = 0

    def move_rebatedor(self):
        """Move o rebatedor"""
        if (self.x >= 0 and self.x <= self.screen_width - self.largura):
            if (self.x + self.movex) < 0:
                self.x = 0
            elif (self.x + self.movex + self.largura > self.screen_width):
                self.x = self.screen_width - self.largura
            else:
                self.x += self.movex
            self.draw_rebatedor(self.screen)

    def draw_rebatedor(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.largura, self.altura],)
