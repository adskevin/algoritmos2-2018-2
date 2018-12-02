

class StackUnderflow (Exception):
    """Define classe para acesso de pilha vazia"""
    pass


class Pilha:
    def __init__(self, tamanho):
        self._dados = [0]*tamanho
        self._topo = 0

    def empty(self):
        return self._topo == 0

    def push(self, valor):
        self.empty = False
        self._dados[0] = valor

    def pick(self):
        if self.empty():
            raise StackUnderflow()
        return self._dados[self._topo - 1]
