
class No:

    def __init__(self, val):
        self.dado = val
        self.proximo = None
        self.anterior = None


class Lista:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def set_first(self, valor):  # Adiciona o primeiro elemento na lista
        self.head = No(valor)
        self.tail = self.head
        self.proximo = None

    def append(self, valor):  # Adiciona um elemento no final da lista
        if (self.head is None):
            self.set_first(valor)

        else:
            atual = self.tail
            self.tail = No(valor)
            self.tail.anterior = atual
            atual.proximo = self.tail

        self.size += 1

    def addFirst(self, valor):  # Adiciona um elemento no comeco da lista
        if (self.head is None):
            self.set_first(valor)

        else:
            novo_no = No(valor)
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no
            novo_no.anterior = None

        self.size += 1

    def removeFirst(self):  # Remove o primeiro elemento da lista
        if(self.head is None):  # Verifica se a lista nao esta vazia
            return
        else:
            new_head = self.head.proximo
            new_head.anterior = None
            self.head = new_head
        self.size -= 1

    def removeLast(self):  # Remove o ultimo elemento da lista
        if(self.head is None):
            return
        else:
            self.tail = self.tail.anterior
            self.tail.proximo = None
        self.size -= 1

    def listSize(self):  # Retorna o tamanho da lista
        return self.size

    def remove(self, valor):  # Remove os objetos com dado igual a "valor"
        atual = self.head
        while atual is not None:  # Enquanto atual nao for None
            if atual.dado == valor:
                if atual == self.head:  # Se atual for o head
                    self.head = atual.proximo
                    self.head.anterior = None
                    self.size -= 1
                elif atual == self.tail:  # Se o atual for o tail
                    self.tail = self.tail.anterior
                    self.tail.proximo = None
                    atual = self.tail.anterior
                    self.size -= 1
                else:  # Se nao for nem head nem tail
                    anterior = atual.anterior
                    proximo = atual.proximo
                    anterior.proximo = proximo
                    proximo.anterior = anterior
                    self.size -= 1
            atual = atual.proximo

    def pop(self):  # Elimina ultimo elemento e o retorna
        valor = self.tail
        self.tail = self.tail.anterior
        self.tail.proximo = None
        self.size -= 1
        return valor

    def first(self):  # Retorna o primeiro elemento da lista
        if self.head is not None:
            return self.head

    def last(self):  # Retorna o ultimo elemento da lista
        if self.head is not None:
            return self.tail

    def ord_append(self, valor):
        atual = self.head
        novo_no = No(valor)
        while atual is not None:
            proximo = atual.proximo
            if novo_no.dado <= proximo.dado:
                pass


x = Lista()
x.append(1)
x.append(2)
x.append(2)
x.append(3)
x.append(3)
print "Pop: ", x.pop().dado
print "Size: ", x.listSize()
print "First: ", x.first().dado
print "Last: ", x.last().dado
print

i = x.head
while i is not None:
    anterior = i.anterior
    proximo = i.proximo
    print "Atual: ", i.dado
    if anterior is not None:
        print "Anterior: ", anterior.dado
    else:
        print "Anterior: None"
    if proximo is not None:
        print "Proximo: ", proximo.dado
    else:
        print "Proximo: None"
    i = i.proximo
    print
