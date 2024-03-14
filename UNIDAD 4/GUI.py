import tkinter as tk
from datetime import datetime

# Función para actualizar el reloj
def actualizar_reloj():
    now = datetime.now()
    hora_actual = now.strftime("%H:%M:%S")
    label_reloj.config(text=hora_actual)
    label_reloj.after(1000, actualizar_reloj)  # Actualizar cada segundo

# Variables para control de acceso
usuarios = {
    "maria": "1234",
    "rosa": "321"
}
intentos_restantes = 3

# Función para verificar el código de acceso
def verificar_acceso():
    global intentos_restantes

    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()

    if usuario in usuarios and usuarios[usuario] == contrasena:
        # Acceso correcto
        ventana_acceso.destroy()
        mostrar_ventana_principal(usuario)
    else:
        # Acceso incorrecto
        intentos_restantes -= 1
        label_error.config(text=f"Acceso incorrecto. Intentos restantes: {intentos_restantes}")

        if intentos_restantes == 0:
            # Bloquear acceso
            boton_ingresar.config(state="disabled")
            label_error.config(text="Acceso bloqueado. Contacte al administrador.")

# Función para mostrar la ventana principal
def mostrar_ventana_principal(usuario):
    # Crear la ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title(f"Bienvenido, {usuario.capitalize()}")
    ventana_principal.geometry("300x300")

    # Obtener la fecha y hora actual
    now = datetime.now()

    # Etiquetas para mostrar la fecha y hora actual en números
    label_fecha_numero = tk.Label(ventana_principal, text=f"Fecha actual: {now.day}/{now.month}/{now.year}")
    label_fecha_numero.pack(pady=5)

    label_hora_numero = tk.Label(ventana_principal, text=f"Hora actual: {now.hour}:{now.minute}:{now.second}", font=("Arial", 18))
    label_hora_numero.pack(pady=5)

    # Ejecutar el bucle de eventos de la ventana principal
    ventana_principal.mainloop()

# Crear la ventana de acceso
ventana_acceso = tk.Tk()
ventana_acceso.title("Acceso al sistema")
ventana_acceso.geometry("300x250")  # Aumenta la altura para dar espacio al reloj

# Etiquetas y entradas de usuario y contraseña
label_usuario = tk.Label(ventana_acceso, text="Usuario:")
label_usuario.grid(row=0, column=0, padx=5, pady=5)
entrada_usuario = tk.Entry(ventana_acceso)
entrada_usuario.grid(row=0, column=1, padx=5, pady=5)

label_contrasena = tk.Label(ventana_acceso, text="Contraseña:")
label_contrasena.grid(row=1, column=0, padx=5, pady=5)
entrada_contrasena = tk.Entry(ventana_acceso, show="*")
entrada_contrasena.grid(row=1, column=1, padx=5, pady=5)

# Botón para ingresar y etiqueta de error
boton_ingresar = tk.Button(ventana_acceso, text="Ingresar", command=verificar_acceso)
boton_ingresar.grid(row=2, column=1, padx=5, pady=5)

label_error = tk.Label(ventana_acceso, text="")
label_error.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Etiqueta para mostrar el reloj (hora actual)
label_reloj = tk.Label(ventana_acceso, text="", font=("Arial", 24))  # Cambia el tamaño de letra aquí
label_reloj.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")  # Alinea la etiqueta al centro horizontal y verticalmente

# Actualizar el reloj
actualizar_reloj()

# Ejecutar el bucle de eventos de la ventana de acceso
ventana_acceso.mainloop()