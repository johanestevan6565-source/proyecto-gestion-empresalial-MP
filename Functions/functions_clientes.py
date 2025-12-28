import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # Directorio base del proyecto
datos_clientes = os.path.join (BASE_DIR, 'Data', 'clientes', 'clientes.json') # Ruta al archivo JSON de clientes
def cargar_clientes(): # Carga los clientes desde el archivo JSON
    try:
        with open(datos_clientes, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def guardar_clientes(clientes): # Guarda los clientes en el archivo JSON
    with open(datos_clientes, 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

def normalizar_nombre(nombre): # Normaliza el nombre del cliente
    return ' '.join(palabra.capitalize() for palabra in nombre.split())

def agregar_cliente(nombre): # Agrega un nuevo cliente
    clientes = cargar_clientes()
    nombre = normalizar_nombre(nombre)
    identificador_ID = str(len(clientes) + 1)
    clientes[identificador_ID] = {"nombre": nombre}
    guardar_clientes(clientes)
    return identificador_ID

def obtener_cliente(identificador_ID): # Obtiene un cliente por su ID
    clientes = cargar_clientes()
    return clientes.get(identificador_ID, None)

def listar_clientes(): # Lista todos los clientes
    return cargar_clientes()

def eliminar_cliente(identificador_ID): # Elimina un cliente por su ID
    clientes = cargar_clientes()
    if identificador_ID in clientes:
        del clientes[identificador_ID]
        guardar_clientes(clientes)
        return True
    return False

def editar_cliente(identificador_ID, nuevo_nombre): # Actualiza el nombre de un cliente por su ID
    clientes = cargar_clientes()
    if identificador_ID in clientes:
        clientes[identificador_ID]["nombre"] = nuevo_nombre
        guardar_clientes(clientes)
        return True
    return False

def buscar_clientes_por_nombre(nombre): # Busca clientes por nombre
    clientes = cargar_clientes()
    resultados = {}
    nombre_normalizado = nombre.strip().lower()
    for id, datos in clientes.items():
        if nombre_normalizado == datos['nombre'].lower():
            resultados[id] = datos
    return resultados