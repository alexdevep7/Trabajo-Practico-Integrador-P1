# 📊 Trabajo Práctico Integrador – Programación 1

### 🎓 Universidad Tecnológica Nacional

**Tecnicatura Universitaria en Programación a Distancia (TUPAD)**

---

## 👥 Estudiantes – Comisión Ag25-1C-03

- **Castillo Belisario, Alfredo**
- **Chiuán Castilla, Cesia**

## 👨‍🏫 Docentes

- **Coordinador:** Alberto Cortez
- **Profesor:** Brian Lara

---

## 📋 Descripción del Repositorio

Este repositorio almacena el **Trabajo Práctico Integrador** de la materia **Programación 1**.  
El proyecto consiste en un **Sistema de Gestión de Datos de Países**, desarrollado en **Python**, que permite realizar operaciones de almacenamiento, consulta, filtrado, ordenamiento y análisis estadístico sobre un catálogo de países en formato **CSV**.

---

## 🌍 Funcionalidades Principales

### 🔧 Gestión de Datos (CRUD)

- ✅ Agregar nuevos países al catálogo
- ✅ Actualizar población y superficie
- ✅ Consultar información de países específicos
- ✅ Visualizar el catálogo completo

### 🔍 Búsquedas

- 🔹 Búsqueda exacta por nombre de país
- 🔹 Búsqueda parcial (por texto contenido)

### 🎯 Filtros

- 🌎 Filtrar países por continente
- 👥 Filtrar por rango de población
- 📏 Filtrar por rango de superficie

### 📊 Ordenamiento

- 🔸 Por nombre (A–Z / Z–A)
- 🔸 Por población (ascendente / descendente)
- 🔸 Por superficie (ascendente / descendente)

### 📈 Estadísticas

- País con mayor/menor población
- País con mayor/menor superficie
- Promedios de población y superficie
- Distribución de países por continente

---

## 📁 Estructura del Proyecto

```bash
📦 Trabajo-Practico-Integrador-P1/
├── 📁 TP INTEGRADOR/
│   ├── 📄 tp_integrador.py              # Archivo principal de ejecución
│   │
│   ├── 📁 modulos/                     # Paquete de módulos del sistema
│   │   ├── __init__.py                 # Inicialización del paquete
│   │   ├── datos.py                    # CRUD y persistencia CSV
│   │   ├── busquedas.py                # Búsqueda exacta y parcial
│   │   ├── estadisticas.py             # Cálculos estadísticos
│   │   ├── filtros.py                  # Filtros por criterios
│   │   ├── ordenamiento.py             # Ordenamiento de países
│   │   ├── utilidades.py               # Formateo y presentación
│   │   └── validaciones.py             # Validación de datos
│   │
│   └── 📁 datos/
│       └── paises.csv                  # Base de datos de países
│
└── 📄 README.md                        # Este archivo


🧩 Descripción de los Módulos

| Módulo               | Descripción                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------- |
| **tp_integrador.py** | Punto de entrada de la aplicación. Menú interactivo con 8 opciones. Coordina todos los módulos. |
| **datos.py**         | CRUD sobre CSV. Carga, guarda y valida duplicados.                                              |
| **busquedas.py**     | Búsqueda exacta y parcial por nombre (case-insensitive).                                        |
| **estadisticas.py**  | Cálculos de máximos, mínimos, promedios y conteo por continente.                                |
| **filtros.py**       | Filtra por continente, rango de población o superficie.                                         |
| **ordenamiento.py**  | Ordena por nombre, población o superficie (asc/desc).                                           |
| **utilidades.py**    | Formato de tablas, visualización de países, limpieza de pantalla.                               |
| **validaciones.py**  | Validación de entradas numéricas y textuales con mensajes descriptivos.                         |



🎨 Características Técnicas

✅ Arquitectura modular y separada por responsabilidades

✅ Código limpio y documentado con docstrings

✅ Validaciones robustas sin uso de excepciones

✅ Persistencia automática en CSV tras modificaciones

✅ Totalmente funcional con módulos estándar de Python


🚀 Instrucciones de Ejecución
🧠 Requisitos Previos

Python 3.6 o superior

No se requieren librerías externas

🔍 Verificar versión de Python

# Windows
python --version

# Mac/Linux
python3 --version

Debe mostrar Python 3.6 o superior.


▶️ Ejecución del Programa

Al ejecutar el programa, se mostrará un menú interactivo:

============================================================
GESTIÓN DE DATOS DE PAÍSES
============================================================
1.  Agregar un país
2.  Actualizar datos de un país
3.  Buscar un país por nombre
4.  Filtrar países
5.  Ordenar países
6.  Ver estadísticas
7.  Ver todos los países
8.  Salir

Selecciona una opción (1–8) y presiona Enter.

📦 Dependencias

Este proyecto no utiliza librerías externas.
Se emplean únicamente módulos estándar de Python:

csv → lectura y escritura de archivos

os → manejo de rutas y permisos

sys → salida y finalización del programa

No se requiere ejecutar pip install.


🔗 Enlaces

📹 Video Demostrativo: [Pendiente de subir]
📄 Documentación en PDF: [Pendiente de subir]

El video mostrará el flujo completo del sistema (agregar países, búsquedas, filtros, ordenamientos y estadísticas).
El documento PDF incluirá la documentación técnica y los diagramas de arquitectura.


💡 Ejemplos de Ejecución
🧩 Ejemplo 1 – Agregar un País

Entrada:

Seleccione una opción (1–8): 1
--- AGREGAR PAÍS ---
Nombre del país: Argentina
Población: 45195774
Superficie (km²): 2780400
Continente: América

Salida:

País 'Argentina' agregado exitosamente
Se guardaron 1 país(es) correctamente


📊 Ejemplo 2 – Ver Estadísticas

Entrada:

Seleccione una opción (1–8): 6

Salida:

============================================================
ESTADÍSTICAS
============================================================

--- POBLACIÓN ---
País con mayor población : China (1,439,323,776)
País con menor población : Vaticano (825)
Promedio de población : 67,890,123 habitantes

--- SUPERFICIE ---
País con mayor superficie : Rusia (17,098,242)
País con menor superficie : Vaticano (0)
Promedio de superficie : 1,234,567 km²

--- DISTRIBUCIÓN POR CONTINENTE ---
África : 54 países
América : 35 países
Asia : 48 países
Europa : 44 países
Oceanía : 14 países


⚠️ Ejemplo 3 – Manejo de Errores

Entrada:

Seleccione una opción (1–8): 1
--- AGREGAR PAÍS ---
Nombre del país:

Salida:

❌ Error: El nombre no puede estar vacío


🧠 Créditos

Proyecto desarrollado por:
Castillo Belisario, Alfredo & Chiuán Castilla, Cesia
📚 Universidad Tecnológica Nacional – TUPAD



```
