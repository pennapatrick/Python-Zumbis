# 5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.

a = int(input('Valor de a: '))
b = int(input('Valor de b: '))
while a % b != 0:
    a, b = b, a%b
print (f'mdc = {b}')
