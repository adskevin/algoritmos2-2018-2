"""Lista"""

import random


L = []


def lista():
    global L
    val = 0
    while val < 10:
        L.append(random.randint(10, 100))
        val += 1
    print L


def retorno_lista():
    global L
    nova_L = []
    var = True
    for x in L:
        if x % 2 == 0:
            nova_L.append(True)
        else:
            nova_L.append(False)
    print nova_L


lista()
retorno_lista()
