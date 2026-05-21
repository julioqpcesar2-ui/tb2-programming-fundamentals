# ==========================================
# MODULO DE VENTAS - ELIORODAS
# ==========================================

# Este modulo luego se integrara
# con Inventario y Reportes

# =========================
# DATOS COMPARTIDOS
# =========================

productos = ["Platos", "Tazas", "Cubiertos"]
stock = [10, 15, 8]
precios = [20.0, 15.0, 5.0]

# Variable global de caja
caja_total = 0

# Lista para guardar ventas
ventas = []


# =========================
# MODULO VENTAS
# =========================

def modulo_ventas():

    global caja_total

    continuar = "si"

    while continuar == "si":

        print("\n================================")
        print("       MODULO DE VENTAS")
        print("================================")

        # Mostrar productos
        print("\nPRODUCTOS DISPONIBLES:\n")

        for i in range(len(productos)):
            print(i + 1, ".",
                  productos[i],
                  "- Stock:", stock[i],
                  "- Precio: S/", precios[i])

        # =========================
        # INGRESAR PRODUCTO
        # =========================

        producto = input("\nIngrese nombre del producto: ")

        # Verificar si existe
        if producto in productos:

            posicion = productos.index(producto)

            # =========================
            # INGRESAR CANTIDAD
            # =========================

            cantidad = int(input("Ingrese cantidad: "))

            # Validar cantidad
            if cantidad > 0:

                # Validar stock
                if cantidad <= stock[posicion]:

                    # =========================
                    # CALCULAR TOTAL
                    # =========================

                    total = cantidad * precios[posicion]

                    # =========================
                    # ACTUALIZAR STOCK
                    # =========================

                    stock[posicion] = stock[posicion] - cantidad

                    # =========================
                    # GUARDAR VENTA
                    # =========================

                    caja_total = caja_total + total

                    ventas.append([
                        producto,
                        cantidad,
                        total
                    ])

                    # =========================
                    # MOSTRAR RESUMEN
                    # =========================

                    print("\n================================")
                    print("       VENTA REALIZADA")
                    print("================================")

                    print("Producto:", producto)
                    print("Cantidad:", cantidad)
                    print("Precio Unitario: S/", precios[posicion])
                    print("Total Venta: S/", total)
                    print("Stock Restante:", stock[posicion])

                else:
                    print("\nERROR: Stock insuficiente")

            else:
                print("\nERROR: Cantidad invalida")

        else:
            print("\nERROR: Producto no existe")

        # =========================
        # REPETIR VENTAS
        # =========================

        continuar = input(
            "\n¿Desea realizar otra venta? (si/no): "
        )

    # =========================
    # CIERRE MODULO
    # =========================

    print("\n================================")
    print("      CIERRE DE VENTAS")
    print("================================")

    print("Caja total acumulada: S/", caja_total)

    print("\nVentas realizadas:")

    for venta in ventas:
        print(
            "Producto:", venta[0],
            "- Cantidad:", venta[1],
            "- Total: S/", venta[2]
        )


# =========================
# EJECUTAR MODULO
# =========================

modulo_ventas()