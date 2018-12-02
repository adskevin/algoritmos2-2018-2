"""Steps."""

from behave import given, when, then

from cod_acesso import teste_maior, teste_menor, soma_num_par, soma_num_impar


@given('os numeros 1 e 3 e 4')
def entra_com_valores(context):
    """Entra com os valores pedidos."""
    context.lista = [1, 3, 4]


@when('quero saber qual e o maior e seu indice')
def maior_valor(context):
    """Chama metodo de teste de maior valor."""
    context.retorno = teste_maior(context.lista)


@then('retorno {valor:d}')
def asserta_retorno(context, valor):
    """Testa se o retorno e valido."""
    assert context.retorno == valor


@when('quero saber qual e o menor e seu indice')
def menor_valor(context):
    """Chama metodo de teste de menor valor."""
    context.retorno = teste_menor(context.lista)


@when('quero saber a soma dos numeros pares')
def soma_pares(context):
    """Chama metodo de soma de numeros pares."""
    context.retorno = soma_num_par(context.lista)


@when('quero saber a soma dos numero impares')
def soma_impares(context):
    """Chama metodo de soma de numeros impares."""
    context.retorno = soma_num_impar(context.lista)
