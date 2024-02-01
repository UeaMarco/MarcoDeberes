
Información_personal_dicc= {
    "Nobre": "Marco",
    "Ciudad": "Orellana",
    "Edad": "24",
    "Profesión": "Técnico",
}

#Cambiar el valor de la clave "Ciudad" a "Quito"
Información_personal_dicc["Ciudad"] = "Quito"

#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
if"teléfono" not in Información_personal_dicc:
    Información_personal_dicc["teléfono"] = 28967

#Eliminar la clave "Edad"
del Información_personal_dicc["Edad"]


for clave,valor in Información_personal_dicc.items():
    print(clave + ":" + str(valor))

print("ciudad modificada:", Información_personal_dicc["Ciudad"])