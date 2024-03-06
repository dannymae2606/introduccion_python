'''Programa que calcula el IVA de una compra, siendo el IVA del 19% 
sobre el valor total de la compra'''

def iva_calculado(valorCompra):
    total = valorCompra * 1.19
    return total

valorCompra = float (input("Ingrese el valor de la compra:  "))
total_compra = iva_calculado(valorCompra)
print ("El total de la compra con IVA (19%) es:  ", total_compra)