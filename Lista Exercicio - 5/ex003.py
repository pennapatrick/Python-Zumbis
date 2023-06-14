# Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também divisíveis por 7?
lista = list()
for c in range(1067, 3628):
    if c % 2 == 0 and c % 7 == 0:
        lista.append(c)
print(lista)
print(len(lista))