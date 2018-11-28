"""Exercicio de colisao."""


def teste(ponto, retang):
    """Testa se ponto está dentro de retangulo."""
    dimension = [0, 0]
    # print(retang[2], retang[3])
    dimension[0] = retang[2]
    dimension[1] = retang[3]
    x = retang[0]
    y = retang[1]
    isIn = False
    while x < retang[0]+dimension[0]:
        while y < retang[1]+dimension[1]:
            if ponto[0] == x:
                isIn = True
            elif ponto[1] == y:
                isIn = True
            # print(x, ".", y)
            y += 1
        x += 1
    if (isIn):
        # print("Está dentro.")
        return True
    else:
        # print("Não está dentro.")
        return False
