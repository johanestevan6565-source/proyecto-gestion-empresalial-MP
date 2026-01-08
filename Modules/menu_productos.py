from Functions import functions_productos

def menu_productos():
    
    while True: # Bucle del menú de productos
        print("\n=== MENÚ DE GESTIÓN DE PRODUCTOS ===")
        print("1. Agregar producto")
        print("2. Editar producto")
        print("3. Eliminar producto")
        print("4. Listar productos")
        print("5. cambiar precio de producto")
        print("6. Reactivar producto")
        print("7. Salir al menú principal\n")
        print("="*30)
        opcion = input("\nSeleccione una opción: ")

        if opcion == '1': # Agregar producto

            while True: # Bucle para agregar productos
                print("\n=== AGREGAR PRODUCTO ===")
                print("ingrese 'salir' en cualquier momento para volver al menu\n")
                nombre = functions_productos.pedir_nombre_producto()
                if nombre is None:
                    print("\nVolviendo al menú principal...")
                    break
                precio = functions_productos.pedir_precio_producto()
                if precio is None:
                    print("Volviendo al menú principal.")
                    break
                functions_productos.agregar_producto(nombre, precio)
                print("\nProducto agregado exitosamente con ID:", functions_productos.generar_id(functions_productos.cargar_productos()))
                print ("="*30)

        elif opcion == '2': # Editar producto
            print("\n=== EDITAR PRODUCTO ===")
            print("\n" + "="*30 + "\n" + "   LISTA DE PRODUCTOS")
            functions_productos.listar_productos()
            print("="*30 + "\n")

            pid = functions_productos.pedir_producto_a_editar()
            if pid is None:
                    return
            nuevo_nombre = functions_productos.pedir_nuevo_nombre_producto(pid)
            if nuevo_nombre is None:
                    return
            if functions_productos.editar_producto(pid, nuevo_nombre):
                print("Producto actualizado exitosamente.")
            else:
                print("Error al actualizar el producto.")

        elif opcion == '3': # Eliminar producto
            print("\n=== ELIMINAR PRODUCTO ===")
            print("\n" + "="*30 + "\n" + "   LISTA DE PRODUCTOS")
            functions_productos.listar_productos(activo=True)
            print("="*30)
            pid = functions_productos.pedir_producto_a_eliminar()
            if pid is None:
                continue
            if functions_productos.eliminar_producto(pid):
                print("Producto eliminado exitosamente.")
            else:
                 print("Error al eliminar el producto.")

        elif opcion == '4': # Listar productos
            print("\n" + "="*30 + "\n" + "   LISTA DE PRODUCTOS")
            functions_productos.listar_productos()
            print("="*30)
            
        elif opcion == '5': # Cambiar precio de producto
            print("\n=== CAMBIAR PRECIO DE PRODUCTO ===")
            print("\n" + "="*30 + "\n" + "   LISTA DE PRODUCTOS")
            functions_productos.listar_productos()
            print("="*30)
            seleccionado = functions_productos.seleccionar_producto(activo=True)
            if not seleccionado:
                continue
            pid, datos = seleccionado
            nuevo_precio = input("Nuevo precio: ").strip()
            functions_productos.editar_precio(pid, nuevo_precio)
            print("Precio actualizado.")

        elif opcion == '6': # Reactivar producto
            print("\n=== REACTIVAR PRODUCTO ===")
            print("\n" + "="*30 + "\n" + "   LISTA DE PRODUCTOS INACTIVOS")
            productos_inactivos = functions_productos.listar_productos(activo=False)
            print("="*30)
            seleccionado = functions_productos.seleccionar_producto(activo=False)
            if not seleccionado:
                continue
            pid, datos = seleccionado
            productos = functions_productos.cargar_productos()
            confirmacion = input(f"¿Está seguro de que desea reactivar el producto '{datos['nombre']}'? (s/n): ").strip().lower()
            if confirmacion == 's':
                if functions_productos.reactivar_producto(pid):
                    print("Producto reactivado exitosamente.")
                else:
                    print("Error al reactivar el producto.")
        else:
            print("Opción inválida. Por favor, intente de nuevo.")