#ejercicio 4

#Vamos a crear un código que realice por pantalla un calculo de variables, que nos permita sumar,
#restar y hacer operaciones para mostar al final un resultado de cada operación y a su vez crear una tabla de
#la verdad y cada una de las operaciones usando "bool" o usando "and" y "or"

print ("Este programa no se debe hacer por chat gpt,el que lo haga le bajo nota")

a= input ("Deme un numero en pantalla  ")
b= input ("Deme un numero mayor que el anterior ")


a= int (a)
b= int (b)

print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a%b)


print ("Tabla de verdad relacionada con and o y")
print ((str(a==a)) + "and" + str (a==a) + "--->" + str(a==a))
print ((str (a==a)) + "and" + str (a==b) + "--->" + str(a==b))
print ((str (a==b)) + "and" + str (a==b) + "--->"+ str (a==b))
print ((str (a==b)) + "and" + str (a==a) + "--->" + str (a==b))


print ("Tabla deverdad relacionada con o")
print ((str(a==a)) + "and" + str (a==a) + "--->" + str(a==a))
print ((str (a==a)) + "and" + str (a==b) + "--->" + str(a==a))
print ((str (a==b)) + "and" + str (a==b) + "--->"+ str (a==b))
print ((str (a==b)) + "and" + str (a==a) + "--->" + str (a==a))


print ("Tabla de verdad")
print (bool (a==a))
print (bool (a==b))
print (bool (b==a))
print (bool (b==b))
