# 10) Escreva um programa para calcular a redução do tempo de vida de um fumante.
#     Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#     Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá.
#     Exiba o total de dias.

anos = int(input('Anos: '))
cigarros_por_dia = int(input('Cigarros por dia: '))

minutos = (anos * 365) * (cigarros_por_dia * 10)
dias_perdidos = (minutos / 60) / 24

print(f'Perdeu {dias_perdidos:.1f} dias de vida')
