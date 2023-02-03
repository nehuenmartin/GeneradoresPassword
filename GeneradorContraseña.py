import random # Importamos la librería random para poder usar números aleatorios
import string # Importamos la librería string para poder usar letras aleatorias
import secrets # Importamos la librería secrets para poder usar caracteres aleatorios

lista_contraseñas = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '!', '@', '#', '$', '%', '&', '*', '?'
]
contraseña = '' # Esta variable va a contener la contraseña generada
for i in range(16): # 16 es el número de caracteres que va a tener la contraseña
    contraseña = contraseña + random.choice(lista_contraseñas)[0]
print('tu contraseña es: ', contraseña, '(se uso el módulo random)')



# Ahora vamos a generar una contraseña con el módulo secrets

alhabeto = string.ascii_letters # Esta variable va a contener las letras del alfabeto
contraseña2 = ''.join(secrets.choice(alhabeto) for i in range(16)) # Esta variable va a contener la contraseña generada con el módulo secrets
print('tu contraseña2 es: ', contraseña2, '(se uso el módulo secrets)')


