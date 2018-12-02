"""Implementa um Deque."""


class Deque:
    """Implementa um Deque."""

    def __init__(self, tamanho):
        """Inicializa o Deque."""
        self.tamanho = tamanho
        self.dados = [0] * self.tamanho
        self.first = 0
        self.last = 0

    def is_empty(self):
        """Verifica se o Deque esta vazio."""
        if self.dados[self.first] == 0 and self.dados[self.last] == 0:
            return True
        else:
            return False

    def proximo(self, valor):
        """Pula para o proximo"""
        valor += 1
        if valor >= self.tamanho:
            valor = 0
        return valor

    def pushBack(self, valor):
        """Insere um valor no fim do deque"""
        if self.dados[self.first] == 0 and self.dados[self.last] == 0:
            self.dados[self.first] = valor
        else:
            self.last = self.proximo(self.last)
            self.dados[self.last] = valor
