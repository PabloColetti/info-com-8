# Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
# sus ventas totales y el departamento comercial te solicita que ayudes a los
# vendedores a calcular sus comisiones creando un programa que les pregunte su
# nombre y cuánto han vendido en éste mes.
# Tu programa le va a responder con una frase que incluya su nombre y el monto
# que le corresponde por las comisiones

vendedor = input("Ingrese su nombre: ")
ventas = float(input("Ingrese la cantidad de ventas realizadas este mes: "))
comisiones = float(ventas * 0.06)
print(vendedor, "realizó", ventas, "ventas este mes, y su comisión es de $", comisiones)