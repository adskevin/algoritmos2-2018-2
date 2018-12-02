"""Lista duplamente encadeada com busca indexada."""
import random


class No:
    """Classe no."""

    def __init__(self, val):
        """Metodo construtor do no."""
        self.dado = val
        self.proximo = None
        self.anterior = None


class Lista:
    """Clases lista."""

    def __init__(self):
        """Metodo construtor da lista."""
        self.head = None
        self.tail = None
        self.size = 0
        self.index_list = None

    def listSize(self):
        """Retorna o tamanho da lista."""
        return self.size

    def first(self):
        """Retorna o primeiro elemento da lista."""
        if self.head is not None:
            return self.head

    def last(self):
        """Retorna o ultimo elemento da lista."""
        if self.head is not None:
            return self.tail

    def ord_append(self, valor):
        """Inclusao ordenada de valores."""
        self.index_list = None
        obj = self.head
        if obj is None:  # Se a lista estiver vazia
            new_knot = No(valor)
            self.head = new_knot
            self.tail = new_knot
            self.size += 1
        elif valor <= obj.dado:  # Se o valor for o primeiro da lista
            new_knot = No(valor)
            old_head = self.head
            new_knot.proximo = old_head
            old_head.anterior = new_knot
            self.head = new_knot
            self.size += 1
        elif valor >= self.tail.dado:  # Se o valor for o ultimo da lista
            new_knot = No(valor)
            old_tail = self.tail
            new_knot.anterior = old_tail
            old_tail.proximo = new_knot
            self.tail = new_knot
            self.size += 1
        else:
            while obj.proximo is not None:  # Analiza o valor do proximo objeto
                if valor <= obj.proximo.dado:  # Se o valor for menor ou igual ao proximo
                    new_knot = No(valor)
                    proximo = obj.proximo
                    obj.proximo = new_knot
                    new_knot.anterior = obj
                    proximo.anterior = new_knot
                    new_knot.proximo = proximo
                    self.size += 1
                    break
                obj = obj.proximo

    def create_index_list(self):
        """Cria a lista de indices."""
        obj_list = self.head
        if self.index_list is None:
            self.index_list = Lista()
        index_list = self.index_list
        if index_list.head is None:
            index_list.head = No(obj_list)
            index_list.tail = index_list.head
        x = 0
        while x < 10:
            i = 0
            while i < 10:
                if obj_list.proximo is not None:
                    obj_list = obj_list.proximo
                else:
                    break
                i += 1
            index_list.ord_append(obj_list)
            x += 1

    def print_list_simple(self):
        """Impressao simples da lista."""
        i = self.head
        while i is not None:
            print i.dado
            i = i.proximo

    def print_list_simple_2(self):
        """Impressao utilizada para imprimir o dado do dado do indice."""
        i = self.head
        while i.proximo is not None:
            i_dado = i.dado
            print i_dado.dado
            i = i.proximo

    def print_list(self):
        """Impressao utilizada para debug."""
        i = self.head
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

    def insert_valores(self, quantidade):
        """Insere uma quantidade definida de valores aleatorios."""
        for i in range(quantidade):
            rand = random.randint(0, 200)
            self.ord_append(rand)

    def insert_valores_ord(self, quantidade):
        """Insere uma quantidade definida de valores ordenados."""
        for i in range(quantidade):
            self.ord_append(i)

    def find(self, valor):
        """Encontra um valor na lista e retorna o no da lista."""
        self.create_index_list()
        i_index = self.index_list.head
        while i_index is not None:
            i_list = i_index.dado  # Aqui contem o objeto correspondente ao indice
            if not(valor >= self.head.dado and valor <= self.tail.dado):  # Verifica se o valor esta dentro da lista
                print "O valor nao esta na lista."
                return None
            elif i_list.dado >= valor:
                print "Index encontrado:", i_list.dado  # Dado do objeto
                while i_list.dado > valor:
                    i_list = i_list.anterior
                print "Saiu do while com o valor:", i_list.dado
                if i_list.dado == valor:
                    return i_list
                else:
                    print "O valor nao esta na lista."
                    return None
                break
            i_index = i_index.proximo

    def remove(self, valor):
        """Remove o no com valor correspondente, se existir e o retorna."""
        obj = self.find(valor)
        if obj is None:
            return None
        else:
            self.index_list = None
            anterior = obj.anterior
            proximo = obj.proximo
            anterior.proximo = proximo
            proximo.anterior = anterior
            print "Valor removido:", obj.dado
            return obj


x = Lista()
x.insert_valores_ord(100)
x.ord_append(50)
x.ord_append(51)
x.remove(40)
x.remove(60)
obj = x.find(41)
if obj is not None:
    print "Dado encontrado na lista:", obj.dado
print "--------------------------------------"
print "Size: ", x.listSize()
print "First: ", x.first().dado
print "Last: ", x.last().dado
print "--------------------------------------"
index = x.index_list
index.print_list_simple_2()
print "--------------------------------------"
x.print_list_simple()
