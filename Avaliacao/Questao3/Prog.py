"""Cria e move um rebatedor"""

from Rebatedor import rebatedor
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


def criarebatedor(x, y, largura, altura, color):
    """Cria um objeto do tipo rebatedor."""
    return rebatedor(x, y, largura, altura, color)


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


def move_rebatedor(x):
    """Move o rebatedor."""
    global rebatedor
    if rebatedor.x < 0:
        rebatedor.x = 0
    elif rebatedor.x > 400 - rebatedor.largura:
        rebatedor.x = 400 - rebatedor.largura
    else:
        rebatedor.x += x


rebatedor = criarebatedor(0, 380, 50, 20, coraleatoria())


def main():
    """Metodo main."""
    global rebatedor
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    rodando = True
    clock = pygame.time.Clock()
    color = rebatedor.color
    x = rebatedor.x
    y = rebatedor.y
    larg = rebatedor.largura
    alt = rebatedor.altura
    pygame.draw.rect(screen, color, [x, y, larg, alt],)
    while rodando:
        clock.tick(60)
        pygame.draw.rect(screen, black, [0, 0, 400, 400],)
        for event in pygame.event.get():
            x = 0
            if pygame.key.get_pressed()[pygame.K_UP]:
                y = -5
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                y = 5
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                x = 5
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                x = -5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False
        if rebatedor.x >= 0 and rebatedor.x <= 400:
            rebatedor.x += x
        if rebatedor.x < 0:
            rebatedor.x = 0
        if rebatedor.x > 400 - rebatedor.largura:
            rebatedor.x = 400 - rebatedor.largura
        color = rebatedor.color
        xr = rebatedor.x
        yr = rebatedor.y
        larg = rebatedor.largura
        alt = rebatedor.altura
        pygame.draw.rect(screen, color, [xr, yr, larg, alt],)
        pygame.display.flip()


main()
