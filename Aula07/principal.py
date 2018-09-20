

matrA = []
matrB = []
matrC = []


def instancia_matrizes(linhas, colunas):
    M = []
    while linhas > 0:
        M.append([2] * colunas)
        linhas -= 1
    return M


def soma_matriz(matrA, matrB):
    soma = 0
    lin = len(matrA)
    col = len(matrB[0])
    if lin != col:
        return None
    C = instancia_matrizes(lin, col)

    for x in range(lin):
        for y in range(col):
            for r in range(len(matrA[0])):
                C[x][y] += matrA[x][r] * matrB[r][y]

    return C


def main():
    matrA = instancia_matrizes(2, 1)
    matrB = instancia_matrizes(1, 2)

    print(matrA)
    print(matrB)
    print(soma_matriz(matrA, matrB))


main()
