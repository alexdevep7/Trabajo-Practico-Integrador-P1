"""
Módulo de Datos
Gestión de lectura, almacenamiento y manipulación de datos de países
"""

import csv
import os
from modulos.validaciones import validar_numero_positivo


paises = []
ruta_csv = ""


def inicializar(ruta):
    """
    Inicializa el módulo con la ruta del CSV y carga los datos.

    Args:
        ruta: Ruta al archivo CSV de países
    """
    global ruta_csv, paises
    ruta_csv = ruta
    paises = []
    cargar_datos()


def cargar_datos():
    """
    Carga datos desde el archivo CSV.
    """
    global paises, ruta_csv

    if not os.path.exists(ruta_csv):
        print(f"X Error: Archivo '{ruta_csv}' no encontrado")
        return False

    if not os.access(ruta_csv, os.R_OK):
        print(f"X Error: No hay permisos para leer '{ruta_csv}'")
        return False

    archivo = open(ruta_csv, 'r', encoding='utf-8')
    lector = csv.DictReader(archivo)

    if lector.fieldnames != ['nombre', 'poblacion', 'superficie', 'continente']:
        print("X Error: Formato de CSV invalido. Columnas esperadas: nombre, poblacion, superficie, continente")
        archivo.close()
        return False

    for fila in lector:
        nombre = fila.get('nombre')
        poblacion = fila.get('poblacion')
        superficie = fila.get('superficie')
        continente = fila.get('continente')

        if nombre and poblacion and superficie and continente:
            if poblacion.isdigit() and superficie.isdigit():
                pais = {
                    'nombre': nombre,
                    'poblacion': int(poblacion),
                    'superficie': int(superficie),
                    'continente': continente
                }
                paises.append(pais)
            else:
                print(f"Advertencia: Fila con poblacion o superficie invalida ignorada - {nombre}")
        else:
            print(f"Advertencia: Fila con campos vacios ignorada")

    archivo.close()
    print(f"Se cargaron {len(paises)} paises correctamente")
    return True


def guardar_datos():
    """
    Guarda los datos actuales en el archivo CSV.
    """
    global paises, ruta_csv

    if not os.access(os.path.dirname(ruta_csv) or '.', os.W_OK):
        print(f"X Error: No hay permisos para escribir en el directorio")
        return False

    archivo = open(ruta_csv, 'w', newline='', encoding='utf-8')
    escritor = csv.DictWriter(
        archivo,
        fieldnames=['nombre', 'poblacion', 'superficie', 'continente']
    )
    escritor.writeheader()
    escritor.writerows(paises)
    archivo.close()

    print(f"Se guardaron {len(paises)} paises correctamente")
    return True


def agregar_pais(nombre, poblacion, superficie, continente):
    """
    Agrega un nuevo país a la lista.

    Args:
        nombre: Nombre del país
        poblacion: Población
        superficie: Superficie en km²
        continente: Continente

    Returns:
        bool: True si se agregó exitosamente, False si ya existe
    """
    global paises

    pais_nuevo = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }

    # Verificar que el país no exista ya
    existe = False
    for p in paises:
        if p['nombre'].lower() == pais_nuevo['nombre'].lower():
            existe = True
            break

    if existe:
        print(f"El pais '{pais_nuevo['nombre']}' ya existe en la base de datos")
        return False

    paises.append(pais_nuevo)
    guardar_datos()
    print(f"Pais '{pais_nuevo['nombre']}' agregado exitosamente")
    return True


def actualizar_pais(nombre, poblacion=None, superficie=None):
    """
    Actualiza población y/o superficie de un país.

    Args:
        nombre: Nombre del país a actualizar
        poblacion: Nueva población (opcional)
        superficie: Nueva superficie (opcional)

    Returns:
        bool: True si se actualizó, False si el país no existe
    """
    global paises

    for pais in paises:
        if pais['nombre'].lower() == nombre.lower():
            cambios = []

            if poblacion is not None:
                poblacion_str = str(poblacion)
                poblacion_valid, poblacion_result = validar_numero_positivo(poblacion_str, "Población")
                if not poblacion_valid:
                    print(f"✗ {poblacion_result}")
                    return False
                pais['poblacion'] = poblacion_result
                cambios.append(f"Poblacion: {poblacion_result:,}")

            if superficie is not None:
                superficie_str = str(superficie)
                superficie_valid, superficie_result = validar_numero_positivo(superficie_str, "Superficie")
                if not superficie_valid:
                    print(f"✗ {superficie_result}")
                    return False
                pais['superficie'] = superficie_result
                cambios.append(f"Superficie: {superficie_result:,} km2")

            if cambios:
                guardar_datos()
                print(f"✓ '{pais['nombre']}' actualizado: {', '.join(cambios)}")
                return True

    print(f"✗ Pais '{nombre}' no encontrado")
    return False


def obtener_pais(nombre):
    """
    Obtiene un país por nombre (búsqueda exacta).

    Args:
        nombre: Nombre del país

    Returns:
        dict: Datos del país o None si no existe
    """
    global paises

    for pais in paises:
        if pais['nombre'].lower() == nombre.lower():
            return pais
    return None


def obtener_todos():
    """
    Retorna lista de todos los países.

    Returns:
        list: Lista de diccionarios con datos de países
    """
    global paises
    return paises.copy()


def cantidad_paises():
    """
    Retorna la cantidad total de países.

    Returns:
        int: Cantidad de países
    """
    global paises
    return len(paises)
