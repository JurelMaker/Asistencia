import random
import string

def matricula(): 
    """
    Genera una cadena aleatoria de 12 caracteres,
    que contiene letras (mayúsculas y minúsculas) y números.
    """
    longitud = 8
    caracteres = string.ascii_letters + string.digits
    cadena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return cadena

