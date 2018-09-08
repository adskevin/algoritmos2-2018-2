"""Exercicio de colisao"""
retang2 = [0, 0]
dimension2 = [0, 0]
retang = [0, 0]
dimension = [0, 0]
retangDimension = 0


def menu():
    global retang
    global dimension
    global retang2
    global dimension2
    retang[0] = int(input("Digite a Coordenada X para o retângulo 1: "))
    retang[1] = int(input("Digite a Coordenada Y para o retângulo 1: "))

    dimension[0] = int(input("Digite a Dimensão X do retângulo 1: "))
    dimension[1] = int(input("Digite a Dimensão Y do retângulo 1: "))
    # print(ponto)
    retang2[0] = int(input("Digite a Coordenada X para o retângulo 2: "))
    retang2[1] = int(input("Digite a Coordenada Y para o retângulo 2: "))
    # print(retang)
    dimension2[0] = int(input("Digite a Dimensão X do retângulo 2: "))
    dimension2[1] = int(input("Digite a Dimensão Y do retângulo 2: "))
    teste()


def teste():
    global retang
    global dimension
    global retang2
    global dimension2
    d11 = dimension[0]
    d12 = dimendion[1]
    d21 = dimension2[0]
    d22 = dimension2[1]
    x1 = retang[0]
    y1 = retang[1]
    x2 = retang2[0]
    y2 = retang2[1]
    isIn = False
    if x1 > x2:
        if x1+d11 <= x2+d21:
            if y11 > y21:
                if y2+d
    if (isIn):
        print("Está dentro.")
    else:
        print("Não está dentro.")


menu()
