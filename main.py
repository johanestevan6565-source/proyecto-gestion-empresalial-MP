# main.py
from Debug.menu_clientes import menu_clientes
from Debug.menu_inventarios import menu_test_inventarios
from Debug.menu_productos import menu_productos
from Debug.menu_proveedores import menu_proveedores
def main():
    while True:
        print("\n=== SISTEMA DE GESTIÓN EMPRESARIAL ===")
        print("1. Gestión de clientes")
        print("2. Gestión de productos")
        print("3. Gestión de ventas (próximamente)")
        print("4. Gestión de inventarios (próximamente)")
        print("5. Gestion de Proveedores (próximamente)")
        print("6. Gestión de informes (próximamente)")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()

        elif opcion == "2":
            menu_productos() # Llama a la función del menú de productos

        elif opcion == "3":
            print("Funcionalidad para registro de ventas por cliente próximamente.")
            

        elif opcion == "4":
            menu_test_inventarios() # Llama a la función del menú de inventarios   

        elif opcion == "5":
            menu_proveedores() # Llama a la función del menú de proveedores

        elif opcion == "6":
            print("Funcionalidad para gestión de informes próximamente.")
        elif opcion == "7":
            print("Funcionalidad para gestión de informes próximamente.")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    main()

