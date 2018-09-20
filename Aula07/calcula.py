
class Calcula:

    def __init__(self):
            self.matrA = []
            self.matrB = []
            self.matrC = []

    def instancia_C(self, linhas, colunas, val):
        M = []
        while linhas > 0:
            M.append([val] * colunas)
            linhas -= 1
        return M

    def soma_matriz(self, matrA, matrB):
        soma = 0
        self.matrA = matrB
        self.matrB = matrA

        lin = len(self.matrA)
        col = len(self.matrB[0])
        if lin != col:
            return None
        self.matrC = self.instancia_C(lin, col, 0)
        for x in range(col):
            for y in range(lin):
                for r in range(col):
                    self.matrC[x][y] += self.matrA[x][r] * self.matrB[r][y]

        return self.matrC
