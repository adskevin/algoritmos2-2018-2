"""Exercicio de acesso a dados de lista."""


def teste_maior(lista):
    """Testa qual numero e o maior da lista."""
    valor_maior = lista[0]
    indice_maior = 0
    for x in lista:
        if (x > valor_maior):
            valor_maior = x
    for x in lista:
        if x == valor_maior:
            break
        indice_maior += 1
    return lista[indice_maior]


def teste_menor(lista):
    """Testa qual numero e o menor da lista."""
    valor_menor = lista[0]
    indice_menor = 0
    for x in lista:
        # print "Valor de x no for: ", x
        if (x < valor_menor):
            # indice = enumerate(lista[x])
            valor_menor = x
    for x in lista:
        if x == valor_menor:
            break
        indice_menor += 1
    return lista[indice_menor]


def soma_num_par(lista):
    """Soma os numeros pares da lista."""
    soma_par = 0
    for x in lista:
        if x % 2 == 0:
            soma_par += x
    return soma_par


def soma_num_impar(lista):
    """Soma os numeros impares da lista."""
    soma_impar = 0
    for x in lista:
        if x % 2 != 0:
            soma_impar += x
    return soma_impar


def soma_sem_sentido(lista):
    """Executa a soma solicitada pelo exercicio."""
    soma_divisao = 0
    soma_par = 0
    soma_impar = 0
    indice = 0
    for x in lista:
        if indice % 2 == 0:
            soma_par += x
        if indice % 2 != 0:
            soma_impar += x
        indice += 1
    print "Soma dos numeros dos indices pares: ", soma_par
    print "Soma dos numeros dos indices impares: ", soma_impar
    soma_divisao = (soma_par/float(soma_impar))
    print "Soma da divisao e: ", soma_divisao


def imprime_num_invert(lista):
    """Imprime a lista de tras pra frente."""
    indice = (len(lista)-1)
    lista_invertida = []
    while indice >= 0:
        lista_invertida.append(lista[indice])
        indice -= 1
    print lista_invertida
