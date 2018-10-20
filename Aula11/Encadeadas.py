"""Define um no da lista encadeada."""


class No:
    def __init__(self, valor):
        """Inicializa no."""
        self.dado = valor
        self.proximo = None


class Lista:
    """Define lista encadeada."""

    def __init__(self):
        """Inicializa uma nova lista."""
        self.head = None
        self.tail = None

    def append(self, valor):
        """Adiciona um valor ao final da lista."""
        if self.tail is None:
            self.head = self.tail = No(valor)
        else:
            self.tail.proximo = No(valor)
            self.tail = self.tail.proximo

    def addFirst(self, valor):
        real_head = self.head
        self.head = No(valor)
        self.head.proximo = real_head

    def removeFirst(self):
        self.head = self.head.proximo

    def removeLast(self):
        i = self.head
        anterior = None
        if self.head.proximo is None:
            self.head = self.proximo = None
        else:
            while i.proximo is not None:
                # print(i.dado)
                anterior = i
                i = i.proximo
                if i.proximo is None:
                    # print'Dado:', anterior.dado
                    anterior.proximo = None
                    self.tail = anterior


x = Lista()
x.append(1)
x.append(2)
x.append(3)
x.append(4)
x.append(5)
x.addFirst(4)
x.addFirst(5)
x.removeFirst()
x.removeLast()
i = x.head
while i is not None:
    print(i.dado)
    i = i.proximo
