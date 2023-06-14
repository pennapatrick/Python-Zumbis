notas = []
soma = 0
contador = 0

while contador <= 3:
    notas.append(float(input('Nota: ')))
    soma = soma + notas[contador]
    contador += 1
print(notas)
print(f'Media: {soma/contador}')
