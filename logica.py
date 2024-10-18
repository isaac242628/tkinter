import random

numero = ''.join(str(i) for i in range(10))
caracteres = ''.join(chr(i) for i in range(128))
juntar_numeros = caracteres + numero
juntando_tudo = list(juntar_numeros)
random.shuffle(juntando_tudo)
embaralhar = ''.join(juntando_tudo[:8])
print(embaralhar)
