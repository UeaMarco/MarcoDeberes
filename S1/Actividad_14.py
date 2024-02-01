def Productos_descuento(producto,precio):
    print(f"Producto {producto} ")
Productos_descuento("Secadora", 500)
Productos_descuento("Lavadora", 600)

def calcular_descuento(producto, precio):
    descuento = precio * 0.1
    precio_con_descuento = precio - descuento
    print(f"Artefacto {producto}  ${precio:.2f} dolares.")
    print(f"Descuento ${precio_con_descuento:.2f} dolares.")
calcular_descuento("Computadora", 500)
calcular_descuento("Refrigeradora", 600)