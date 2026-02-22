# Sistema de Gestión Empresarial

## 📌 Descripción

Sistema integral de gestión empresarial desarrollado en Python, diseñado para
administrar de forma organizada y persistente la información clave de una empresa.

El sistema permite gestionar clientes, inventarios, movimientos financieros
(ingresos, egresos, abonos y saldos), con capacidad de análisis, exportación
de datos y visualización gráfica del estado general del negocio.

El proyecto está diseñado con una arquitectura modular y escalable, permitiendo
su crecimiento progresivo hacia interfaces gráficas, aplicaciones web/móviles
y automatización mediante chatbots.

---

## 🎯 Objetivo del proyecto

Crear una aplicación funcional, confiable y extensible que facilite:

- La organización de clientes y sus operaciones
- El control de inventarios por cliente y por día
- El seguimiento financiero del negocio
- La generación de reportes claros y exportables
- El análisis del estado general de la empresa

---

## ⚙️ Funcionalidades actuales

- Gestión de clientes:
  - Agregar clientes
  - Listar clientes
  - Buscar clientes por nombre
  - Editar clientes
  - Eliminar clientes
- Persistencia de datos mediante archivos JSON
- Arquitectura modular (separación de lógica, datos y menú)
- Control de versiones con Git y GitHub

---

## 🧩 Funcionalidades planificadas (Roadmap)

- Gestión de inventarios:
  - Inventarios por cliente
  - Inventarios por fecha
  - Control de productos y empaques
- Gestión financiera:
  - Ingresos y egresos
  - Abonos y saldos pendientes
  - Cartera de clientes
- Reportes:
  - Exportación a Excel
  - Exportación a PDF
- Análisis y visualización:
  - Gráficos de balance general
  - Gráficos de cartera y saldos
  - Análisis histórico de datos
- Interacción avanzada:
  - Integración con chatbot para consultas de datos
  - Versión web y/o móvil
- Persistencia avanzada:
  - Migración futura a base de datos (SQL)

---

## 🗂️ Estructura del proyecto

proyecto-gestion-empresarial/
│
├── main.py
├── menu/
│ └── menu_clientes.py
│
├── servicios/
│ └── clientes.py
│
├── data/
│ └── clientes.json
│
├── utils/
│ └── validaciones.py
│
├── README.md
└── .gitignore


---

## 🛠️ Tecnologías utilizadas

- Python 3
- JSON (persistencia de datos)
- Git / GitHub
- Programación modular

---

## 🚀 Estado del proyecto

🟡 En desarrollo activo  
El proyecto se encuentra en una fase inicial funcional, con enfoque en
una base sólida que permita un crecimiento ordenado y profesional.

---

## 📄 Licencia

Proyecto de uso educativo y personal.  
Licencia a definir en futuras versiones.