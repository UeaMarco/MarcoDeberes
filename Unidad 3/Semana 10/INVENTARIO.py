class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

class ListaProductos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto in self.productos:
            if nombre is not None:
                self.productos[id_producto].nombre = nombre
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)

    def mostrar_lista_productos(self):
        for producto in self.productos.values():
            print(producto)

class InterfazUsuario:
    def __init__(self):
        self.lista_productos = ListaProductos()

    def menu(self):
        while True:
            print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Lista de Productos\n6. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '6':
                break
            elif opcion == '1':
                self.agregar_producto()
            elif opcion == '2':
                self.eliminar_producto()
            elif opcion == '3':
                self.actualizar_producto()
            elif opcion == '4':
                self.buscar_producto()
            elif opcion == '5':
                self.mostrar_lista_productos()

    def agregar_producto(self):
        id_producto = input("Ingrese el ID del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        producto = Producto(id_producto, nombre, cantidad, precio)
        self.lista_productos.agregar_producto(producto)

    def eliminar_producto(self):
        id_producto = input("Ingrese el ID del producto a eliminar: ")
        self.lista_productos.eliminar_producto(id_producto)

    def actualizar_producto(self):
        id_producto = input("Ingrese el ID del producto a actualizar: ")
        print("Ingrese los nuevos valores o deje en blanco para mantener los actuales:")
        nombre = input(f"Nuevo nombre del producto ({self.lista_productos.productos[id_producto].nombre}): ") or self.lista_productos.productos[id_producto].nombre
        cantidad = int(input(f"Nueva cantidad del producto ({self.lista_productos.productos[id_producto].cantidad}): ") or self.lista_productos.productos[id_producto].cantidad)
        precio = float(input(f"Nuevo precio del producto ({self.lista_productos.productos[id_producto].precio}): ") or self.lista_productos.productos[id_producto].precio)
        self.lista_productos.actualizar_producto(id_producto, nombre, cantidad, precio)

    def buscar_producto(self):
        nombre = input("Ingrese el nombre o parte del nombre del producto a buscar: ")
        self.lista_productos.buscar_producto(nombre)

    def mostrar_lista_productos(self):
        self.lista_productos.mostrar_lista_productos()

if __name__ == "__main__":
    interfaz = InterfazUsuario()
    interfaz.menu()
