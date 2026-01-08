import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'Data', 'productos', 'productos.json')


def cargar_productos(): #funcion de cargar productos
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def guardar_productos(productos): #funcion de guardar productos
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)


def pedir_nombre_producto(): #funcion de pedir nombre del producto
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre.lower() == 'salir':
        return None
    if not nombre:
        print("El nombre no puede estar vacío.")
        return pedir_nombre_producto()
    if len(nombre) > 50:
        print("Máximo 50 caracteres.")
        return pedir_nombre_producto()
    if not nombre.replace(" ", "").isalpha():
        print("Solo letras y espacios.")
        return pedir_nombre_producto()
    if any(datos['nombre'].lower() == nombre.lower() for datos in cargar_productos().values()): 
        print("El producto ya existe.")
        return pedir_nombre_producto()
    return nombre


def pedir_precio_producto(): #funcion de pedir precio del producto
    precio = input("Ingrese el precio del producto: ").strip()
    if precio.lower() == 'salir':
        return None
    try:
        precio = float(precio)
    except ValueError:
        print("Precio inválido.")
        return pedir_precio_producto()
    if precio <= 0:
        print("El precio debe ser mayor que 0.")
        return pedir_precio_producto()
    if precio >= 10**8:
        print("El precio es demasiado grande.")
        return pedir_precio_producto()
    return round(precio, 2)


def generar_id(productos): #funcion de asignacion de ID por producto
    return f"P{len(productos) + 1}"


def agregar_producto(nombre, precio): #funcion de agregar producto
    productos = cargar_productos()
    producto_id = generar_id(productos)

    productos[producto_id] = {
        "nombre": nombre.strip().title(),
        "precio": float(precio),
        "activo": True
    }
    guardar_productos(productos)
    return producto_id


def normalizar_texto(texto): #funcion de normalizacion de texto
    return texto.strip().lower()


def listar_productos(activo=None):
    productos = cargar_productos()
    resultados = {}
    for pid, datos in productos.items():
        estado = datos.get("activo", True)
        if activo is None or estado == activo:
            resultados[pid] = datos
    if not resultados:
        print("No hay productos para mostrar.")
        return {}
    for pid, datos in resultados.items():
        estado_txt = "Activo" if datos.get("activo", True) else "Inactivo"
        print(f"{pid} - {datos['nombre']} - Precio: ${datos['precio']:.2f} - Estado: {estado_txt}")
    return resultados


def obtener_producto_flexible(entrada, activo=None): #funcion de obtener productos de forma flexible
    productos = cargar_productos()
    entrada_normalizada = normalizar_texto(entrada)
    resultados = []
    for pid, datos in productos.items():
        estado = datos.get("activo", True)
        if activo is not None and estado != activo:
            continue
        nomre_normalizado = normalizar_texto(datos["nombre"])
        if entrada_normalizada == pid.lower() or entrada_normalizada == nomre_normalizado:
            resultados.append((pid, datos))
        elif entrada_normalizada in nomre_normalizado:
            resultados.append((pid, datos))
    return resultados if resultados else None


def pedir_producto_a_editar(): #funcion de pedir producto a editar
    print("\nDigite 'salir' para volver al menú\n")
    while True:
        prodID = input("Ingrese el ID o nombre del producto a editar: ").strip()
        if prodID.lower() == 'salir':
            return None
        resultados = obtener_producto_flexible(prodID)
        if not resultados:
            print("No se encontró ningún producto.")
            continue
        if len(resultados) > 1:
            print("\nSe encontraron varios productos:\n")
            for pid, datos in resultados:
                print(f"{pid} - {datos['nombre']}")
            print("Sea más preciso.\n")
            continue
        pid, datos = resultados[0]
        print(f"\nProducto seleccionado: {pid} - {datos['nombre']}\n")
        return pid


def pedir_nuevo_nombre_producto(pid): #funcion de pedir nuevo nombre del producto
    while True:
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").strip()
        if nuevo_nombre.lower() == 'salir':
            return None
        if not nuevo_nombre:
            print("El nombre no puede estar vacío.")
            continue
        if len(nuevo_nombre) > 50:
            print("Máximo 50 caracteres.")
            continue
        if not nuevo_nombre.replace(" ", "").isalpha():
            print("Solo letras y espacios.")
            continue
        if any(datos['nombre'].lower() == nuevo_nombre.lower() and pid != pid_existente for pid_existente, datos in cargar_productos().items()):
            print("El producto ya existe.")
            continue
        return nuevo_nombre


def editar_precio(producto_id, nuevo_precio): #funcion de editar precios 
    productos = cargar_productos()
    if producto_id in productos:
        productos[producto_id]["precio"] = float(nuevo_precio)
        guardar_productos(productos)
        return True
    return False


def editar_producto(producto_id, nuevo_nombre): #funcion de editar producto
    productos = cargar_productos()
    if producto_id in productos:
        productos[producto_id]["nombre"] = nuevo_nombre.strip().title()
        guardar_productos(productos)
        return True
    return False


def eliminar_producto(producto_id): #funcion de elimnar producto
    productos = cargar_productos()
    if producto_id in productos:
        productos[producto_id]["activo"] = False
        guardar_productos(productos)
        return True
    return False


def pedir_producto_a_eliminar(): #funcion de pedir producto a eliminar
    print("\nDigite 'salir' para volver al menú\n")
    while True:
        entrada = input("Ingrese el ID o nombre del producto a eliminar: ").strip()
        if entrada.lower() == 'salir':
            return None
        resultados = obtener_producto_flexible(entrada, activo=True)
        if not resultados:
            print("No se encontró ningún producto.")
            continue
        if len(resultados) > 1:
            print("Se encontraron varios productos:")
            for pid, datos in resultados:
                print(f"{pid} - {datos['nombre']}")
            print("Sea más preciso.")
            continue
        pid, datos = resultados[0]
        confirmacion = input(
            f"¿Está seguro de que desea eliminar {pid} - {datos['nombre']}? (s/n): "
        ).strip().lower()
        if confirmacion == 's':
            return pid
        else:
            print("Eliminación cancelada.")
            return None
        

def reactivar_producto(producto_id): #funcion de reactivar producto
    productos = cargar_productos()
    if producto_id in productos and not productos[producto_id]["activo"]:
        productos[producto_id]["activo"] = True
        guardar_productos(productos)
        return True
    return False


def seleccionar_producto(activo=None): #funcion de seleccionar producto
    print("\nDigite 'salir' para volver\n")
    while True:
        entrada = input("Ingrese ID o nombre: ").strip()
        if entrada.lower() == 'salir':
            return None

        resultados = obtener_producto_flexible(entrada, activo)
        if not resultados:
            print("No se encontró producto.")
            continue
        if len(resultados) > 1:
            for pid, datos in resultados:
                print(f"{pid} - {datos['nombre']}")
            print("Sea más preciso.")
            continue

        return resultados[0]  # (pid, datos)
