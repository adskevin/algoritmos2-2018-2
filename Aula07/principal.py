from calcula import Calcula

matrA = []
matrB = []
matrC = []


def instancia_matrizes(linhas, colunas, val):
    M = []
    while linhas > 0:
        M.append([val] * colunas)
        linhas -= 1
    return M


def main():
    calc = Calcula()
    matrA = instancia_matrizes(5, 4, 2)
    matrB = instancia_matrizes(4, 5, 2)
    matrC = calc.soma_matriz(matrA, matrB)
    print(matrC)

    matrA = instancia_matrizes(2, 2, 2)
    matrB = instancia_matrizes(2, 2, 2)
    matrC = calc.soma_matriz(matrA, matrB)
    print(matrC)


main()
