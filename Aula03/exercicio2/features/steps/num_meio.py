"""Encontrando o numero do meio."""

from behave import given, when, then

from codigo_num_meio import func_meio


@given(u'os numeros 2 e 3 e 4')
def given_tres_numeros(context):
    """Dado que o sistema tenha tres valores."""
    context.num1 = 2
    context.num2 = 3
    context.num3 = 4


@when(u'quero saber o numero do meio')
def when_encontra_num_meio(context):
    """Utilizo uma funcao pra encontrar o numero do meio."""
    a = context.num1
    b = context.num2
    c = context.num3
    context.retorno = func_meio(a, b, c)


@then('o resultado e 3')
def then_verif_retorno(context):
    """Verifica o retorno da funcao."""
    assert context.retorno == 3
