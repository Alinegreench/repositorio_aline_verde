import string

caracteres_ascii = string.ascii_letters
print(caracteres_ascii)
        
def verificar(cadena):
    for i in cadena:
        if i not in caracteres_ascii:  
            return False
    return True
    
cadena1 = "Esto es un a cadena$"
print(verificar(cadena1))