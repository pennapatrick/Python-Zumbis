# 1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra
#    o maior e o menor valor, sem usar as funções max e min

import random

lista = (random.sample(range(101), 10))

maior = lista[0]
menor = lista[0]

for c in lista:
    if c > maior:
        maior = c
    if c < menor:
        menor = c

print (lista)
print (maior)
print (menor)