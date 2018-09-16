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
