# 6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
#    e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#    8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
#    quanto pagou ao sindicato e o salário líquido.
#    Observe que Salário Bruto - Descontos = Salário Líquido. 
#    Calcule os descontos e o salário líquido, conforme a tabela abaixo:

ganho_hora = float(input('Ganho por hora R$: '))
horas_trabalhadas = int(input('Horas trabalhadas no mês: '))
bruto = horas_trabalhadas * ganho_hora

imposto_renda = (bruto * (11/100))
inss = (bruto * (8/100))
sindicato = (bruto * (5/100))

descontos = imposto_renda + inss + sindicato
liquido = bruto - descontos

print (f'Salario bruto: R${bruto:.2f}')
print (f'Imposto de renda: R$-{imposto_renda:.2f}')
print (f'INSS: R$-{inss:.2f}')
print (f'Sindicato: R$-{sindicato:.2f}')
print (f'Total de descontos: R$-{descontos:.2f}')
print (f'Salário liquido: R${liquido:.2f}')