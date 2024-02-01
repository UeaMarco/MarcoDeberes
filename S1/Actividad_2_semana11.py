def temperatura_promedio(ciudades_temperaturas):

    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Creamos un diccionario de ciudades y temperaturas
ciudades_temperaturas = {
    "Nueva York": [22, 25, 26, 24, 23],
    "Los Ángeles": [28, 30, 29, 31, 27],
    "Chicago": [21, 20, 22, 18, 19],
    "Miami": [32, 33, 34, 30, 32],
    "Dallas": [26, 28, 27, 29, 25]
}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")
