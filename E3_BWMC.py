# BWMC
# Ejercicio 3 ADS PC#3 parte 2

#El usuario  ingresa las partes de la division
dividendo = float(input("Ingresa el dividendo: "))
divisor = float(input("Ingresa el divisor: "))

#Se realizara la division si el divisor es mayor a 0
#Si no es mayor a 0 o es 0 mostrara error
if divisor > 0:
    print("El resultado de la division es: ",dividendo/divisor)
else:
    print("La division no se puede realizar")
