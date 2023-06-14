f = open(r'C:\Users\patri\OneDrive\Área de Trabalho\zumbi\Python-Zumbis\Revisão\Arquivo_Listas\surf.txt')
maior = 0
for linha in f:
    nome, pontos = linha.split()
    if float(pontos) > maior:
        maior = float(pontos)
f.close()
print (maior)
