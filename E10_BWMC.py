# BWMC
# Ejercicio 10 ADS PC#3 parte 2

# MUESTRA EL MENU
print(
    "Bienvenido a la pizzeria Matom de Paz \nTipos de pizza \n   1.Vegetariana \n   2.No vegetariana \n"
)
#Solicita el tipo de pizza que el cliente desea
tipo = input("Ingresa el tipo de pizza que quieres:")
# Se evalua que pizza ha decidido el cliente 
if tipo == "1":
    #Se muestran los ingrediente
    print("Ingredientes de pizzas vegetarianas \n   Pimiento \n   Tofu \n")
    ingrediente = input("Ingresa el ingrediente que deseas: ")
    #Cambia las letras de ingredientes a minusculas
    ingredientelow = ingrediente.lower()
    #Se muestra mensaje dependiendo de los ingredientes
    if ingredientelow == "pimiento":
        print("Has elegido la pizza vegetariana con mozarrella, tomate y pimiento")
    elif ingredientelow == "tofu":
        print("Has elegido la pizza vegetariana con mozarrella, tomate y tofu")
    else: 
        print("Opcion invalida")
else:
    #Se muestran los ingredientes
    print("Ingredientes de pizzas no vegetarianas\n   Peperoni\n   Jamon\n   Salmon\n")
    #Se solicita el ingrediente
    ingrediente = input("Introduce el ingrediente que deseas: ")
    #Se cambia los valores de ingredientes a minusculas
    ingredientelow = ingrediente.lower()
    #Se muestran el mensaje dependiendo de los ingredientes
    if ingredientelow == "peperoni":
        print("Has elegido la pizza no vegetariana con mozarrella, tomate y peperoni")
    elif ingredientelow == "jamon":
        print("Has elegido la pizza no vegetariana con mozarrella, tomate y jamon")
    elif ingredientelow == "salmon":
        print("Has elegido la pizza no vegetariana con mozarrella, tomate y salmon")
    else: 
        print("Opcion invalida")
