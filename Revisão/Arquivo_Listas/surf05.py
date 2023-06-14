f = open(r'C:\Users\patri\OneDrive\Área de Trabalho\zumbi\Python-Zumbis\Revisão\Arquivo_Listas\surf.txt')
notas = []
nomes = []
for linha in f:
    nome, pontos = linha.split()
    notas.append(float(pontos))
    nomes.append(nome)
f.close()
notas.sort(reverse=True)
nomes.sort(reverse=True)
print (f'{nomes[0]} {notas[0]}')
print (f'{nomes[1]} {notas[1]}')
print (f'{nomes[2]} {notas[2]}')

