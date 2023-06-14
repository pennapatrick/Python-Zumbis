# 3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
#    anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
#    crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
#    necessários para que a população do país A ultrapasse ou iguale a população do país B,
#    mantidas as taxas de crescimento

ano = 0
A = 80000
B = 200000

while True:
    A = A + ( A * 0.03)
    B = B + ( B * 0.015)
    ano += 1
    if A >= B:
        print (f'Demorou {ano} anos para que A ultrapassasse B')
        print (f'Total de A: {int(A)}')
        print (f'Total de B: {int(B)}')
        break