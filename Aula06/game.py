import pygame
from estrela import Estrela
import random
from nave import Nave

estrelas = []
num_estrelas = 40
vel_mult = 2
nave = Nave()
nyan = pygame.image.load("./imgs/nyan.png")


GREY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def criacao(param):
    if param == 0:
        x = random.randint(0, 800)
    elif param == 1:
        x = 800
    y = random.randint(0, 600)
    vel = random.randint(1, 3)

    estrela = Estrela()
    estrela.set_coord_x(x)
    estrela.set_coord_y(y)
    estrela.set_vel(vel)

    return estrela


def instancia_estrelas():
    global num_estrelas
    qtd = 0
    while qtd < num_estrelas:
        estrelas.append(criacao(0))
        qtd += 1


def instancia_nave():
    nave = Nave()
    nave.set_x = 100
    nave.set_y = 100


def controle():
    if event.key == pygame.K_UP:
        if nave.get_y() >= 0:
            nave.set_y(nave.get_y() - 5)
    if event.key == pygame.K_DOWN:
        if nave.get_y() <= 600:
            nave.set_y(nave.get_y() + 5)
    if event.key == pygame.K_LEFT:
        if nave.get_x() >= 0:
            nave.set_x(nave.get_x() - 5)
    if event.key == pygame.K_RIGHT:
        if nave.get_x() <= 800:
            nave.set_x(nave.get_x() + 5)


def main():
    global num_estrelas
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    rodando = True

    instancia_estrelas()
    instancia_nave()
    # clock = pygame.time.Clock()
    while rodando:
        # clock.tick(60)
        # screen.fill((0, 0, 0))
        for event in pygame.event.get():
            x = 0
            y = 0

            if pygame.key.get_pressed()[pygame.K_UP]:
                print ("K_UP = True")
                y = -5
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                print ("K_DOWN = True")
                y = 5
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                print ("K_RIGHT = True")
                x = 5
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                print ("K_LEFT = True")
                x = -5

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False

        # pygame.draw.rect(screen, BLACK, [nave.get_x(), nave.get_y(), 10, 5],)
        if nave.get_y() >= 0 and nave.get_y() <= 600:
            print ("Entrou em draw", y)
            print (nave.get_y())
            nave.set_y(nave.get_y() + y)
            if nave.get_y() < 0:
                nave.set_y(0)
            if nave.get_y() > 595:
                nave.set_y(595)
            print (nave.get_y())

        if nave.get_x() >= 0 and nave.get_x() <= 800:
            print ("Entrou em draw", x)
            print (nave.get_x())
            nave.set_x(nave.get_x() + x)
            if nave.get_x() < 0:
                nave.set_x(0)
            if nave.get_x() > 790:
                nave.set_x(790)
            print (nave.get_x())

        # pygame.draw.rect(screen, WHITE, [nave.get_x(), nave.get_y(), 10, 5],)
        qtd = 0

        # screen.blit(nyan, (200, 200))



        pygame.draw.rect(screen, BLACK, [nave.get_x(), nave.get_y(), 80, 50],)
        screen.blit(pygame.transform.scale(nyan, (80, 50)), (nave.get_x(), nave.get_y()))
        while qtd < num_estrelas:
            pygame.draw.rect(screen, BLACK, [estrelas[qtd].get_x(), estrelas[qtd].get_y(), estrelas[qtd].get_vel(), estrelas[qtd].get_vel()],)
            estrelas[qtd].set_coord_x(estrelas[qtd].get_x()-(estrelas[qtd].get_vel() * vel_mult))
            if estrelas[qtd].get_x() <= 0:
                estrelas[qtd] = criacao(1)
            pygame.draw.rect(screen, GREY, [estrelas[qtd].get_x(), estrelas[qtd].get_y(), estrelas[qtd].get_vel(), estrelas[qtd].get_vel()],)
            pygame.display.flip()
            qtd += 1


if __name__ == "__main__":
    # call the main function
    main()
