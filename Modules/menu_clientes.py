from Functions import functions_clientes

def menu_clientes():

    while True: # Bucle principal del programa

        print("\n=== MENU DE GESTION DE CLIENTES ===") # Menú de gestión de clientes
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Salir al menu principal\n")
        opcion = input("Seleccione una opcion: ")

        if opcion == '1': # Agregar cliente
            while True: # Bucle para agregar clientes
                nombre = input("\nIngrese el nombre del cliente (o 'salir' para volver al menú principal): ")
                if nombre.lower().strip() == 'salir': # Salir al menú principal
                    print("Volviendo al menú principal.")
                    break
                ok, resultado, mensaje = functions_clientes.agregar_cliente(nombre)
                print(mensaje) 
                if ok: # Cliente agregado exitosamente
                    print(f"{mensaje} ID: {resultado}")
                    break
                else: # Error al agregar cliente
                    print(f"Error: {mensaje}")

        elif opcion == '2': # Listar clientes
            print("\n" + "="*30 + "\n" + "   LISTA DE CLIENTES")
            clientes = functions_clientes.listar_clientes()
            if not clientes:
                print("No hay clientes registrados.")
                print("="*30)
                continue
            print("\n---- listado de clientes ----")
            for cid, datos in clientes.items():
                print(f"ID: {cid} | Nombre: {datos['nombre']}")
            print("="*30)
            input("Presione Enter para continuar...")
            while True: # Esperar a que el usuario presione Enter para volver al menú
                print("    MENU")
                print("1. seleccionar cliente por ID")
                print("2. editar cliente por ID")
                print("3. eliminar cliente por ID")
                print("Presione Enter para volver al menú principal.")
                sub = input("digite la opcion:  ")
                if sub == '':
                    break
                if sub == '1': # Seleccionar cliente por ID
                    cid = input("Ingrese el ID del cliente: ")
                    ok, cliente, mensaje = functions_clientes.obtener_cliente(cid) 
                    if ok:
                        print(cliente)
                    else:
                        print(mensaje)
                elif sub == '2': # Editar cliente por ID
                    cid = input("Ingrese el ID del cliente a editar: ")
                    nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
                    ok, mensaje = functions_clientes.editar_cliente(cid, nuevo_nombre)
                    print(mensaje)
                elif sub == '3': # Eliminar cliente por ID
                    cid = input("Ingrese el ID del cliente a eliminar: ")
                    ok, _, mensaje = functions_clientes.eliminar_cliente(cid)
                    print(mensaje)
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion == '3': # Salir del programa 
            print("Saliendo del programa. ¡Hasta luego!")
            break