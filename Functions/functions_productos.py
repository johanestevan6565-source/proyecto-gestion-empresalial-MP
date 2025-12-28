import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'Data', 'productos', 'productos.json')


def cargar_productos():
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def guardar_productos(productos):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)


def generar_id(productos):
    return f"P{len(productos) + 1}"


def agregar_producto(nombre, precio):
    productos = cargar_productos()
    producto_id = generar_id(productos)

    productos[producto_id] = {
        "nombre": nombre.strip().title(),
        "precio": float(precio),
        "activo": True
    }

    guardar_productos(productos)
    return producto_id

def normalizar_texto(texto):
    return texto.strip().lower()


def listar_productos():
    productos = cargar_productos()
    for id, datos in productos.items():
        estado = "Activo" if datos['activo'] else "Inactivo"
        print(f"ID: {id}, Nombre: {datos['nombre']}, Precio: {datos['precio']}, Estado: {estado}")
    return cargar_productos()


def obtener_producto_flexible(entrada):
    productos = cargar_productos()
    entrada_normalizada = normalizar_texto(entrada)
    resultados = []
    for pid, datos in productos.items():
        nomre_normalizado = normalizar_texto(datos["nombre"])
        if entrada_normalizada == pid.lower() or entrada_normalizada == nomre_normalizado:
            resultados.append((pid, datos))
    return resultados if resultados else None

def editar_precio(producto_id, nuevo_precio):
    productos = cargar_productos()
    if producto_id in productos:
        productos[producto_id]["precio"] = float(nuevo_precio)
        guardar_productos(productos)
        return True
    return False

def editar_producto(producto_id, nuevo_nombre):
    productos = cargar_productos()
    if producto_id in productos:
        productos[producto_id]["nombre"] = nuevo_nombre.strip().title()
        guardar_productos(productos)
        return True
    return False

def eliminar_producto(producto_id):
    productos = cargar_productos()
    if producto_id in productos:
        productos[producto_id]["activo"] = False
        guardar_productos(productos)
        return True
    return False
