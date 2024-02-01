def agregar_persona(registro, nombre, edad, estado_civil):
    # La función agregar_persona toma cuatro parámetros: registro, nombre, edad y estado_civil.
    # Crea un diccionario 'persona' con claves 'Nombre', 'Edad' y 'Estado_Civil'.
    # Luego, agrega esta entrada al diccionario 'registro' con la clave 'nombre'.

    persona = {
        'Nombre': nombre,
        'Edad': edad,
        'Estado_Civil': estado_civil,

    }
    registro[nombre]= persona
def mostrar_registro(registro):
    # La función mostrar_registro toma un parámetro: registro.
    print("\nRegistro actual:")
    # Itera sobre cada elemento (nombre, persona) en el diccionario 'registro'.
    for nombre, persona in  registro.items() :
        # Imprime información sobre cada persona en el registro.
        print(f"Nombre:{persona['Nombre']}, Edad:{persona['Edad']}, Estado Civil: {persona['Estado_Civil']}")
def main():
    # La función principal main no toma ningún parámetro.
    registro ={}

    agregar_persona( registro, 'Juan', 25,'Casado')
    mostrar_registro(registro)# Muestra el registro actual.

    agregar_persona( registro, 'Carlos', 22,'casado')
    mostrar_registro(registro)# Muestra el registro actual.


    agregar_persona( registro, 'Ander', 18,'soltero')
    mostrar_registro(registro)# Muestra el registro actual.

    agregar_persona(registro, 'Isaias', 40, 'Casado')
    mostrar_registro(registro)# Muestra el registro actual.

if __name__=="__main__":
  main()# Si el script se ejecuta directamente, llama a la función principal 'main'.