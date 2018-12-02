"""Verificando colisao de dois retangulos."""

from behave import given, when, then

from colisao_cod import teste


@given('dois retangulos nas coordenadas (6,7) (7,8) e dimensoes (2,2) e (2,2)')
def cria_retangulos(context):
    """Cria dois retangulos."""
    context.rect1 = [6, 7, 2, 2]
    context.rect2 = [7, 8, 2, 2]


@when('quero saber se os retangulos colidiram.')
def teste_colisao(context):
    """Testa de colisao."""
    context.result = teste(context.rect1, context.rect2)


@then('o resultado e verdadeiro.')
def asserta_resultado_verdadeiro(context):
    """Verifica se result e verdadeiro."""
    assert context.result


@given('dois retangulos nas coordenadas (6,7) (2,5) e dimensoes (2,2) e (2,2)')
def cria_retangulos2(context):
    """Cria dois retangulos."""
    context.rect1 = [6, 7, 2, 2]
    context.rect2 = [2, 5, 2, 2]


@then('o resultado e falso.')
def asserta_resultado_falso(context):
    """Verifica se result e falso."""
    assert not(context.result)
