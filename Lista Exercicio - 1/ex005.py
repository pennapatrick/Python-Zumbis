# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

preço = float(input('Preço: '))
desconto = float(input('Desconto em %: '))

valor_desconto = preço * (desconto / 100)
preço_final = preço - valor_desconto

print (f'Valor do desconto: R${valor_desconto}')
print (f'Preço a pagar: R${preço_final}')