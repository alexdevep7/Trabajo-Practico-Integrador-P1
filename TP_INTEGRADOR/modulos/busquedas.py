"""
Módulo de Búsquedas
Funciones para buscar países por nombre (exacta y parcial)
"""


def buscar_por_nombre_exacto(paises, nombre):
    """
    Busca un país por nombre exacto (case-insensitive).

    Args:
        paises: Lista de diccionarios con países
        nombre: Nombre del país a buscar

    Returns:
        dict: Datos del país si existe, None si no
    """
    for pais in paises:
        if pais['nombre'].lower() == nombre.lower():
            return pais
    return None


def buscar_por_nombre_parcial(paises, nombre):
    """
    Busca países cuyo nombre contiene el texto dado (case-insensitive).

    Args:
        paises: Lista de diccionarios con países
        nombre: Texto a buscar en los nombres

    Returns:
        list: Lista de países que coinciden (puede estar vacía)
    """
    nombre_lower = nombre.lower()
    resultados = [
        pais for pais in paises
        if nombre_lower in pais['nombre'].lower()
    ]
    return resultados


def buscar_pais(paises, nombre, busqueda_exacta=False):
    """
    Busca un país por nombre (wrapper general).

    Args:
        paises: Lista de diccionarios con países
        nombre: Nombre a buscar
        busqueda_exacta: Si True, búsqueda exacta; si False, parcial

    Returns:
        list: Lista de países encontrados (o lista con 1 elemento si exacta)
    """
    if busqueda_exacta:
        resultado = buscar_por_nombre_exacto(paises, nombre)
        return [resultado] if resultado else []
    else:
        return buscar_por_nombre_parcial(paises, nombre)
