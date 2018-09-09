# First object test


from estrela import Estrela
import random

estrelas = []
num_estrelas = 2
vel_mult = 5


def primeiro_teste():
    # instancia do objeto da classe Estrela
    estrela1 = Estrela()

    # impressao dos valores para teste
    print estrela1.get_x()
    print estrela1.get_y()
    print estrela1.get_vel()

    # set dos valores para teste
    estrela1.set_coord_x(500)
    estrela1.set_coord_y(500)
    estrela1.set_vel(2)

    # nova impressao para confirmacao de mudanca de valores
    print estrela1.get_x()
    print estrela1.get_y()
    print estrela1.get_vel()


# criar 5 estrelas com posicoes aleatorias dentro de padroes
def criacao():
    # x = random.randint(0, 800)
    x = 800
    y = random.randint(0, 600)
    vel = random.randint(1, 3)

    estrela = Estrela()
    estrela.set_coord_x(x)
    estrela.set_coord_y(y)
    estrela.set_vel(vel)

    return estrela


# metodo principal
def main():
    global num_estrelas
    qtd = 0
    while qtd < num_estrelas:
        estrelas.append(criacao())
        print "===================="
        print estrelas[qtd].get_x()
        print estrelas[qtd].get_y()
        print estrelas[qtd].get_vel()
        qtd += 1


# mover as estrelas conforme pedido ao pressionar enter
def move():
    global num_estrelas
    a = input("Pressione enter.")
    if a == 1:
        return 1
    qtd = 0
    while qtd < num_estrelas:
        estrelas[qtd].set_coord_x(estrelas[qtd].get_x()-(estrelas[qtd].get_vel() * vel_mult))
        if estrelas[qtd].get_x() <= 0:
            estrelas[qtd] = criacao()
        print "===================="
        print estrelas[qtd].get_x()
        print estrelas[qtd].get_y()
        print estrelas[qtd].get_vel()
        qtd += 1


main()
while True:
    if move() == 1:
        break
