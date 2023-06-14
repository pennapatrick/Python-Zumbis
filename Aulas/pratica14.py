palavra = (input('Palavra: ')).upper()

if palavra[::-1] == palavra:
    print(f'{palavra} é um palindromo ({palavra[::-1]})')
else:
    print(f'{palavra} NÃO é um palíndromo ({palavra[::-1]})')

