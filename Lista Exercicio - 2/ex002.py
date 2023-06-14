# 2. Determine se um ano é bissexto. Verifique no Google como fazer isso...

import calendar

ano = int(input('Digite um ano: '))

if calendar.isleap(ano) == True:
    print (f'{ano} é um ano bissexto')
else:
    print (f'{ano} NÃO é um ano bissexto')
