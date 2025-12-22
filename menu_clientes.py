import clientes

print("\n menu \n")
print("1. Agregar cliente")
print("2. Listado de clientes")
print("3. Salir")

while True: # Bucle principal del programaopcion = input("Seleccione una opcion: ")
    opcion = input("Seleccione una opcion: ")

    if opcion == '1': # Agregar cliente
        while True: # Bucle para agregar clientes
            print("\nIngrese 'salir' para volver al menú principal.")
            nombre = input("Ingrese el nombre del cliente: ")
            if nombre.lower().strip() == 'salir': # Salir al menú principal
                print("Volviendo al menú principal.")
                break
            elif not nombre.strip(): # Validar que el nombre no esté vacío
                print("El nombre no puede estar vacío. Intente de nuevo.")
            elif nombre[0].isdigit() : # Validar que el nombre no comience con un número
                print("El nombre no puede comenzar con un número. Intente de nuevo.")
            elif not nombre.replace(" ", "").isalnum(): # Validar que el nombre solo contenga caracteres alfanuméricos y espacios
                print("El nombre solo puede contener letras, números y espacios. Intente de nuevo.")
            elif len(nombre.strip()) < 2: # Validar que el nombre tenga al menos 2 caracteres
                print("El nombre debe tener al menos 2 caracteres. Intente de nuevo.")
            elif buscar_clientes_por_nombre := clientes.buscar_clientes_por_nombre(nombre): # Verificar si el cliente ya existe
                print("Ya existe un cliente con ese nombre:")
                for id, datos in buscar_clientes_por_nombre.items():
                    print(f"ID: {id}, Nombre: {datos['nombre']}")
            else: # Agregar cliente válido
                id_cliente = clientes.agregar_cliente(nombre)
                print(f"Cliente agregado con ID: {id_cliente}")

    elif opcion == '2': # Listar clientes
        print("\n" + "="*30 + "\n" + "   LISTA DE CLIENTES")
        todos_clientes = clientes.listar_clientes()
        if todos_clientes: # Verifica si hay clientes para mostrar
            for id, datos in todos_clientes.items():
                print(f"ID: {id}, Nombre: {datos['nombre']}")
        else: # No hay clientes registrados
            print("No hay clientes registrados.")
        print("="*30)
        while True: # Esperar a que el usuario presione Enter para volver al menú
            print("    MENU")
            print("1. seleccionar cliente por ID \n2. borrar cliente por ID \n3. editar cliente por ID \n\nPresione Enter para volver al menú principal.\n\n")
            entrada = input("digite la opcion:  ")
            if entrada == '':
                break
            elif entrada == '1': # Seleccionar cliente por ID
                id_seleccionar = input("Ingrese el ID del cliente a seleccionar: ")
                cliente = clientes.obtener_cliente(id_seleccionar)
                if cliente: # Cliente encontrado
                    print(f"Cliente seleccionado: ID: {id_seleccionar}, Nombre: {cliente['nombre']}")
                else:
                    print("No se encontró un cliente con ese ID.")
            elif entrada == '2': # Borrar cliente por ID
                id_borrar = input("Ingrese el ID del cliente a borrar: ")
                if clientes.eliminar_cliente(id_borrar):
                    print("Cliente eliminado exitosamente.")
                else:
                    print("No se encontró un cliente con ese ID.")
            elif entrada == '3': # Editar cliente por ID
                id_editar = input("Ingrese el ID del cliente a editar: ")
                cliente = clientes.obtener_cliente(id_editar)
                if cliente:
                    nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
                    if clientes.editar_cliente(id_editar, nuevo_nombre):
                        print("Cliente editado exitosamente.")
                    else:
                        print("No se encontró un cliente con ese ID.")
                else:
                    print("No se encontró un cliente con ese ID.")
    elif opcion == '3': # Salir del programa 
        print("Saliendo del programa. ¡Hasta luego!")
        break