# BWMC
# Ejercicio 5 ADS PC#3 parte 2

#El usuario ingresa su edad e ingresos
edad = int(input("Ingrese la edad del usuario "))
ingresos= float(input("Ingrese las ganancias mensuales en Euros "))

#Se verifica la edad del usuario
if edad > 16:
    #Se verifican los ingresos del usuario 
    if ingresos > 1000:
        #Imprime este mensaje si tiene mas de 16 y gana mas de 1000 euros al mes
        print("El usuario es elegible para tributar ")
    else:
        #El usuario es mayor de 16 pero no genera mas de 1000 euros mensuales
        print("Las ganancias mensuales del usuario son menores de 1000 euros")
else:
    #El usuario es menor de 16 y no genera mas de 1000 euros mensuales
    print("El usuario es menor de 16 años, no es elegible para tributar")