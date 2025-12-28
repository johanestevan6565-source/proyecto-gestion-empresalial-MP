from Functions import functions_productos

def menu_productos():
    
    while True: # Bucle del menú de productos
        print("\n=== MENÚ DE GESTIÓN DE PRODUCTOS ===")
        print("1. Agregar producto")
        print("2. Editar producto")
        print("3. Eliminar producto")
        print("4. Listar productos")
        print("5. cambiar precio de producto")
        print("6. Salir al menú principal\n")
        opcion = input("Seleccione una opción: ")

        if opcion == '1': # Agregar producto

            nombre = input("Ingrese el nombre del producto: ")
            precio = input("Ingrese el precio del producto: ")
            functions_productos.agregar_producto(nombre, precio)
            print("Producto agregado exitosamente con ID:", functions_productos.generar_id(functions_productos.cargar_productos()))

        elif opcion == '2': # Editar producto
            print("\n=== EDITAR PRODUCTO ===")
            print("\n" + "="*30 + "\n" + "   LISTA DE PRODUCTOS")
            todos_productos = functions_productos.listar_productos()
            if todos_productos: # Verifica si hay productos para mostrar
                print("="*30)
                print("\nDigite 'salir' para volver al menu\n")
                while True:
                    prodID = input("Ingrese el ID del producto a editar: ").strip()
                    if prodID.lower().strip() == 'salir':
                        break
                    resultados = functions_productos.obtener_producto_flexible(prodID)
                    if not resultados:
                        print("No se encontró un producto con ese ID.")
                        continue
                    if len (resultados) > 1:
                        print("Se encontraron múltiples productos con ese nombre. Por favor, use el ID para mayor precisión.")
                        for pid, datos in resultados:
                            print(f"{pid} - {datos['nombre']}")
                            print("sea mas preciso")
                        continue
                    pid, datos = resultados[0]
                    print(f"Producto seleccionado: {pid} - {datos['nombre']}")
                    nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").strip() 
                    if functions_productos.editar_producto(pid, nuevo_nombre):
                        print("Producto actualizado exitosamente.")
                    else:
                        print("Error al actualizar el producto.")
        elif opcion == '3': # Eliminar producto
            print("\n=== ELIMINAR PRODUCTO ===")
            print("\n" + "="*30 + "\n" + "   LISTA DE PRODUCTOS")
            todos_productos = functions_productos.listar_productos()
            if todos_productos: # Verifica si hay productos para mostrar
                print("="*30)
                print("\nDigite 'salir' para volver al menu\n")
                while True:
                    prodID = input("Ingrese el ID del producto a eliminar: ").strip()
                    if prodID.lower().strip() == 'salir':
                        break
                    resultados = functions_productos.obtener_producto_flexible(prodID)
                    if not resultados:
                        print("No se encontró un producto con ese ID.")
                        continue
                    if len (resultados) > 1:
                        print("Se encontraron múltiples productos con ese nombre. Por favor, use el ID para mayor precisión.")
                        for pid, datos in resultados:
                            print(f"{pid} - {datos['nombre']}")
                            print("sea mas preciso")
                        continue
                    pid, datos = resultados[0]
                    confirmacion = input(f"¿Está seguro de que desea eliminar el producto {pid} - {datos['nombre']}? (s/n): ").strip().lower()
                    if confirmacion == 's':
                        if functions_productos.eliminar_producto(pid):
                            print("Producto eliminado exitosamente.")
                        else:
                            print("Error al eliminar el producto.")
                    else:
                        print("Eliminación cancelada.")

        elif opcion == '4': # Listar productos
            producto = functions_productos.listar_productos()
            if producto: # Verifica si hay productos para mostrar
                print("\n" + "="*30 + "\n" + "   LISTA DE PRODUCTOS")
                for id, datos in producto.items():
                    estado = "Activo" if datos['activo'] else "Inactivo"
                    print(f"ID: {id}, Nombre: {datos['nombre']}, Precio: {datos['precio']}, Estado: {estado}")
                print("="*30)
            
        elif opcion == '5': # Cambiar precio de producto
            print("\n=== CAMBIAR PRECIO DE PRODUCTO ===")
            print("\n" + "="*30 + "\n" + "   LISTA DE PRODUCTOS")
            todos_productos = functions_productos.listar_productos()
            print("="*30)
            print("\nDigite 'salir' para volver al menu\n")
            while True:
                prodID = input("Ingrese el ID del producto a editar: ").strip()
                if prodID.lower() == 'salir':
                    break
                resultados = functions_productos.obtener_producto_flexible(prodID)
                if not resultados:
                    print("No se encontró un producto con ese ID.")
                    continue
                if len (resultados) > 1:
                    print("Se encontraron múltiples productos con ese nombre. Por favor, use el ID para mayor precisión.")
                    for pid, datos in resultados:
                        print(f"{pid} - {datos['nombre']}")
                        print("sea mas preciso")
                    continue
                pid, datos = resultados[0]
                print(f"Producto seleccionado: {pid} - {datos['nombre']} (Precio actual: {datos['precio']})")
                nuevo_precio = input("Ingrese el nuevo precio del producto: ").strip() 
                if functions_productos.editar_precio(pid, nuevo_precio):
                    print("Precio del producto actualizado exitosamente.")
                else:
                    print("Error al actualizar el precio del producto.")
        elif opcion == '6': # Salir al menú principal
            print("Volviendo al menú principal.")
            break

        else:
            print("Opción inválida. Por favor, intente de nuevo.")