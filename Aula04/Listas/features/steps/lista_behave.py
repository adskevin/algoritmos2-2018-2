"""True ou False para os valores de uma lista"""

from behave import given, then, when

from cod_lista import lista, retorno_lista


@given(u'a lista (L)')
def carregar_lista(context):
    context.lista = lista


@when(u'quero saber quais sao pares ou impares')
def retorna_lista_par_impar(context):
    context.retorno = retorno_lista


@then(u'retorno True ou False')
def resultado(context):
    context.retorno = True or False
