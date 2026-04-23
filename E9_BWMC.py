# BWMC
# Ejercicio 9 ADS PC#3 parte 2

edad = int(input("Ingresa tu edad: "))
# Se asigna el precio dependiendo de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Se imprime el precio
print("El total a pagar es de ", precio)
