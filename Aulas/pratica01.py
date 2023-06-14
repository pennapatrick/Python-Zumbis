velocidade = int(input('Velocidade: '))

if velocidade > 110:
    multa = (velocidade - 110) * 5
    print ('MULTADO ', end='// ')
    print (f'Valor: R${multa}')
else:
    print (f'Siga em frente!')
