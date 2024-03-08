'''Programa que pide dos números al usuario y una operación matemática
a ejecutar con esos dos números. Las operaciones son:
-Suma
-Resta (el primero menos el segundo)
-Multiplicación
-División (el primero sobre el segundo)
-Exponenciación (el primero es la base y el segundo el exponente)
-Radicación (el primero es el radicando y el segundo es el índice)'''

n1 = float (input ("Ingrese primer número: "))
n2 = float (input ("Ingrese segundo número: "))

print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicación")
print ("4. División")
print ("5. Exponenciación")
print ("6. Radicación")
opc = int (input("Seleccione una opción: "))
if 1 < opc > 6:
    print ("Opcion inválida.")
    exit()

def opcion(n1, n2, opc):

    if opc == 1:
        return n1 + n2
    elif opc == 2:
        return n1 - n2
    elif opc == 3:
        return n1 * n2
    elif opc == 4:
        return n1 / n2
    elif opc == 5:
        return n1 ** n2
    elif opc == 6:
        if n1 < 0 and n2 % 2 == 0:
            print ("No se puede calcular la raíz cuadrada de un número negativo.")
            exit()
        return n1 ** (1/n2)
        
resultado = opcion(n1, n2, opc)
print (f"El resultado es: {resultado}")

