'''Programa que convierte una unidad en días, horas, minutos a segundos'''

dias = int (input("Ingrese cantidad de días: "))
horas = int (input("Ingrese cantidad de horas: "))
minutos = int (input("Ingrese cantidad de minutos: "))

if dias < 1:
    print ("Ingrese un número mayor a 1.")
    exit()

if horas < 1:
    print ("Ingrese un número mayor a 1.")
    exit()

if minutos < 1:
    print ("Ingrese un número mayor a 1.")
    exit()

else:

    print (f"En {dias} días hay {dias * 86400} segundos")
    print (f"En {horas} horas hay {horas * 3600} segundos")
    print (f"En {minutos} minutos hay {minutos * 60} segundos")




