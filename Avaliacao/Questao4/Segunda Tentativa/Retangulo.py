"""Classe retangulo."""


class retangulo:
    """Objeto retangulo."""

    def __init__(self, x, y, l, a, color):
        """Cria um retangulo."""
        self.x = x
        self.y = y
        self.largura = l
        self.altura = a
        self.color = color
        self.alive = True
