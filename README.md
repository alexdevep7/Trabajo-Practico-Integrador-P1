📊 Trabajo Práctico Integrador - Programación 1
🎓 Universidad Tecnológica Nacional
Tecnicatura Universitaria en Programación a Distancia (TUPAD)

👥 ✨ Estudiantes de la Comisión Ag25-1C-03

👤Nombre: Castillo Belisario, Alfredo
👤Nombre: Chiuán Castilla, Cesia

👨‍🏫 Docentes

👤Coordinador: Alberto Cortez
👤Profesor: Brian Lara

---

📋 Descripción del Repositorio
Este repositorio almacena el Trabajo Práctico Integrador de la materia 👨‍💻Programación 1👨‍💻.
El proyecto consiste en un Sistema de Gestión de Datos de Países desarrollado en Python, que permite realizar operaciones de almacenamiento, consulta, filtrado, ordenamiento y análisis estadístico sobre un catálogo de países almacenado en formato CSV.
🌍 Funcionalidades Principales:
Gestión de Datos (CRUD):

✅ Agregar nuevos países al catálogo
✅ Actualizar población y superficie de países existentes
✅ Consultar información de países específicos
✅ Visualizar el catálogo completo

Búsquedas:

🔍 Búsqueda exacta por nombre de país
🔍 Búsqueda parcial (contiene texto)

Filtros:

🌎 Filtrar países por continente
👥 Filtrar por rango de población
📏 Filtrar por rango de superficie

Ordenamiento:

📊 Ordenar por nombre (A-Z o Z-A)
📊 Ordenar por población (ascendente/descendente)
📊 Ordenar por superficie (ascendente/descendente)

Estadísticas:

📈 País con mayor/menor población
📈 País con mayor/menor superficie
📈 Promedios de población y superficie
📈 Distribución de países por continente

---

📌 ESTRUCTURA:📌

📦 Trabajo-Practico-Integrador-P1/
├── 📁 TP INTEGRADOR/
│ ├── 📄 tp_integrador.py # Archivo principal de ejecución
│ │
│ ├── 📁 modulos/ # Paquete de módulos del sistema
│ │ ├── 📄 **init**.py # Inicialización del paquete
│ │ ├── 📄 datos.py # CRUD y persistencia CSV
│ │ ├── 📄 busquedas.py # Búsqueda exacta y parcial
│ │ ├── 📄 estadisticas.py # Cálculos estadísticos
│ │ ├── 📄 filtros.py # Filtros por criterios
│ │ ├── 📄 ordenamiento.py # Ordenamiento de países
│ │ ├── 📄 utilidades.py # Formateo y presentación
│ │ └── 📄 validaciones.py # Validación de datos
│ │
│ └── 📁 datos/
│ └── 📄 paises.csv # Base de datos de países
│
└── 📄 README.md # Este archivo

---

📚 DESCRIPCION DE LOS MODULOS:
tp_integrador.py - Archivo principal

Punto de entrada de la aplicación
Menú interactivo con 8 opciones
Coordinación de todos los módulos

modulos/datos.py - Gestión de datos

Carga y guarda datos desde/hacia CSV
Operaciones CRUD (Create, Read, Update)
Validación de duplicados y permisos de archivos

modulos/busquedas.py - Búsquedas

Búsqueda exacta por nombre (case-insensitive)
Búsqueda parcial por texto contenido

modulos/estadisticas.py - Estadísticas

Cálculo de máximos y mínimos
Promedios poblacionales y de superficie
Conteo por continente

modulos/filtros.py - Filtros

Filtrado por continente
Filtrado por rangos de población
Filtrado por rangos de superficie

modulos/ordenamiento.py - Ordenamiento

Ordenamiento por nombre (alfabético)
Ordenamiento por población
Ordenamiento por superficie
Orden ascendente y descendente

modulos/utilidades.py - Presentación

Formato de tablas con box-drawing
Visualización individual de países
Separadores de miles en números
Limpieza de pantalla multiplataforma

modulos/validaciones.py - Validaciones

Validación de números positivos
Validación de textos no vacíos
Validación de rangos lógicos
Mensajes de error descriptivos

🎨 Características de la estructura:

✅ Arquitectura modular con separación de responsabilidades
✅ Cada módulo tiene una función específica y bien definida
✅ Código limpio, ordenado y bien documentado con docstrings
✅ Validaciones robustas sin uso de excepciones
✅ Persistencia automática en CSV tras modificaciones

---

🚀 Instrucciones de Ejecución
Requisitos Previos

Python 3.6 o superior
No se requieren librerías de terceros (solo módulos estándar de Python)

Verificar Versión de Python
Windows:
bashpython --version
Mac/Linux:
bashpython3 --version
Debe mostrar Python 3.6 o superior.

Navegar por el Menú:
El programa mostrará un menú interactivo con las siguientes opciones:

1.  Agregar un pais
2.  Actualizar datos de un pais
3.  Buscar un pais por nombre
4.  Filtrar paises
5.  Ordenar paises
6.  Ver estadisticas
7.  Ver todos los paises
8.  Salir

---

Seleccione una opcion (1-8):

Ingresa el número de la opción deseada y presiona Enter.

---

📚 Uso de Librerías de Terceros:
El proyecto utiliza únicamente módulos estándar de Python, no requiere instalación de librerías de terceros mediante pip.
Módulos estándar utilizados:

csv - Para lectura y escritura de archivos CSV
os - Para operaciones del sistema de archivos (rutas, permisos)
sys - Para gestión de salida del programa

No se requiere ejecutar pip install para ninguna librería.

---

Enlaces:
📹 Video Demostrativo
Link del video: [Pendiente de subir]

El video incluye una demostración completa del sistema, mostrando todas las funcionalidades: agregar países, búsquedas, filtros, ordenamiento y estadísticas.

📄 Documentación en PDF
Link del documento PDF: [Pendiente de subir]

El documento PDF contiene la documentación técnica completa del proyecto, diagramas de arquitectura y explicación detallada de cada módulo.

---

💡 Ejemplos de Entrada y Salida
Ejemplo 1: Agregar un País
Entrada:

Seleccione una opcion (1-8): 1

--- AGREGAR PAIS ---
Nombre del pais: Argentina
Poblacion: 45195774
Superficie (km2): 2780400
Continente: America

Salida:

Pais 'Argentina' agregado exitosamente
Se guardaron 1 paises correctamente

Presiona Enter para continuar...

Ejemplo 5: Ver Estadísticas
Entrada:

Seleccione una opcion (1-8): 6

Salida:

--- POBLACION ---
Pais con mayor poblacion : China (1,439,323,776)
Pais con menor poblacion : Vaticano (825)
Promedio de poblacion : 67,890,123 habitantes

--- SUPERFICIE ---
Pais con mayor superficie : Rusia (17,098,242)
Pais con menor superficie : Vaticano (0)
Promedio de superficie : 1,234,567 km2

--- DISTRIBUCION POR CONTINENTE ---
Africa : 54 paises
America : 35 paises
Asia : 48 paises
Europa : 44 paises
Oceania : 14 paises

Presiona Enter para continuar...

Ejemplo 3: Manejo de Errores - Validación
Entrada:

Seleccione una opcion (1-8): 1

--- AGREGAR PAIS ---
Nombre del pais:

Salida:

X Error: Nombre no puede estar vacio

Presiona Enter para continuar...

---

👨‍💻 Autores
Estudiantes de la Tecnicatura Universitaria en Programación a Distancia
Universidad Tecnológica Nacional (UTN)
Comisión: Ag25-1C-03
Año: 2025
