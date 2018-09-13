import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    rodando = True

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
            if event.type == pygame.QUIT:
                rodando = False


if __name__ == "__main__":
    # call the main function
    main()
