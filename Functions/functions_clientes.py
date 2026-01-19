import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # Directorio base del proyecto
datos_clientes = os.path.join (BASE_DIR, 'Data', 'clientes', 'clientes.json') # Ruta al archivo JSON de clientes

def cargar_clientes(): # Carga los clientes desde el archivo JSON
    if not os.path.exists(datos_clientes): # Si el archivo no existe, retorna un diccionario vacío
        return {}
    with open(datos_clientes, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def guardar_clientes(clientes): # Guarda los clientes en el archivo JSON
    with open(datos_clientes, 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

def normalizar_nombre(nombre): # Normaliza el nombre del cliente
    return ' '.join(palabra.capitalize() for palabra in nombre.split())

def generar_nuevo_id(clientes): # Genera un nuevo ID único para un cliente
    ids = [int(k) for k in clientes.keys() if k.isdigit()]
    return str(max(ids) + 1) if ids else '1'

def validar_nombre(nombre): # Valida el nombre del cliente
    if not nombre.strip():
        return False, "El nombre no puede estar vacío."
    if nombre[0].isdigit():
        return False, "El nombre no puede comenzar con un número."
    if not all (c.isalnum() or c.isspace() for c in nombre):
        return False, "El nombre solo puede contener letras, números y espacios."
    if len(nombre.strip()) < 2:
        return False, "El nombre debe tener al menos 2 caracteres."
    return True, ""

def agregar_cliente(nombre): # Agrega un nuevo cliente
    clientes = cargar_clientes()
    nombre = normalizar_nombre(nombre)
    valido, mensaje = validar_nombre(nombre)
    if not valido:
        return False, None, mensaje
    for datos in clientes.values():
        if datos['nombre'].lower() == nombre.lower():
            return False, None, "Ya existe un cliente con ese nombre."
    nuevo_id = generar_nuevo_id(clientes)
    clientes[nuevo_id] = {"nombre": nombre}
    guardar_clientes(clientes)
    return True, nuevo_id, "Cliente agregado exitosamente."

def obtener_cliente(cliente_ID): # Obtiene un cliente por su ID
    cliente_ID = str(cliente_ID).strip()
    clientes = cargar_clientes()
    if cliente_ID not in clientes:
        return False, None, "No se encontró un cliente con ese ID."
    return True, clientes.get(cliente_ID), "Cliente encontrado."

def listar_clientes(): # Lista todos los clientes
    return cargar_clientes()

def eliminar_cliente(cliente_ID): # Elimina un cliente por su ID
    clientes = cargar_clientes()
    cliente_ID = str(cliente_ID).strip()
    if cliente_ID not in clientes:
        return False, None, "No se encontró un cliente con ese ID."
    eliminado = clientes[cliente_ID]["nombre"]
    del clientes[cliente_ID]
    guardar_clientes(clientes)
    return True

def editar_cliente(cliente_ID, nuevo_nombre): # Actualiza el nombre de un cliente por su ID
    clientes = cargar_clientes()
    cliente_ID = str(cliente_ID).strip()
    if cliente_ID not in clientes:
        return False, "No se encontró un cliente con ese ID."
    nuevo_nombre = normalizar_nombre(nuevo_nombre)
    valido, mensaje = validar_nombre(nuevo_nombre)
    if not valido:
        return False, mensaje
    clientes[cliente_ID]["nombre"] = nuevo_nombre
    guardar_clientes(clientes)
    return True, "Cliente actualizado exitosamente."
