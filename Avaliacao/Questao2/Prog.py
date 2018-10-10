"""Criacao de 60 retangulos alinhados de 10 em 10 com cores aleatorias."""

from Retangulo import retangulo
import random
import pygame

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)
blueviolet = (138, 43, 226)
gold = (255, 215, 0)
retangulos = []


def criaretangulo(x, y, largura, altura, color):
    """Cria um objeto do tipo retangulo."""
    return retangulo(x, y, largura, altura, color)


def coraleatoria():
    """Retorna uma cor aleatoria."""
    valor = random.randint(0, 7)
    if valor == 0:
        return red
    elif valor == 1:
        return green
    elif valor == 2:
        return blue
    elif valor == 3:
        return darkBlue
    elif valor == 4:
        return white
    elif valor == 5:
        return pink
    elif valor == 6:
        return blueviolet
    elif valor == 7:
        return gold
    else:
        print("Erro na cor")


def cria_lista_retangulos(quantidade):
    """Adiciona retangulos a lista."""
    x = 10
    y = 10
    larg = 20
    alt = 20
    contador = 1
    while quantidade > 0:
        color = coraleatoria()
        retangulos.append(criaretangulo(x, y, larg, alt, color))
        if contador >= 10:
            x = -10
            y = y + alt
            contador = 1
        else:
            contador += 1
        x += larg
        quantidade -= 1


def main():
    """Metodo main."""
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    rodando = True
    clock = pygame.time.Clock()
    cria_lista_retangulos(60)
    while rodando:
        clock.tick(60)
        pygame.draw.rect(screen, black, [0, 0, 400, 400],)
        for i in range(len(retangulos)):
            # print(retangulos[i].getcolor)
            color = retangulos[i].color
            x = retangulos[i].x
            y = retangulos[i].y
            larg = retangulos[i].largura
            alt = retangulos[i].altura
            pygame.draw.rect(screen, color, [x, y, larg, alt],)
        pygame.display.flip()
        while(rodando):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # print("ESC")
                        rodando = False


main()
