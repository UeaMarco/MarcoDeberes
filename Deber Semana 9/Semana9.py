print("Bienvenido")
cantidad = []
productos= []
precio= []

while True:
    print("""
    (1) Añadir productos
    (2) Buscar productos
    (3) Modificar productos
    (4) Ver productos 
    (5) Eliminar productos
    (6) Exit
    """)
    respuesta = int(input("Ingrese su opción: "))
    if respuesta == 1:
        ac = int(input("Ingrese la cantidad de su producto: "))
        ap = input("Ingrese el nombre de su producto")
        apre = int(input("Ingrese el precio de su producto"))

        cantidad.append(ac)
        productos.append(ap)
        precio.append(apre)

    elif respuesta ==2:
        buscador=input("ingrese el nombre de el producto:")
        posición= productos.in1dex(buscador)
        print("la cantidad de el producto es: " , cantidad[posición])
        print("El nombre de le prodcuto es:", productos[posición])
        print("el precio de el producto es:", precio[posición])

    elif respuesta == 3:
        buscador= input("Ingrese el nomnre de el producto a modificar:")
        posición=productos.index(buscador)
        ac=int(input("ingrese la cantidad de su prodcuto:"))
        ap=input("ingrese el precio de su producto:")
        cantidad[posición] = ac
        productos[posición]= ap
        precio[posición]= apre

    elif respuesta == 4:
        print("la cantidad es:", cantidad)
        print("El nombre es:", productos)
        print("El precio es:", precio)
    else:
        break
