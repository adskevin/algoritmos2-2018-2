from estrela import Estrela
import cod_espaco


@given(u'dois valores inteiros e positivos, 0 e 600')
def valores_positivos(context):
    context.val1 = 0
    context.val2 = 600


@given(u'uma lista com os valores 1, 2 e 3')
def lista_valores(context):
    context.lista = [1, 2, 3]


@when(u'eu crio um objeto que representa uma estrela')
def cria_estrela(context):
    context.estrela = cod_espaco.estrela


@then(u'a coordenada X da estrela é 800,')
def verifica_x_estrela(context):
    assert cod_espaco.estrela.get_x() == 800


@then(u'a coordenada Y da estrela esta entre 0 e 600')
def step_impl(context):
    assert context.estrela.get_y() <= 600 and context.estrela.get_y() >= 0


@then(u'a velocidade da estrela é 1, 2 ou 3')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a velocidade da estrela é 1, 2 ou 3')
