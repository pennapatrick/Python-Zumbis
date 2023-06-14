# 6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = int(input('Distancia em km: '))
velocidade = int(input('Velocidade em km/h: '))

tempo = distancia / velocidade

print (f'Tempo estimado: {tempo}h')