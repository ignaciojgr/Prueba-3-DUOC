import json
inventario = []

# Función que valida los inputs que deban tener sólo letras y espocios
def validar_letras_y_espacios(textodeEntrada):
    while True:
        input_del_usuario = input(textodeEntrada)
        if input_del_usuario == "":
            return None
        if all(caracter.isalpha() or caracter.isspace() for caracter in input_del_usuario):
            return input_del_usuario
        else:
            print("Error. Debe ingresar solo letras o espacios")

# Función que valida los inputs que deban tener solo números
def validar_numeros(textodeEntrada):
    while True:
        input_del_usuario = input(textodeEntrada)
        if input_del_usuario == "":
            return None
        try:
            input_del_usuario = float(input_del_usuario)
            return input_del_usuario
        except ValueError:
            print("Error. Debe ingresar solo números")

# Función que añade un producto a la lista inventario
def ingresar_producto():
    nombre = validar_letras_y_espacios("Ingrese el nombre del producto: ")
    precio = validar_numeros("Ingrese el precio del producto: ")
    cantidad = validar_numeros("Ingrese la cantidad el producto: ")

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    })

# Función que actualiza un producto
def actualizar_producto(inventario, nombredeArchivo="inventario.json"):
    if not inventario:
        print("No hay productos en el inventario.")
        return
    print("Productos en inventario: ")
    for indice, producto in enumerate(inventario, start=1):
        print(f"{indice}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    indice = validar_numeros("Ingrese el producto a actualizar por numero: ")
    indice = int(indice)
    if indice < 0 or indice > len(inventario):
        print("Indice fuera de rango.")
        return
    
    producto_seleccionado = inventario[indice-1]
    nuevo_nombre = validar_letras_y_espacios("Ingrese el nuevo nombre: ") or producto_seleccionado["nombre"]
    nuevo_precio = validar_numeros("Ingrese el nuevo precio: ") or producto_seleccionado["precio"]
    nueva_cantidad = validar_numeros("Ingrese la nueva cantidad: ") or producto_seleccionado["cantidad"]

    inventario[indice - 1] = {
        "nombre": nuevo_nombre,
        "precio": nuevo_precio,
        "cantidad": nueva_cantidad,
    }
    print("Producto actualizado exitosamente.")
    
    guardar_en_formato_json(inventario, nombredeArchivo)

# Función que muestra todos los productos ingresados en el inventario
def mostrar_inventario(inventario):
    if not inventario:
        print("No hay gastos registrados.")
        return
    for indice, producto in enumerate(inventario, start=1):
        nombre = producto.get("nombre", "Nombre no proporcionado")
        precio = producto.get("precio", "Precio no proporcionado")
        cantidad = producto.get("cantidad", "Cantidad no proporcionada")
        print(f"{indice} Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}")

# Función que crea una archivo JSON
def guardar_en_formato_json(inventario, nombredeArchivo):
    with open(nombredeArchivo, mode="w", newline="", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=3)
    print("Los archivos se han actualizado correctamente. ")

# Función que muestra el menu principal
def menu():
    while True:
        print("\nBienvenido al menú de inventario:\n"
            "1. Ingresar producto\n"
            "2. Mostrar inventario\n"
            "3. Actualizar producto\n"
            "4. Guardar archivo en formato JSON\n"
            "5. Salir del programa"
            )
        opcion_ingresada = validar_numeros("Ingrese la opción deseada: ")
        if opcion_ingresada == 1:
            ingresar_producto()
        elif opcion_ingresada == 2:
            mostrar_inventario(inventario)
        elif opcion_ingresada == 3:
            actualizar_producto(inventario)
        elif opcion_ingresada == 4:
            guardar_en_formato_json(inventario, nombredeArchivo="inventario.json")
        elif opcion_ingresada == 5:
            break
        else:
            print("Error. Opción no válida. Intente de nuevo.")

# Ejecución del menu principal
menu()



    


    

    