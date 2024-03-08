'''Programa que calcule el IMC de una persona dado su peso y estatura. Luego, 
indicar su nivel de peso así:

IMC              CLASIFICACIÓN

------------------------------

  <  18.5       ->  BAJO PESO
18.5  -  24.9   ->  NORMAL
25.0  -  29.9   ->  SOBREPESO
30.0  -  34.9   ->  OBESIDAD I
35.0  -  39.9   ->  OBESIDAD II
40.0  -  49.9   ->  OBESIDAD III
  >  50.0       ->  OBESIDAD IV


  
IMC = PESO  /  (ESTATURA * ESTATURA)'''

def calcular_imc(peso, estatura):
    imc = (peso)/(estatura ** 2)
    return imc

peso = float (input("Ingrese peso en kg: "))
estatura = float (input ("Ingrese estatura en metros: "))

IMC = round(calcular_imc(peso, estatura), 2)

if IMC < 18.5:
    print("La calificación de su IMC es: Bajo peso.")
elif 18.5 <= IMC <= 24.9:
    print("La calificación de su IMC es: Normal.")
elif 25.0 <= IMC <= 29.9:
    print("La calificación del IMC es: Sobrepeso.")
elif 30.0 <= IMC <= 34.9:
    print ("La calificación del IMC es: Obesidad I.")
elif 35.0 <= IMC <= 39.9:
    print("La calificación del IMC es: Obesidad II.")
elif 40.0 <= IMC <= 49.9:
    print("La calificación del IMC es: Obesidad III.")
else:
    print("La calificación del IMC es: Obesidad IV.")