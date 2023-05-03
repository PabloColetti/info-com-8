# Escribir un programa que pida al usuario un carácter y muestre por pantalla si
# es una letra mayúscula, una letra minúscula, un número o un carácter especial.

# pida al usuario un carácte

# esMinuscula = txt.islower()
# esMayuscula = txt.isupper()
# esNumero = txt.isdigit()
# esLetra = txt.isalpha()

# print("Es minuscula", esMinuscula)
# print("Es MAYUSCULA", esMayuscula)
# print("Es numero", esNumero)
# print("Es letra", esLetra)

txt = input("Ingresa un caracter: ") 

if(txt.isalpha()):
    if(txt.islower()):
        print("Es una letra minuscula")
    else:
        print("Es una letra mayuscula")
elif(txt.isdigit()):
    print("Es numero")
else:
    print("Es un caracter especial")
