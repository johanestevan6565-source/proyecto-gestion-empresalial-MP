from Modules.config import PRODUCTOS_FILE
import json

def cargar_productos(): # Carga los productos desde el archivo JSON, creando el archivo si no existe con una estructura inicial
    try:
        with open(PRODUCTOS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        data_inicial = {"productos": []}
        with open(PRODUCTOS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data_inicial, f, indent=4, ensure_ascii=False)
        return data_inicial

def guardar_productos(data): # Guarda los productos en el archivo JSON, creando el archivo si no existe
    with open(PRODUCTOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def generar_id(data, nombre): # Genera un ID único para un nuevo producto basado en la primera letra del nombre y un número secuencial, asegurándose de no duplicar IDs existentes
    letra = nombre.strip()[0].upper()
    contador = 1
    ids_existentes = [
        p["id"] for p in data["productos"]
        if p["id"].startswith(letra)
    ]
    while True:
        nuevo_id = f"{letra}{contador:02}"
        if nuevo_id not in ids_existentes:
            return nuevo_id
        contador += 1

def validar_nombre(nombre): # Valida el nombre del producto, asegurándose de que no esté vacío, no exceda los 50 caracteres y solo contenga letras y espacios
    if not nombre or not nombre.strip():
        return False, "El nombre no puede estar vacío"
    if len(nombre.strip()) > 50:
        return False, "Máximo 50 caracteres"
    if not nombre.replace(" ", "").isalpha():
        return False, "Solo letras y espacios"
    return True, ""

def validar_precio(precio): # Valida el precio del producto, asegurándose de que sea un número válido y mayor a 0
    try:
        precio = float(precio)
    except ValueError:
        return False, "Precio inválido"
    if precio <= 0:
        return False, "El precio debe ser mayor a 0"
    return True, ""

def validar_tipo_venta(tipo): # Valida el tipo de venta del producto, asegurándose de que sea "unidad" o "kg"
    tipo = tipo.lower()
    if tipo not in ["unidad", "kg"]:
        return False, "Tipo inválido. Debe ser 'unidad' o 'kg'"
    return True, ""

def producto_existe(nombre, data, excluir_id=None): # Verifica si un producto con el mismo nombre ya existe, excluyendo un ID específico si se proporciona (útil para edición)
    for p in data["productos"]:
        if p["nombre"].lower() == nombre.lower():
            if excluir_id and p["id"] == excluir_id:
                continue
            return True
    return False

def agregar_producto(nombre, precio, tipo_venta): # Agrega un nuevo producto después de validar el nombre y el precio, y asegurándose de que no exista un producto con el mismo nombre
    data = cargar_productos()

    valido, mensaje = validar_nombre(nombre)
    if not valido:
        return False, mensaje
    valido, mensaje = validar_precio(precio)
    if not valido:
        return False, mensaje
    valido, mensaje = validar_tipo_venta(tipo_venta)
    if not valido:
        return False, mensaje
    if producto_existe(nombre, data):
        return False, "El producto ya existe"
    nuevo = {
        "id": generar_id(data, nombre),
        "nombre": nombre.strip().title(),
        "precio": round(float(precio), 2),
        "tipo_venta": tipo_venta.lower(),
        "activo": True
    }

    data["productos"].append(nuevo)
    guardar_productos(data)
    return True, "Producto agregado correctamente"

def editar_producto(producto_id, nombre=None, precio=None): # Edita un producto existente, permitiendo cambiar el nombre y/o el precio después de validar los nuevos valores y asegurándose de que el nuevo nombre no esté registrado por otro producto
    data = cargar_productos()
    for p in data["productos"]:
        if p["id"].lower() == producto_id.lower():
            if nombre is not None:
                valido, mensaje = validar_nombre(nombre)
                if not valido:
                    return False, mensaje
                if producto_existe(nombre, data, excluir_id=producto_id):
                    return False, "Nombre ya registrado"
                p["nombre"] = nombre.strip().title()
            if precio is not None:
                valido, mensaje = validar_precio(precio)
                if not valido:
                    return False, mensaje
                p["precio"] = round(float(precio), 2)
            guardar_productos(data)
            return True, "Producto actualizado"
    return False, "Producto no encontrado"

def cambiar_estado_producto(producto_id, activo): # Cambia el estado de un producto a activo o inactivo, buscando el producto por su ID y actualizando su estado
    data = cargar_productos()
    for p in data["productos"]:
        if p["id"] == producto_id:
            p["activo"] = activo
            guardar_productos(data)
            return True, "Estado actualizado"
    return False, "Producto no encontrado"


def listar_productos(activo=None): # Lista los productos, filtrando por estado activo o inactivo si se especifica, o mostrando todos si no se proporciona un filtro
    data = cargar_productos()
    resultados = []
    for p in data["productos"]:
        if activo is None or p["activo"] == activo:
            resultados.append(p)
    return resultados

def buscar_producto(entrada, activo=None): # Busca productos por ID o nombre, filtrando por estado activo o inactivo si se especifica, y devolviendo una lista de resultados que coincidan con la entrada
    data = cargar_productos()
    entrada = entrada.strip().lower()
    resultados = []
    for p in data["productos"]:
        if activo is not None and p["activo"] != activo:
            continue
        if entrada == p["id"].lower():
            return [p]
        if entrada == p["nombre"].lower():
            return [p]
        if entrada in p["nombre"].lower():
            resultados.append(p)
    return resultados if resultados else None

def editar_precio_producto(producto_id, nuevo_precio): # Edita el precio de un producto específico, validando el nuevo precio antes de actualizarlo
    data = cargar_productos()
    for p in data["productos"]:
        if p["id"].lower() == producto_id.lower():
            valido, mensaje = validar_precio(nuevo_precio)
            if not valido:
                return False, mensaje
            p["precio"] = round(float(nuevo_precio), 2)
            guardar_productos(data)
            return True, "Precio actualizado"
    return False, "Producto no encontrado"