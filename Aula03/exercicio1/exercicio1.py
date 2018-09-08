"""Exercicio de colisao"""
ponto = [0, 0]
retang = [0, 0]
retangDimension = 0
dimension = [0, 0]


def menu():
    global ponto
    global retang
    global dimension
    ponto[0] = int(input("Digite a Coordenada X para o ponto: "))
    ponto[1] = int(input("Digite a Coordenada Y para o ponto: "))
    # print(ponto)
    retang[0] = int(input("Digite a Coordenada X para o retângulo: "))
    retang[1] = int(input("Digite a Coordenada Y para o retângulo: "))
    # print(retang)
    dimension[0] = int(input("Digite a Dimensão X do retângulo: "))
    dimension[1] = int(input("Digite a Dimensão Y do retângulo: "))
    teste()


def teste():
    global retang
    global dimension
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
        print("Está dentro.")
    else:
        print("Não está dentro.")


menu()
