# BWMC
# Ejercicio 6 ADS PC#3 parte 2

#Se le pide el nombre y el genero al usuario
nombre = input("Ingresa tu nombre ")
genero = input("¿Cuál es tu sexo (Mujer o Hombre)? ")
#Si el genero es mujer se evalua a que grupo pertenece
if genero == "Mujer":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    #Si es hombre tambien evalua a que grupo pertenecia 
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
        
print(nombre ,"pertenece al grupo: ", grupo)
