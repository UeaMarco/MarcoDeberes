import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

class Inventario:
    def __init__(self, archivo_inventario):
        self.productos = {}
        self.archivo_inventario = archivo_inventario

    def cargar_inventario(self):
        try:
            with open(self.archivo_inventario, 'r') as file:
                for line in file:
                    id_producto, nombre, cantidad, precio = line.strip().split(',')
                    self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo.")
            self.guardar_inventario()
        except PermissionError:
            print("No se tiene permiso para acceder al archivo de inventario.")

    def guardar_inventario(self):
        try:
            with open(self.archivo_inventario, 'w') as file:
                for producto in self.productos.values():
                    file.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("No se tiene permiso para guardar el archivo de inventario.")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            self.guardar_inventario()
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)

# Interfaz de usuario en la consola
def menu(inventario):
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '6':
            break
        elif opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad del producto (deje en blanco para mantener la misma): ")
            if cantidad:
                cantidad = int(cantidad)
            precio = input("Ingrese el nuevo precio del producto (deje en blanco para mantener el mismo): ")
            if precio:
                precio = float(precio)
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre o parte del nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()

if __name__ == "__main__":
    archivo_inventario = "inventario.txt"
    inventario = Inventario(archivo_inventario)
    inventario.cargar_inventario()
    menu(inventario)