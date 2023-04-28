# Escribe un programa que solicite al usuario su información personal, incluyendo
# su nombre completo, edad, estatura, peso, dirección y número de teléfono.
# A continuación, el programa deberá imprimir un mensaje con los datos
# ingresados por el usuario en el siguiente formato:
# La información ingresada es la siguiente:
# Nombre completo: [nombre completo]
# Edad: [edad]
# Estatura: [estatura] cm
# Peso: [peso] kg
# Dirección: [dirección]
# Número de teléfono: [número de teléfono]

nombre = input("Nombre completo: ")
edad = int(input("Edad: "))
estatura = int(input("Estatura: "))
peso = int(input("Peso: "))
direccion = input("Direccion: ")
numero_telefono = input("Numero de telefono: ")

print(f'''
  ======================================
  Nombre completo: {nombre}
  Edad: {edad}
  Estatura: {estatura} cm
  Peso: {peso} kg
  Dirección: {direccion}
  Número de teléfono: {numero_telefono}
  ======================================
''')