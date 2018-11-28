# language: pt


Funcionalidade: Verificar se um ponto esta dentro de um retangulo.

Cenario: Um ponto esta dentro do retangulo.
    Dado um ponto com as coordenadas (7, 8)
    Dado um retangulo nas coordenadas (6,7) e dimensao (2,2)
    Quando quero saber se o ponto esta dentro do retangulo
    Entao o resultado e verdadeiro.

Cenario: Um ponto nao esta dentro do retangulo.
    Dado um ponto com as coordenadas (5, 9)
    Dado um retangulo nas coordenadas (6,7) e dimensao (2,3)
    Quando quero saber se o ponto esta dentro do retangulo
    Entao o resultado e falso.
