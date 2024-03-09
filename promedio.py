def calcular_nota (n1, n2, n3):
    
    if 0 < n1 < 11 and 0 < n2 < 11 and 0 < n3 < 11:
        return (n1 * 0.3) + (n2 * 0.3) + (n3 * 0.4)
    else:
       print ("Las calificaciones deben estar en el rango de 1 a 10.")
       return None

n1 = float (input("Ingrese la primer calificación:  "))
n2 = float (input("Ingrese la segunda calificación:  "))
n3 = float (input("Ingrese la tercera calificación:  "))

notaFinal = calcular_nota (n1, n2, n3)
print ("La nota final es:  ", notaFinal)

