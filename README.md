# Sistema de Gestión de Clientes

Proyecto desarrollado en Python para la gestión básica de clientes e inventarios mediante un menú en consola.
Permite agregar, listar, buscar, editar y eliminar datos, almacenando la información en archivos JSON.

---

## 📌 Características

- Agregar clientes con validaciones
- Agregar inventario de objetos con validaciones
- Listar clientes registrados
- Adjuntar clientes con sus respectivos inventarios
- Buscar clientes por nombre
- Editar clientes por ID
- Eliminar clientes por ID
- Persistencia de datos usando JSON
- Proyecto modular (separación de lógica y menú)

---

## 🛠️ Tecnologías utilizadas

- Python 3
- JSON
- Git

---

## 📂 Estructura del proyecto

```text
proyecto empresa/
│
├── menu_clientes.py      # Menú principal del programa
├── clientes.py           # Lógica de gestión de clientes
├── clientes.json         # Base de datos (JSON)
├── README.md             # Documentación del proyecto
└── .gitignore            # Archivos ignorados por Git
