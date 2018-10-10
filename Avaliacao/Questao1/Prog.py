"""Movimentacao e colisao da bola com as extremidades da tela."""

from Bola import bola
import pygame

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)


def criabola(center, radius, color):
    """Cria um objeto do tipo bola."""
    return bola(center, radius, color)


def movebola(direction):
    """Move a bola."""
    global bola
    if bola.x + 5 <= 400 - bola.radius and direction == 0:
        bola.x += 5
        return 0
    if bola.x + 5 >= 400 - bola.radius and direction == 0:
        bola.x = 400 - bola.radius
        bola.color = red
        return 1

    if bola.x - 5 >= 0 + bola.radius and direction == 1:
        bola.x -= 5
        return 1
    if bola.x - 5 <= 0 + bola.radius and direction == 1:
        bola.x = 0 + bola.radius
        bola.color = blue
        return 0

    if bola.y + 5 <= 400 - bola.radius and direction == 2:
        bola.y += 5
        return 2
    if bola.y + 5 >= 400 - bola.radius and direction == 2:
        bola.y = 400 - bola.radius
        bola.color = green
        return 3

    if bola.y - 5 >= 0 + bola.radius and direction == 3:
        bola.y -= 5
        return 3
    if bola.y - 5 <= 0 + bola.radius and direction == 3:
        bola.y = 0 + bola.radius
        bola.color = pink
        return 2


bola = criabola([200, 50], 50, white)


def main():
    """Metodo main."""
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    rodando = True
    clock = pygame.time.Clock()
    print(bola.center)
    print(bola.x)
    print(bola.y)
    direction1 = 0
    direction2 = 2
    while rodando:
        clock.tick(60)
        pygame.draw.rect(screen, black, [0, 0, 400, 400],)
        direction1 = movebola(direction1)
        direction2 = movebola(direction2)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # print("ESC")
                    rodando = False
        print(bola.center)
        pygame.draw.circle(screen, bola.color, [bola.x, bola.y], bola.radius, )
        pygame.display.flip()


main()
