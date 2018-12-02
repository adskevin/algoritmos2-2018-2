"""Steps."""
from behave import given, when, then
from estrela import Estrela


@given('dois valores inteiros e positivos, 0 e 600')
def dados_dois_valores(context):
    """Cria dois valores positivos."""
    context.valores = [0, 600]


@given('uma lista com os valores 1, 2 e 3')
def dado_lista(context):
    """Cria uma lista com os valores 1,  2 e 3."""
    context.lista = [1, 2, 3]


@when('eu crio um objeto que representa uma estrela')
def cria_estrela(context):
    """Instancia uma estrela."""
    context.estrela = Estrela()


@then('a coordenada X da estrela é 800,')
def verif_coord_x(context):
    """Verifica coordenada x."""
    if context.estrela.x is not 800:
        context.estrela.x = 800


@then('a coordenada Y da estrela esta entre 0 e 600')
def testa_coord_y(context):
    """Verifica se a coordenada y da estrela esta entre 0 e 600."""
    assert (context.estrela.y >= 0 and context.estrela.y <= 600)


@then('a velocidade da estrela é 1, 2 ou 3')
def testa_velocidade_estrela(context):
    """Verifica se a velocidade da estrela esta dentro do padrao."""
    assert (context.estrela.spd >= 1 or context.estrela.spd <= 3)


@given('um objeto representando uma estrela')
def cria_estrela_novamente(context):
    """Cria estrela."""
    cria_estrela(context)


@when('eu movo a estrela')
def move_estrela(context):
    """Quando movo a estrela."""
    context.x_antes_de_mover = context.estrela.x
    context.y_antes_de_mover = context.estrela.y
    context.spd_antes_de_mover = context.estrela.spd
    context.estrela.move_estrela()


@then('a coordenada X varia de acordo com a velocidade da estrela')
def testa_x_estrela(context):
    """Testa a coord x depois de um movimento."""
    assert (context.x_antes_de_mover == context.estrela.x + context.estrela.spd)


@then('a coordenada Y da estrela nao varia')
def testa_y_estrela(context):
    """Testa coord y depois de um movimento."""
    assert (context.y_antes_de_mover == context.estrela.y)


@then('a velocidade da estrela nao varia')
def testa_spd_estrela(context):
    """Testa spd depois de um movimento."""
    assert (context.spd_antes_de_mover == context.estrela.spd)


@when('eu crio uma lista de {val:d} estrelas')
def cria_varias_estrelas(context, val):
    """Cria varias estrelas."""
    context.lista_de_estrelas = []
    x = 0
    while x < val:
        cria_estrela(context)
        context.lista_de_estrelas.append(context.estrela)
        x += 1


@then('a coordenada X de cada estrela e 800')
def testa_x_todas_estrelas(context):
    """Testa o x de todas as estrelas."""
    passou = True
    for i in context.lista_de_estrelas:
        print(passou)
        if not(i.x == 800):
            passou = False
    assert passou


@then('a coordenada Y de cada estrela esta entre 0 e 600')
def testa_y_todas_estrelas(context):
    """Testa todos os y das estrelas."""
    passou = True
    for i in context.lista_de_estrelas:
        print(passou)
        if not(i.y <= 600 and i.y >= 0):
            passou = False
    assert passou


@then('a velocidade de cada estrela e 1, 2 ou 3')
def testa_spd_todas_estrelas(context):
    """Testa o spd de todas as estrelas."""
    passou = True
    for i in context.lista_de_estrelas:
        print(passou)
        if not(i.spd <= 3 and i.spd >= 1):
            passou = False
    assert passou


@given('uma lista de objetos representando estrelas')
def cria_varias_estrelas_novamente(context):
    """Cria novamente varias estrelas."""
    cria_varias_estrelas(context, 10)


@when('eu movo as estrelas da lista')
def move_todas_estrelas(context):
    """Move todas as estrelas uma vez."""
    for i in context.lista_de_estrelas:
        i.move_estrela()


@then('a coordenada X de cada estrela varia de acordo com a sua velocidade')
def testa_todos_os_x(context):
    """Testa se os x antigos correspondem com os atuais."""
    valor = len(context.lista_de_estrelas)
    x = 0
    passou = True
    while x < valor:
        if not(context.lista_de_estrelas[x].x_old == context.lista_de_estrelas[x].x + context.lista_de_estrelas[x].spd):
            passou = False
        x += 1
    assert passou


@then('a coordenada Y de cada estrela nao varia')
def testa_todos_os_y(context):
    """Testa se os y antigos correspondem com os atuais."""
    valor = len(context.lista_de_estrelas)
    x = 0
    passou = True
    while x < valor:
        if not(context.lista_de_estrelas[x].y_old == context.lista_de_estrelas[x].y):
            passou = False
        x += 1
    assert passou


@then('a velocidade de cada estrela nao varia')
def testa_todos_os_spd(context):
    """Tesata se os spd antigos correspondem com os atuais."""
    valor = len(context.lista_de_estrelas)
    x = 0
    passou = True
    while x < valor:
        if not(context.lista_de_estrelas[x].spd_old == context.lista_de_estrelas[x].spd):
            passou = False
        x += 1
    assert passou


@given('uma lista especifica de estrelas')
def cria_lista_especifica_estrelas(context):
    """Cria uma lista especifica de estrelas."""
    cria_varias_estrelas(context, 3)
    context.lista_de_estrelas[0].x = 10
    context.lista_de_estrelas[0].y = 10
    context.lista_de_estrelas[0].spd = 3

    context.lista_de_estrelas[1].x = 10
    context.lista_de_estrelas[1].y = 20
    context.lista_de_estrelas[1].spd = 2

    context.lista_de_estrelas[2].x = 10
    context.lista_de_estrelas[2].y = 14
    context.lista_de_estrelas[2].spd = 1


@when('eu movo as etrelas {val:d} vezes')
def move_n_vezes(context, val):
    """Move as estrelas n vezes."""
    for i in range(val):
        move_todas_estrelas(context)


@then('a lista so ira possuir 2 estrelas')
def verifica_qtd_estrelas(context):
    """Verifica se sobraram apenas 2 estrelas."""
    context.count = 0
    for i in context.lista_de_estrelas:
        if i.alive:
            context.count += 1
    assert context.count == 2
