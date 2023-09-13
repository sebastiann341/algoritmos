#ejercicio 6
print ("- Inicio del programa -")

edad1 = int(input("Cual es tu edad?"))


if edad1 < 18:
    print ("menor de edad?")
else:    
    print ("mayor de edad?")

print ("---")
print ("- Modulo de seguridad -")

#Despues de establecer si es mayor de edad, le solicitamos una contraseña

print ("Su contraseña fue enviada a su correo")
ClaveMayorEdad = "contraseña"
password = input("Por favor digita tu clave ")

if ClaveMayorEdad ==  password.lower ():
    print ("Contraseña correcta :)")
else:    
    print ("Contraseña erronea :(")

print ("---")
print ("-Modulo de interaccion -")

print ("Escriba una palabra para seguir con la autenticacion")

frese = input("Introduce tu palabra")


#Si se desea remplazor la contrase solicite al usuario escribir en diferentes numeros o letas la nueva contraseña o solicite un parametro de validacion

vocal = input("Introduce una vocal en minuscula ")

print (frese.replace(vocal, vocal.upper))

print ("Usted a completado los 3 modulos de autenticacion ")