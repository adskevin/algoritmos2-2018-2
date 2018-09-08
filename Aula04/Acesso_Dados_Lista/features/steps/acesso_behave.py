from behave import given, when, then

from cod_acesso import entra_valor


@given(u'os numeros 1 e 3 e 4')
def entrada(context):
    context.lista = [1, 3, 4]
    print(context.lista)


@when(u'quero saber qual e o maior e seu indice')
def compara(context):
    context.indice = 0
    context.valor = 0
    for x in context.lista:
        context.indice += 1
        if context.lista[context.indice] >= context.valor:
            context.valor = context.lista
    print ("Valor = ", context.valor)


@then(u'retorno 4')
def retorna(context):
    print ("Entre os valores: ", context.lista)
    print ("O maior é: ", context.lista[context.indice])
    print ("Seu indice é: ", context.indice)
