"""
Módulo de Filtros
Funciones para filtrar países por diferentes criterios
"""

from modulos.validaciones import validar_rango_poblacion, validar_rango_superficie


def filtrar_por_continente(paises, continente):
    """
    Filtra países por continente.

    Args:
        paises: Lista de diccionarios con países
        continente: Nombre del continente a filtrar

    Returns:
        list: Países que pertenecen al continente especificado
    """
    continente_lower = continente.lower()
    return [
        pais for pais in paises
        if pais['continente'].lower() == continente_lower
    ]


def filtrar_por_rango_poblacion(paises, min_poblacion, max_poblacion):
    """
    Filtra países por rango de población.

    Args:
        paises: Lista de diccionarios con países
        min_poblacion: Población mínima (inclusive)
        max_poblacion: Población máxima (inclusive)

    Returns:
        tuple: (bool, list or str) - (is_valid, countries_list or error_message)
    """
    valid, result = validar_rango_poblacion(min_poblacion, max_poblacion)
    if not valid:
        return False, result

    min_val, max_val = result

    paises_filtrados = []
    for pais in paises:
        if min_val <= pais['poblacion'] <= max_val:
            paises_filtrados.append(pais)

    return True, paises_filtrados


def filtrar_por_rango_superficie(paises, min_superficie, max_superficie):
    """
    Filtra países por rango de superficie.

    Args:
        paises: Lista de diccionarios con países
        min_superficie: Superficie mínima en km² (inclusive)
        max_superficie: Superficie máxima en km² (inclusive)

    Returns:
        tuple: (bool, list or str) - (is_valid, countries_list or error_message)
    """
    valid, result = validar_rango_superficie(min_superficie, max_superficie)
    if not valid:
        return False, result

    min_val, max_val = result

    paises_filtrados = []
    for pais in paises:
        if min_val <= pais['superficie'] <= max_val:
            paises_filtrados.append(pais)

    return True, paises_filtrados


def obtener_continentes(paises):
    """
    Obtiene lista de continentes únicos en el dataset.

    Args:
        paises: Lista de diccionarios con países

    Returns:
        list: Lista de continentes únicos, ordenados alfabéticamente
    """
    continentes = set()
    for pais in paises:
        continentes.add(pais['continente'])
    return sorted(list(continentes))
