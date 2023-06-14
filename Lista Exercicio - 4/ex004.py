# 4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python community welcome and 
#    encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, 
#    and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and
#    whatever your backgrou nd, we welcome you.”
#    Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou terminam com
#    uma das letras “python”.Imprima a lista resultante.Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.

texto = '''“The Python Software Foundation and the global Python community welcome and 
#    encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, 
#    and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and
#    whatever your backgrou nd, we welcome you.”'''.lower()

import string
for c in string.punctuation:
    texto = texto.replace(c, ' ')

resp = []
for p in texto.split():
    if p[0] in 'python' or p[-1] in 'python':
        resp.append(p)

print(resp)

# 5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” 
#    e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e
#    de remover antes os caracteres especiais.

