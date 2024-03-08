
def numPrimo(n):
    if n <= 1:
        return False
    if n == 2:
       return True
    else:
        resultado = []
        for x in range (2,n):
            y = n % x
            resultado.append(y)
        return 0 not in resultado
           



n = int (input("Ingrese un número: "))
if numPrimo(n):
    print ("Es un número primo.")
else:
    print ("No es un número primo.")



       

