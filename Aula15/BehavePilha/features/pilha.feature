# language: pt

Funcionalidade: Criar uma pilha com tamanho estatico.
  Como um usuario quero criar uma pilha com tamanho 10

Cenario: Crio uma pilha.
  Dado o tamanho da pilha sendo 10
  Quando crio uma pilha
  Entao tenho uma pilha com 10 de capacidade
    E a pilha esta vazia

Cenario: Push de um valor
  Dado que eu tenho uma pilha
  Quando insiro o valor 8
  Entao a pilha nao esta vazia
    E o topo da pilha e 8

Cenario: Acessar o topo de uma pilha vazia
  Dado que eu tenho uma pilha
  Quando eu consulto o topo da pilha
  Entao uma excecao StackUnderflow e gerada
