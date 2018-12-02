"""Exercicio de acesso a dados de lista."""

import sys
lista = []
limite_lista = 9


def cria_lista_global(list):
    """Metodo para retrocompatibilidade de codigo."""
    global lista
    lista = list


def entra_valor():
    """Entra com um valor para utilizar o menu."""
    global lista
    global limite_lista
    del lista[:]
    sair = True
    teste = True
    val = 0
    while(sair):
        if(len(lista) >= limite_lista):
            sair = False
        teste = True
        while(teste):
            try:
                val = int(input("Entre com um valor, 0 para cancelar: "))
                # print "Passou"
                teste = False
            except:
                print ("Erro, tente novamente.")
        if val == 0:
            break
        lista.append(val)
    print (lista)


def teste_maior():
    """Testa qual numero e o maior da lista."""
    global lista
    valor_maior = lista[0]
    indice_maior = 0
    for x in lista:
        # print "Valor de x no for: ", x
        if (x > valor_maior):
            # indice = enumerate(lista[x])
            valor_maior = x
    for x in lista:
        if x == valor_maior:
            break
        indice_maior += 1
    print "Valor maior: ", lista[indice_maior]
    print "Indice desse Valor maior: ", indice_maior
    return lista[indice_maior]


def teste_menor():
    """Testa qual numero e o menor da lista."""
    global lista
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
    print "Valor menor: ", lista[indice_menor]
    print "Indice desse Valor menor: ", indice_menor


def soma_num_par():
    """Soma os numeros pares da lista."""
    global lista
    soma_par = 0
    for x in lista:
        if x % 2 == 0:
            soma_par += x
    print "A soma dos numeros pares e: ", soma_par


def soma_num_impar():
    """Soma os numeros impares da lista."""
    global lista
    soma_impar = 0
    for x in lista:
        if x % 2 != 0:
            soma_impar += x
    print "A soma dos numeros impares e: ", soma_impar


def soma_sem_sentido():
    """Executa a soma solicitada pelo exercicio."""
    global lista
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


def menu():
    """Metodo menu."""
    val = 0
    menu = "\n==================================="
    menu += "\n1- Qual o maior numero e qual o seu indice?"
    menu += "\n2- Qual o menor numero e qual o seu indice?"
    menu += "\n3- Qual a soma dos numeros pares?"
    menu += "\n4- Qual a soma dos numeros impares?"
    menu += "\n5- Qual a soma da divisao dos numeros de indice par, pelos numeros de indice impar?"
    menu += "\n6- Imprima os numeros na ordem inversa que foram digitados."
    menu += "\n7- Redigitar lista."
    menu += "\n0- Finalizar."
    print menu
    # sys.exit()
    teste = True
    while(teste):
        try:
            val = int(input("Ecolha: "))
            # print "Passou"
            if val <= 7 and val >= 0:
                teste = False
            else:
                print ("Erro, tente novamente.")
        except:
            print ("Erro, tente novamente.")
    chama_metodo(val)


def imprime_num_invert():
    """Imprime a lista de tras pra frente."""
    global lista
    indice = (len(lista)-1)
    lista_invertida = []
    while indice >= 0:
        lista_invertida.append(lista[indice])
        indice -= 1
    print lista_invertida


def finalizaPrograma():
    """Finaliza o programa."""
    print "Programa Finalizado. "
    sys.exit()


def chama_metodo(val):
    """Verifica o numero entrado no menu."""
    if val == 1:
        teste_maior()
    elif val == 2:
        teste_menor()
    elif val == 3:
        soma_num_par()
    elif val == 4:
        soma_num_impar()
    elif val == 5:
        soma_sem_sentido()
    elif val == 6:
        imprime_num_invert()
    elif val == 7:
        entra_valor()
    elif val == 0:
        finalizaPrograma()
    else:
        print "Erro."
        return menu()


entra_valor()
while True:
    menu()
