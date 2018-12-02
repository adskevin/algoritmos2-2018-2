# language: pt

Funcionalidade: Verificar se um retangulo colidiu com outro retangulo ou nao.

Cenario: Um retangulo colidiu com outro.
    Dados dois retangulos nas coordenadas (6,7) (7,8) e dimensoes (2,2) e (2,2)
    Quando quero saber se os retangulos colidiram.
    Entao o resultado e verdadeiro.

Cenario: Um retangulo nao esta colidindo com outro.
    Dados dois retangulos nas coordenadas (6,7) (2,5) e dimensoes (2,2) e (2,2)
    Quando quero saber se os retangulos colidiram.
    Entao o resultado e falso.
