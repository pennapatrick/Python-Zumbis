f = open(r'C:\Users\patri\OneDrive\Área de Trabalho\zumbi\Python-Zumbis\Revisão\Arquivo_Listas\surf.txt')
notas = {}
for linha in f:
    nome, pontos = linha.split()
    notas[float(pontos)] = nome
f.close()
for nota in sorted(notas, reverse = True):
    print (f'{notas[nota]} tem nota {nota}')
