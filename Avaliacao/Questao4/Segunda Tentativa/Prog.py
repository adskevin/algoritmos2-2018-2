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


def criaretangulo(x, y, largura, altura, color):
    """Cria um objeto do tipo retangulo."""
    return retangulo(x, y, largura, altura, color)


def cria_lista_retangulos(quantidade):
    """Adiciona retangulos a lista."""
    x = 0
    y = 0
    larg = 40
    alt = 40
    contador = 1
    while quantidade > 0:
        color = coraleatoria()
        retangulos.append(criaretangulo(x, y, larg, alt, color))
        if contador >= 10:
            x = -(larg)
            y = y + alt
            contador = 1
        else:
            contador += 1
        x += larg
        quantidade -= 1


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


def main():
    """Metodo main."""
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    rodando = True
    clock = pygame.time.Clock()
    bola1 = bola([200, 300], 15, white, 400, 400, screen)
    bola1.draw_bola(screen)
    rebatedor1 = rebatedor(150, 390, 100, 10, red, 400, 400, screen)
    rebatedor1.draw_rebatedor(screen)
    cria_lista_retangulos(40)
    for i in range(len(retangulos)):
        colora = retangulos[i].color
        xa = retangulos[i].x
        ya = retangulos[i].y
        larga = retangulos[i].largura
        alta = retangulos[i].altura
        pygame.draw.rect(screen, colora, [xa, ya, larga, alta],)
    while rodando:
        clock.tick(60)
        pygame.draw.rect(screen, black, [0, 0, 400, 400],)
        for event in pygame.event.get():
            rebatedor1.movex = 0
            if pygame.key.get_pressed()[pygame.K_UP]:
                pass
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                pass
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                rebatedor1.movex = 10
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                rebatedor1.movex = -10
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                bola1.movex = 5
                bola1.movey = 5
                bola1.color = white
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False
        for i in range(len(retangulos)):
            if retangulos[i].alive is True:
                colora = retangulos[i].color
                xa = retangulos[i].x
                ya = retangulos[i].y
                larga = retangulos[i].largura
                alta = retangulos[i].altura
                retangulos[i] = bola1.colide(retangulos[i])
                if retangulos[i].alive is False:
                    break
        for i in range(len(retangulos)):
            if retangulos[i].alive is True:
                colora = retangulos[i].color
                xa = retangulos[i].x
                ya = retangulos[i].y
                larga = retangulos[i].largura
                alta = retangulos[i].altura
                pygame.draw.rect(screen, colora, [xa, ya, larga, alta],)
        bola1.colide(rebatedor1)
        bola1.move_bola()
        rebatedor1.move_rebatedor()
        pygame.display.flip()


main()
