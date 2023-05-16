nombre1= input("ingrese un nombre")
nombre2= input("ingrese otro nombre")

lista_nombres=[nombre1, nombre2]
lista_nombres.sort()

print("Los nombres en orden alfabetico son: ")
for nombre in lista_nombres:
    print(nombre)
