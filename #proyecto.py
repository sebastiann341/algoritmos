#proyecto

# Obtener datos del usuario
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
objetivo = input("Ingrese su objetivo (subir/bajar/mantener peso): ").lower()

# Inicializar listas de alimentos recomendados y para evitar
alimentos_recomendados = []
alimentos_evitar = []

# Inicializar un diccionario de alimentos y recetas
alimentos_recetas = {
    "papas": "Receta de papas asadas: Lava y corta las papas en rodajas finas. Agrega aceite de oliva, sal y hierbas. Hornea hasta que estén doradas.",
    "carne magra": "Receta de pollo a la parrilla: Marina pechugas de pollo en especias y luego ásalas a la parrilla hasta que estén cocidas.",
    "arroz integral": "Receta de arroz integral: Cocina el arroz integral en agua o caldo de verduras hasta que esté tierno y esponjoso.",
    # Agrega más alimentos y recetas según sea necesario
}

# Lógica de recomendaciones
if objetivo == "subir":
    if edad < 30:
        alimentos_recomendados.extend(["papas", "carne magra", "arroz integral", "pollo", "frutos secos"])
    else:
        alimentos_recomendados.extend(["batidos de proteínas", "aguacate", "frutos secos", "aceite de oliva"])
    alimentos_evitar.extend(["golosinas", "refrescos azucarados", "comida rápida"])
elif objetivo == "bajar":
    if edad < 30:
        alimentos_recomendados.extend(["verduras de hoja verde", "pavo magro", "quinoa", "pescado", "frutas"])
    else:
        alimentos_recomendados.extend(["verduras de hoja verde", "pavo magro", "quinoa", "pescado", "frutas", "salmón"])
    alimentos_evitar.extend(["comida chatarra", "refrescos azucarados", "postres altos en calorías"])
else:
    alimentos_recomendados.extend(["verduras variadas", "proteínas magras (pollo, pavo, pescado)", "granos enteros", "frutas"])
    alimentos_evitar.extend(["alimentos procesados", "refrescos azucarados", "azúcares añadidos"])

# Mostrar recomendaciones
print("Alimentos recomendados:", alimentos_recomendados)
print("Alimentos a evitar:", alimentos_evitar)

#  elija un alimento de la lista de recomendados
eleccion = input("Elige un alimento de la lista de recomendados para ver una receta: ").lower()

# receta correspondiente
if eleccion in alimentos_recetas:
    print("Receta para", eleccion.capitalize() + ":")
    print(alimentos_recetas[eleccion])
else:
    print("Lo siento, no tenemos una receta disponible para ese alimento.")
