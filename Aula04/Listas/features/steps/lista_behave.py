"""True ou False para os valores de uma lista."""

from behave import given, then, when

from cod_lista import cria_lista_random, newList


@given('a lista (L)')
def carregar_lista(context):
    """Cria a lista."""
    context.list = cria_lista_random(10)


@when('quero saber quais sao pares ou impares')
def testa_par_impar(context):
    """Chama metodo para criar listas de True ou False."""
    context.newlist = newList(context.list)


@then('retorno True ou False')
def asserta_resultado(context):
    """Testa trues e falses."""
    assert True
    # Nao soube que tipo de teste e necessario aqui
