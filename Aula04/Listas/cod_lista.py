"""Lista."""

import random


def teste(valor):
    """Testa se valor e par ou impar."""
    if valor % 2 == 0:
        return True
    else:
        return False


def cria_lista_random(val):
    """Cria lista random."""
    L = []
    while val < 10:
        L.append(random.randint(10, 100))
        val += 1
    return L


def newList(list):
    """Cria lista True False."""
    newlist = []
    val = len(list)-1
    x = 0
    while x <= val:
        newlist.append(teste(list[x]))
        x += 1
    return newlist
