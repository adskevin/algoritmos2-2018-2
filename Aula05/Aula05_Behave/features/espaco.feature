# language: pt

Funcionalidade: Exibir uma animação representando um campo de estrelas.
    Como um usuário,
    Eu quero ver um campo de estrelas movendo-se,
    Para pensar na vida.

Cenario: Escolhendo a coordenada Y e a velocidade da estrela.
    Dados dois valores inteiros e positivos, 0 e 600
        E uma lista com os valores 1, 2 e 3
    Quando eu crio um objeto que representa uma estrela
    Então a coordenada X da estrela é 800,
        E a coordenada Y da estrela esta entre 0 e 600
        E a velocidade da estrela é 1, 2 ou 3

Cenario: Movendo a estrela
    Dado um objeto representando uma estrela
    Quando eu movo a estrela
    Então a coordenada X varia de acordo com a velocidade da estrela
        E a coordenada Y da estrela nao varia
        E a velocidade da estrela nao varia

Cenario: Criando varias estrelas.
    Dados dois valores inteiros e positivos, 0 e 600
        E uma lista com os valores 1, 2 e 3
    Quando eu crio uma lista de 20 estrelas
    Então a coordenada X de cada estrela e 800
        E a coordenada Y de cada estrela esta entre 0 e 600
        E a velocidade de cada estrela e 1, 2 ou 3

Cenario: Movendo multiplas estrelas.
    Dada uma lista de objetos representando estrelas
    Quando eu movo as estrelas da lista
    Entao a coordenada X de cada estrela varia de acordo com a sua velocidade
        E a coordenada Y de cada estrela nao varia
        E a velocidade de cada estrela nao varia

        Cenario: Excluindo estrelas.
            Dada uma lista especifica de estrelas:
            | x | y | speed |
            | 10 | 10 | 3 |
            | 10 | 20 | 2 |
            | 10 | 14 | 1 |
            Quando eu movo as etrelas 4 vezes
            Então a lista so ira possuir 2 estrelas
            | x | y | speed |
            | 2 | 20 | 2 |
            | 6 | 14 | 1 |
