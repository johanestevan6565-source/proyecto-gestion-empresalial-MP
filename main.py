# main.py
from Modules.menu_clientes import menu_clientes
from Modules.menu_productos import menu_productos

def main():
    while True:
        print("\n=== SISTEMA DE GESTIÓN EMPRESARIAL ===")
        print("1. Gestión de clientes")
        print("2. Gestión de productos")
        print("3. Registro ventas por cliente (próximamente)")
        print("4. Gestión de ventas (próximamente)")
        print("5. Gestión de inventarios (próximamente)")
        print("6. Gestion de Proveedores (próximamente)")
        print("7. Gestión de informes (próximamente)")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()

        elif opcion == "2":
            menu_productos() # Llama a la función del menú de productos

        elif opcion == "3":
            print("Funcionalidad para registro de ventas por cliente próximamente.")

        elif opcion == "4":
            print("Funcionalidad para gestión de ventas próximamente.")

        elif opcion == "5":
            print("Funcionalidad para gestión de inventarios próximamente.")

        elif opcion == "6":
            print("Funcionalidad para gestión de proveedores próximamente.")

        elif opcion == "7":
            print("Funcionalidad para gestión de informes próximamente.")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    main()