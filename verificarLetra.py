import string
def verificarLetra(letra):
    if letra in string.ascii_uppercase:
        print("La letra es mayúscula")
    elif letra in string.ascii_lowercase:
        print("La letra es minúscula")
    else:
        print("Ingrese una letra por favor")
    
