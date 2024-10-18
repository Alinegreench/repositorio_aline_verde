import string
import random

minusculas_ascii = string.ascii_lowercase
mayusculas_ascii = string.ascii_uppercase
numeros = string.digits
lista_completa = minusculas_ascii + mayusculas_ascii + numeros

def generar_password(cadena):
    print("Ingrese el número de caracteres que quiere que tenga su contraseña:")
    n = int(input())

    contrasena = ''.join(random.choice(lista_completa) for i in range(n))
    return contrasena

print("Contraseña generada:", generar_password(lista_completa))