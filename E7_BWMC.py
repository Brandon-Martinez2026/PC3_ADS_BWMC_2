# BWMC
# Ejercicio 7 ADS PC#3 parte 2

renta = float(input("Ingresa tu renta anual "))

if renta < 10000:
    impo = 0.05
    print("Te corresponde un 5% de tipo impositivo el cual es un total de ",renta*impo )
elif renta >= 10000 and renta < 20000:
    impo = 0.15
    print("Te corresponde un 15% de tipo impositivo el cual es un total de ", renta * impo )
elif renta >= 20000 and renta < 35000:
    impo = 0.20
    print("Te corresponde un 20% de tipo impositivo el cual es un total de ", renta * impo)
elif renta >= 35000 and renta < 60000:
    impo = 0.30
    print("Te corresponde un 30% de tipo impositivo el cual es un total de ",renta * impo)
else:
    impo = 0.20
    print("Te corresponde un 45% de tipo impositivo el cual es un total de ",renta * impo)

print("El total a pagar es de ", renta+(renta*impo))