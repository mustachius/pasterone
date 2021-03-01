#! python3
# pasterone - Gerenciador de clipboard e de mensagens pré-salvas.

texto = {'sim': """eu concordo, pode mandar ver.""",
         'ocupado': """agora eu não posso, estou ocupado, dá pra ser depois?""",
         'não': """acho melhor não."""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Modo de uso: python pasterone.py [palavra_chave] - copie o texto devolvido')
    sys.exit()
palavra_chave = sys.argv[1]     # primeiro comando é a palavra-chave

if palavra_chave in texto:
    pyperclip.copy(texto[palavra_chave])
    print("Texto para " + palavra_chave + " copiado para a clipboard")
else:
    print("Não existe texto para esta palavra-chave")