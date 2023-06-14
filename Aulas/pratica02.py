minutos = int(input('Minutos em linha: '))

if minutos < 200:
    preço_minuto = 0.20
elif minutos <= 400:
    preço_minuto = 0.18
elif minutos <= 800:
    preço_minuto = 0.15
else:
    preço_minuto = 0.08

total = minutos * preço_minuto
print (f'Sua conta de telefone resultou em: R${total:.2f}')
