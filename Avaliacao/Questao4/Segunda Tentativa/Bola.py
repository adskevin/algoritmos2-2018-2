"""Classe Bola."""

import pygame


class bola:
    """Objeto bola."""

    def __init__(self, center, radius, color, screen_width, screen_height, screen):
        """Cria uma bola."""
        self.center = center
        self.x = center[0]
        self.y = center[1]
        self.radius = radius
        self.color = color
        self.movex = 0
        self.movey = 0
        self.allow_death = True
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen

    def inverte_x(self):
        self.movex *= -1

    def inverte_y(self):
        self.movey *= -1

    def move_bola(self):
        if self.x - self.radius <= 0:
            self.x = 0 + self.radius
            self.inverte_x()
        elif self.x + self.radius >= self.screen_width:
            self.x = self.screen_width - self.radius
            self.inverte_x()
        if self.y - self.radius <= 0:
            self.y = 0 + self.radius
            self.inverte_y()
        elif self.y + self.radius >= self.screen_height:
            if self.allow_death:
                self.color = (255, 0, 0)
                self.y = self.x = 200
                self.movex = 0
                self.movey = 0
            else:
                self.y = self.screen_height - self.radius
                self.inverte_y()
        self.x += self.movex
        self.y += self.movey
        self.draw_bola(self.screen)

    def colide(self, obj):
        if self.x + self.radius < obj.x:
            return obj
        if self.x - self.radius > obj.x + obj.largura:
            return obj
        if self.y + self.radius < obj.y:
            return obj
        if self.y - self.radius > obj.y + obj.altura:
            return obj

        obj.alive = False

        if self.x < obj.x and self.y >= obj.y and self.y <= obj.y + obj.altura:
            self.inverte_x()
        elif self.x > obj.x + obj.largura and self.y >= obj.y and self.y <= obj.y + obj.altura:
            self.inverte_x()
        elif self.y < obj.y and self.x >= obj.x and self.x <= obj.x + obj.largura:
            self.inverte_y()
        elif self.y > obj.y + obj.altura and self.x >= obj.x and self.x <= obj.x + obj.largura:
            self.inverte_y()

        return obj

    def draw_bola(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius, )
