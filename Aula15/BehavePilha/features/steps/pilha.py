from cod_pilha import Pilha
from cod_pilha import StackUnderflow


@given('o tamanho da pilha sendo {tam:d}')  # {tam:d} = Variavel tam com um decimal
def Tamanho_da_pilha(context, tam):  # Variavel deve constar aqui
    context.tamanho = tam


@when('crio uma pilha')
def Cria_pilha(context):
    context.pilha = Pilha(context.tamanho)


@then('tenho uma pilha com {tam:d} de capacidade')
def Testa_tamanho_pilha(context, tam):
    assert len(context.pilha._dados) == 10


@then(u'a pilha esta vazia')
def Pilha_esta_vazia(context):
    assert context.pilha.empty is True


@given('que eu tenho uma pilha')
def Tenho_uma_pilha(context):
    context.pilha = Pilha(5)


@when('insiro o valor {val:d}')
def step_impl(context, val):
    context.pilha.push(val)


@then('a pilha nao esta vazia')
def Pilha_nao_vazia(context):
    assert context.pilha.empty is False


@then('o topo da pilha e {val:d}')
def Topo_pilha(context, val):
    assert context.pilha.pick() == val


@when('eu consulto o topo da pilha')
def Consulta_topo_pilha(context):
    try:
        context.result = context.pilha.pick()
        context.exception = None
    except Exception as e:
        context.exception = e


@then('uma excecao StackUnderflow e gerada')
def Excecao_gerada(context):
    assert context.exception is not None
    assert isinstance(context.exception, StackUnderflow) is True
