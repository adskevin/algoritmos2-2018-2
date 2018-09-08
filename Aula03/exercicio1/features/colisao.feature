# language: pt


Feature: Verificar se um ponto esta dentro de um retangulo.

Cenario: Um ponto está dentro do retângulo.
    Dado um ponto com as coordenadas (7, 8)
    Dado um retângulo nas coordenadas (6,7) e dimensão (2,2)
    Quando quero saber se o ponto está dentro do retangulo
    Entao o resultado é verdadeiro.

Cenario: Um ponto não está dentro do retângulo.
    Dado um ponto com as coordenadas (5, 9)
    Dado um retângulo nas coordenadas (6,7) e dimensão (2,3)
    Quando quero saber se o ponto está dentro do retangulo
    Entao o resultado é falso.
