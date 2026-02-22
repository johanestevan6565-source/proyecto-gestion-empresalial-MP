from Modules.config import INVENTARIOS_DIR
from Modules.Productos.Functions.functions_productos 
import os
from datetime import datetime
import json
import os


def nombre_archivo_mensual(fecha=None):
    if fecha is None:
        fecha = datetime.now()
    year = fecha.year
    month = f"{fecha.month:02d}"
    return f"{year}_{month}.json"

def ruta_archivo_inventario(fecha=None): # Obtiene la ruta completa al archivo de inventario mensual basado en la fecha proporcionada o la fecha actual si no se proporciona.
    nombre_archivo = nombre_archivo_mensual(fecha)
    return os.path.join(INVENTARIOS_DIR, nombre_archivo)

def obtener_archivo_mensual(fecha=None):
    ruta = ruta_archivo_inventario(fecha)
    if not os.path.exists(ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump({"eventos": []}, f, indent=4, ensure_ascii=False)
    return ruta

def registrar_evento_inventario(tipo, origen, data): # Registra un evento de inventario en el archivo mensual correspondiente, incluyendo la marca de tiempo, tipo de evento, origen y datos asociados.
    ruta_archivo = obtener_archivo_mensual()
    timestamp = datetime.now().isoformat("%Y-%m-%dT%H:%M:%S")
    evento = {
        "timestamp": timestamp,
        "tipo": tipo,
        "origen": origen,  
        "data": data
    }
    with open(ruta_archivo, 'r+', encoding='utf-8') as f:
        eventos = json.load(f)
        eventos["eventos"].append(evento)
        f.seek(0)
        json.dump(eventos, f, indent=4, ensure_ascii=False)

def registrar_compra_producto(proveedor_id, producto_id, cantidad, unidad, precio_unitario): # Registra una compra de producto en el inventario, calculando el total y registrando el evento correspondiente.
    total = cantidad * precio_unitario
    data_evento = {
        "proveedor_id": proveedor_id,
        "producto_id": producto_id,
        "cantidad": cantidad,
        "unidad": unidad,
        "precio_unitario": precio_unitario,
        "total": total
    }
    registrar_evento_inventario("compra", "registro_compra_producto", data_evento)

def registrar_ingreso_empaque_proveedor(marca, cantidadad, proveedor): # Registra el ingreso de empaque al inventario, incluyendo la marca, cantidad y proveedor, y registrando el evento correspondiente.
    data_evento = {
        "marca": marca,
        "cantidad": cantidadad,
        "proveedor": proveedor
    }
    registrar_evento_inventario (
        tipo="ingreso_empaque_proveedor",
        origen="registro_ingreso_empaque_proveedor",
        data=data_evento
    )

def registrar_ingreso_empaque_cliente(cliente_id, marca, cantidad): # Registra el ingreso de empaque por parte de un cliente, incluyendo el ID del cliente, marca y cantidad, y registrando el evento correspondiente.
    data_evento = {
        "cliente_id": cliente_id,
        "marca": marca,
        "cantidad": cantidad
    }
    registrar_evento_inventario(
        tipo="ingreso_empaque_cliente",
        origen="registro_ingreso_empaque_cliente",
        data=data_evento
    )

def registrar_devolucion_empaque_proveedor(marca, cantidad, proveedor): # Registra la devolución de empaque al proveedor, incluyendo la marca, cantidad y proveedor, y registrando el evento correspondiente.
    data_evento = {
        "marca": marca,
        "cantidad": cantidad,
        "proveedor": proveedor
    }
    registrar_evento_inventario(
        tipo="devolucion_empaque_proveedor",
        origen="registro_devolucion_empaque_proveedor",
        data=data_evento
    )

def registrar_devolucion_empaque_cliente(cliente_id, marca, cantidad): # Registra la devolución de empaque por parte de un cliente, incluyendo el ID del cliente, marca y cantidad, y registrando el evento correspondiente.
    data_evento = {
        "cliente_id": cliente_id,
        "marca": marca,
        "cantidad": cantidad
    }
    registrar_evento_inventario(
        tipo="devolucion_empaque_cliente",
        origen="registro_devolucion_empaque_cliente",
        data=data_evento
    )

def obtener_archivos_inventario():
    return [
        os.path.join(INVENTARIOS_DIR, f)
        for f in os.listdir(INVENTARIOS_DIR)
        if f.endswith(".json")
    ]

def calcular_stock_producto(producto_id):
    stock = 0
    for archivo in obtener_archivos_inventario():
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = json.load(f)
            for evento in contenido.get("eventos", []):
                data = evento.get("data", {})
                if data.get("producto_id") != producto_id:
                    continue
                if evento["tipo"] == "compra":
                    stock += data["cantidad"]
                elif evento["tipo"] == "venta":
                    stock -= data["cantidad"]
    return stock
                    