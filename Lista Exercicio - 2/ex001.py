# 1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
#    um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print('Triangulo Existente: Equilátero')
    elif a != b != c:
        print('Triangulo Existente: Escaleno')
    elif a == b or b == c or c == a:
        print('Triangulo Existente: Isósceles')
else:
    print('Triangulo Inexistente')