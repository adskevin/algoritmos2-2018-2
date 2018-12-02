"""Colisao de dois retangulos."""


def teste(rect1, rect2):
    """Testa a colisao dos retangulos."""
    rect1x = rect1[0]
    rect1y = rect1[1]

    rect1dimx = rect1[2]
    rect1dimy = rect1[3]

    rect2x = rect2[0]
    rect2y = rect2[1]

    rect2dimx = rect2[2]
    rect2dimy = rect2[3]

    if rect1x + rect1dimx < rect2x:
        return False

    elif rect1y + rect1dimy < rect2y:
        return False

    elif rect1x > rect2x + rect2dimx:
        return False

    elif rect1y > rect2y + rect2dimy:
        return False

    else:
        return True
