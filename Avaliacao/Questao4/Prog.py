"""Cria um rebatedor e retangulos que somem ao serem tocados por uma bola."""

from Rebatedor import rebatedor
from Retangulo import retangulo
from Bola import bola
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


def cria_lista_retangulos(quantidade):
    """Adiciona retangulos a lista."""
    x = 0
    y = 0
    larg = 80
    alt = 80
    contador = 1
    while quantidade > 0:
        color = coraleatoria()
        retangulos.append(criaretangulo(x, y, larg, alt, color))
        if contador >= 5:
            x = -(larg)
            y = y + alt
            contador = 1
        else:
            contador += 1
        x += larg
        quantidade -= 1


def criabola(center, radius, color):
    """Cria um objeto do tipo bola."""
    return bola(center, radius, color)


def criarebatedor(x, y, largura, altura, color):
    """Cria um objeto do tipo rebatedor."""
    return rebatedor(x, y, largura, altura, color)


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


def movebola():
    """Move a bola."""
    global bola

    if bola.x + bola.radius <= 400 and bola.x - bola.radius >= 0:
        bola.x += bola.movex

    elif bola.x > 400 - bola.radius:
        bola.x = 400 - bola.radius
        bola.movex = -5

    elif bola.x < 0 + bola.radius:
        bola.x = 0 + bola.radius
        bola.movex = 5

    if bola.y + bola.radius <= 400 and bola.y - bola.radius >= 0:

        bola.y += bola.movey

    elif bola.y > 400 - bola.radius:
        bola.y = 400 - bola.radius
        bola.movey = -5

    elif bola.y < 0 + bola.radius:
        bola.y = 0 + bola.radius
        bola.movey = 5


def move_rebatedor(x):
    """Move o rebatedor."""
    global rebatedor
    if rebatedor.x < 0:
        rebatedor.x = 0
    elif rebatedor.x > 400 - rebatedor.largura:
        rebatedor.x = 400 - rebatedor.largura
    else:
        rebatedor.x += x


rebatedor = criarebatedor(0, 380, 100, 20, white)
bola = criabola([200, 300], 30, white)


def colide(bola, rect):

    val = True
    if bola.y + bola.radius < rect.y:
        val = False
    if bola.y - bola.radius > rect.y + rect.altura:
        val = False
    if bola.x + bola.radius < rect.x:
        val = False
    if bola.x - bola.radius > rect.x + rect.largura:
        val = False
    if val:
        print bola.y - bola.radius > rect.y + rect.altura
    return val


def lado_colide(bola, rect):
    if bola.x < rect.x:
        return 1
    if bola.x > rect.x + rect.largura:
        return 3
    if bola.y < rect.y:
        return 2
    if bola.y > rect.y + rect.altura:
        return 4


def main():
    """Metodo main."""
    global rebatedor
    global bola
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
    cria_lista_retangulos(10)
    x_move_bola = 0
    y_move_bola = 0
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
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                bola.movex = 5
                bola.movey = 5
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
        colision = False
        movebola()
        for i in range(len(retangulos)):
            colision = colide(bola, retangulos[i])
            if colision is True:
                lado = lado_colide(bola, retangulos[i])
                if lado is 1:
                    print("Colidiu - Esquerda")
                    bola.movex = -5
                if lado is 2:
                    print("Colidiu - Cima")
                    bola.movey = -5
                if lado is 3:
                    print("Colidiu - Direita")
                    bola.movex = 5
                if lado is 4:
                    print("Colidiu - Baixo")
                    bola.movey = 5
                # break

        pygame.draw.circle(screen, bola.color, [bola.x, bola.y], bola.radius, )
        for i in range(len(retangulos)):
            colora = retangulos[i].color
            xa = retangulos[i].x
            ya = retangulos[i].y
            larga = retangulos[i].largura
            alta = retangulos[i].altura
            pygame.draw.rect(screen, colora, [xa, ya, larga, alta],)
        pygame.display.flip()


main()
