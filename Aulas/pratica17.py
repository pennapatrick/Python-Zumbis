d, m, a = input('dd/mm/aaaa: ').split('/')
meses = '''Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'''.split()
print (f'{d} de {meses[int(m)-1]} de {a}')