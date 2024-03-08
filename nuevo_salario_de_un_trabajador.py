'''Programa que calcula el nuevo salario de un tranajador si obtuvo 
un incremento de x%'''

def aumentoSalario(x,y):
    aumento = x * ((y/100)+1)
    return aumento

x = float (input("Ingrese salario actual del trabajador: "))
y = int (input("Ingrese el porcentaje de aumento: "))
total = aumentoSalario(x,y)
print (f"El nuevo salario es: {round(total, 2)}")
