"""Classe Bola."""


class bola:
    """Objeto bola."""

    def __init__(self, center, radius, color):
        """Cria uma bola."""
        self.center = center
        self.x = center[0]
        self.y = center[1]
        self.radius = radius
        self.color = color
        self.movex = 0
        self.movey = 0
