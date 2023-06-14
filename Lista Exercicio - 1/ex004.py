# 4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. 
#    Exiba o valor do aumento e do novo salário.

salario = float(input('Salario: '))
aumento = float(input('Aumento em %: '))

aumento2 = salario * (aumento / 100)

total = salario + aumento2
print (f'Aumento: R${aumento2}')
print (f'Novo salário: R${total}')