"""
Módulo de Ordenamiento
Funciones para ordenar países por diferentes criterios
"""


def extraer_nombre_lower(pais):
    """Extrae nombre en minúsculas para ordenar."""
    return pais['nombre'].lower()


def extraer_poblacion(pais):
    """Extrae población para ordenar."""
    return pais['poblacion']


def extraer_superficie(pais):
    """Extrae superficie para ordenar."""
    return pais['superficie']


def ordenar_por_nombre(paises, descendente=False):
    """
    Ordena países por nombre alfabéticamente.

    Args:
        paises: Lista de diccionarios con países
        descendente: Si True, orden descendente; si False, ascendente

    Returns:
        list: Lista de países ordenados
    """
    return sorted(
        paises,
        key=extraer_nombre_lower,
        reverse=descendente
    )


def ordenar_por_poblacion(paises, descendente=False):
    """
    Ordena países por población.

    Args:
        paises: Lista de diccionarios con países
        descendente: Si True, mayor a menor; si False, menor a mayor

    Returns:
        list: Lista de países ordenados
    """
    return sorted(
        paises,
        key=extraer_poblacion,
        reverse=descendente
    )


def ordenar_por_superficie(paises, descendente=False):
    """
    Ordena países por superficie en km².

    Args:
        paises: Lista de diccionarios con países
        descendente: Si True, mayor a menor; si False, menor a mayor

    Returns:
        list: Lista de países ordenados
    """
    return sorted(
        paises,
        key=extraer_superficie,
        reverse=descendente
    )
