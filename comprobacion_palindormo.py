'''Comprobar si una palabra o frase es palíndormo
Ejemplos:
Reconocer
Anna
Ojo rojo
La ruta nos aportó otro paso natural

Tener en cuenta que no se tienen en cuenta ni los espacios ni las
mayúsculas ni las tildes
'''


def esPalindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra = palabra.replace(",", "")
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra. replace("ú", "u")

    return palabra == palabra [::-1]

palabra = input("Ingrese palabra o frase para ser comprobada: ")
compPalindromo =esPalindromo(palabra)

if compPalindromo:
    print (f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es palíndromo.")


