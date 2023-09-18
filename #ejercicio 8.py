#ejercicio 8
# el progrma que vamos a realizar tiene como finalida relaizar un ciclo un donde le pida al usuario 
#ingresar hsta 3 un numero esta caso la edad y cuando genere la varible correcta genere la variable 
#correcta ejecute en pantalla la siguente accion

print ("inicio")
nombre = str((input("Ingrese su nombre ")))
edades_Permitdas = (15,16,17,18,19,20)
edad = int((input("Ingrese su edad ")))
# Verificar si la edad está permitida
if edad in edades_Permitdas:
    print("Su edad está permitida?")
    cedula = ((input("numero de cedula ")))
    if cedula.isdigit() and len(cedula) > 9:
        print("La ceduala es invalida")
        if cedula == "12345678910":
            ubicacion = "Ubicación A1"
        elif cedula == "12345678911":
            ubicacion = "Ubicación A2"
        else:
            ubicacion = "sin ubicacion asignada"
        print(f"Su ubicación es: {ubicacion}")
    else:
        print("No es apto para la entrada")
else:
    print("Su edad no está permitida.")