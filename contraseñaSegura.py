def compPassword(new_password):
    return len(new_password) >= 8
def compUpper(new_password):
    return any(i.isupper() for i in new_password)
def compNumber(new_password):
    return any(i.isnumeric() for i in new_password)

new_password = input ("Ingrese contraseña: ")
caracteres_min = compPassword(new_password) 
upper_min = compUpper(new_password)
number_min = compNumber(new_password)

if caracteres_min and upper_min and number_min:
    print ("Contraseña actualizada.")

else:
    print ("Ingrese una contraseña válida.")
    exit()
    

