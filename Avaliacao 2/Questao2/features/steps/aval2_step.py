from behave import given, when, then
from cod_aval2 import Deque


@given('o tamanho da estrutura sendo 10')
def tamanho_estrutura(context):
    context.tamanho = 10
    assert context.tamanho is 10


@when('crio um deque')
def cria_deque(context):
    context.deque = Deque(context.tamanho)


@then('tenho um deque com capacidade para armazenar 10 elementos')
def testa_tamanho_deque(context):
    assert context.deque.tamanho is 10


@then('a estrutura esta vazia')
def estrutura_esta_vazia(context):
    assert context.deque.is_empty()


@given('que eu tenho um deque')
def tenho_um_deque(context):
    context.tamanho = 10
    context.deque = Deque(context.tamanho)
    assert context.deque is not None


@when('insiro, no final da estrutura, o valor 8')
def end_insert(context):
    context.deque.pushBack(8)


@then('a estrutura nao esta vazia')
def estrutura_nao_vazia(context):
    assert not(context.deque.is_empty())


@then('o elemento na frente da estrutura tem o valor 8')
def elem_frente_tem_8(context):
    assert context.deque.dados[context.deque.first] is 8


@when('insiro, no final da estrutura, os valores [1, 2, 3, 4]')
def insert_final_valores(context):
    context.deque.pushBack(1)
    context.deque.pushBack(2)
    context.deque.pushBack(3)
    context.deque.pushBack(4)


@then(u'o elemento na frente da estrutura tem o valor 1')
def testa_valor_frente(context):
    assert context.deque.dados[context.deque.first] is 1


@then('o elemento no final da estrutura tem o valor 4')
def testa_valor_fim(context):
    assert context.deque.dados[context.deque.last] is 4


@given('este deque tem os elementos, inseridos no final, [1, 3, 5, 7]')
def insert_final_valores_2(context):
    context.deque.pushBack(1)
    context.deque.pushBack(3)
    context.deque.pushBack(5)
    context.deque.pushBack(7)


@when('insiro, no final da estrutura, o valor 9')
def insiro_valor(context):
    context.deque.pushBack(9)


@then('o elemento no final da estrutura tem o valor 9')
def testa_valor_final(context):
    assert context.deque.dados[context.deque.last] is 9
