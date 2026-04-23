# BWMC
# Ejercicio 8 ADS PC#3 parte 2

#Se establece la cantidad de la bonificacion
boni = 2400
#Se pide la puntuacion de la evaluacion anual
puntuacion = float(input("Ingrese la puntuacion de la evaluacion anual "))

#Se evalua a que caso corresponde lo ingresado
if puntuacion == 0.0:
    nivel = "Inaceptable"
    total = boni*puntuacion
elif puntuacion == 0.4:
    nivel = "aceptable"
    total = boni*puntuacion
elif puntuacion > 0.6:
    nivel = "Meritorio"
    total = boni*puntuacion
else:
    nivel = ""
    print("Ingresa una puntuacion valida")

#Se impri9men los detalles
if nivel == "":
    print()
else:
    print("Tu rendimiento es de nivel ", nivel)
    print("Te corresponde recibir ", total)