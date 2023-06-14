# 2. Sorteie 20 inteiros entre 1 e 100 num a lista. Armazene os números pares na lista PAR e os
#    números ímpares na lista IMPAR. Imprima as três listas.

import random

lista = random.sample(range(1, 101), 20)
par = []
impar = []

for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print (sorted(lista))
print (sorted(par))
print (sorted(impar))