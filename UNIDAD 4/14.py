import tkinter as tk
from tkinter import ttk
from datetime import datetime

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Gestión de Eventos")
        self.window.geometry("600x400")

        # Contenedor principal
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Área de visualización de eventos
        self.events_frame = ttk.Frame(self.main_frame)
        self.events_frame.pack(fill=tk.BOTH, expand=True)

        # Lista de eventos
        self.events_list = ttk.Treeview(self.events_frame, columns=("Fecha", "Hora", "Descripción"))
        self.events_list.pack(fill=tk.BOTH, expand=True)
        self.events_list.heading("#0", text="Evento")
        self.events_list.heading("Fecha", text="Fecha")
        self.events_list.heading("Hora", text="Hora")
        self.events_list.heading("Descripción", text="Descripción")

        # Área de entrada de datos
        self.data_frame = ttk.Frame(self.main_frame)
        self.data_frame.pack(fill=tk.X)

        # Etiquetas
        self.fecha_label = ttk.Label(self.data_frame, text="Fecha:")
        self.hora_label = ttk.Label(self.data_frame, text="Hora:")
        self.descripcion_label = ttk.Label(self.data_frame, text="Descripción:")

        # Campos de entrada
        self.fecha_entry = ttk.Entry(self.data_frame)
        self.hora_entry = ttk.Entry(self.data_frame)
        self.descripcion_entry = ttk.Entry(self.data_frame)

        # Posicionamiento de etiquetas y campos de entrada
        self.fecha_label.grid(row=0, column=0, sticky=tk.W)
        self.fecha_entry.grid(row=0, column=1, sticky=tk.E)
        self.hora_label.grid(row=1, column=0, sticky=tk.W)
        self.hora_entry.grid(row=1, column=1, sticky=tk.E)
        self.descripcion_label.grid(row=2, column=0, sticky=tk.W)
        self.descripcion_entry.grid(row=2, column=1, sticky=tk.E)

        # Área de botones
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.pack(fill=tk.X)

        # Botones
        self.add_button = ttk.Button(self.buttons_frame, text="Agregar Evento", command=self.add_event)
        self.delete_button = ttk.Button(self.buttons_frame, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.exit_button = ttk.Button(self.buttons_frame, text="Salir", command=self.exit)

        # Posicionamiento de botones
        self.add_button.pack(side=tk.LEFT)
        self.delete_button.pack(side=tk.LEFT)
        self.exit_button.pack(side=tk.RIGHT)

        # Inicialización de variables
        self.events = []

    # Función para agregar un evento
    def add_event(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validación de datos
        if not fecha or not hora or not descripcion:
            return

        # Convertir fecha y hora a formato datetime
        try:
            fecha_hora = datetime.strptime(f"{fecha} {hora}", "%d/%m/%Y %H:%M")
        except ValueError:
            return

        # Agregar evento a la lista
        self.events.append((fecha, hora, descripcion))
        self.events_list.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar campos de entrada
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete()
