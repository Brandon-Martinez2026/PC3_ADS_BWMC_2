# BWMC
# Ejercicio 2 ADS PC#3 parte 2
# Se establece una contraseña
password = "matomsitoguapo"
# Se le pide al usuario ingresar la contraseña
passw = input("Ingresa la contraseña")
#Se transforma todos los caracteres de la contraseña ingresada por el usuario
#a minusculas
passw2=passw.lower()
# Se verifica si ambas contraseñas coinciden
if passw2 == password:
    print("Has ingresado al sistema ")
else:
    print("Contraseña incorrecta")
