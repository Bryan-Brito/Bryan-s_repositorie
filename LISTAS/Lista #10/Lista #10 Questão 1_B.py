import sys

try:
    X = int(input("Insira um número"))

    Y = X%2

    if Y == 0:
        print("Seu número é par")
    else:
        print("Seu número é ímpar")

except ValueError:
    print('ERRO: Dado de entrada inválido!')