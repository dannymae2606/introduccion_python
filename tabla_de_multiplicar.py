def tablasMultiplicar(n):
    for i in range (0,13):
        multiplicacion = n * i
        print (f"{n} x {i} = {multiplicacion}")

n = int (input ("Ingrese la el número de la tabla de multiplicar a calcular: "))
if not (0 < n <= 9):
    print ("El valor ingresado debe ser en un rango de 1-9.")
    exit()
else:
    tablasMultiplicar(n)
