"""
Módulo de Estadísticas
Funciones para calcular estadísticas sobre países
"""


def obtener_pais_mayor_poblacion(paises):
    """
    Obtiene el país con mayor población.

    Args:
        paises: Lista de diccionarios con países

    Returns:
        dict: País con mayor población, None si lista vacía
    """
    if not paises:
        return None

    pais_mayor = paises[0]
    for pais in paises:
        if pais['poblacion'] > pais_mayor['poblacion']:
            pais_mayor = pais

    return pais_mayor


def obtener_pais_menor_poblacion(paises):
    """
    Obtiene el país con menor población.

    Args:
        paises: Lista de diccionarios con países

    Returns:
        dict: País con menor población, None si lista vacía
    """
    if not paises:
        return None

    pais_menor = paises[0]
    for pais in paises:
        if pais['poblacion'] < pais_menor['poblacion']:
            pais_menor = pais

    return pais_menor


def calcular_promedio_poblacion(paises):
    """
    Calcula el promedio de población.

    Args:
        paises: Lista de diccionarios con países

    Returns:
        float: Promedio de población (0 si lista vacía)
    """
    if not paises:
        return 0
    total = sum(p['poblacion'] for p in paises)
    return total / len(paises)


def calcular_promedio_superficie(paises):
    """
    Calcula el promedio de superficie.

    Args:
        paises: Lista de diccionarios con países

    Returns:
        float: Promedio de superficie en km² (0 si lista vacía)
    """
    if not paises:
        return 0
    total = sum(p['superficie'] for p in paises)
    return total / len(paises)


def contar_paises_por_continente(paises):
    """
    Cuenta cuántos países hay en cada continente.

    Args:
        paises: Lista de diccionarios con países

    Returns:
        dict: Diccionario con continentes como claves y cantidad como valores
    """
    conteos = {}
    for pais in paises:
        continente = pais['continente']
        if continente in conteos:
            conteos[continente] += 1
        else:
            conteos[continente] = 1

    # Ordenar por continente
    return dict(sorted(conteos.items()))


def obtener_pais_mayor_superficie(paises):
    """
    Obtiene el país con mayor superficie.

    Args:
        paises: Lista de diccionarios con países

    Returns:
        dict: País con mayor superficie, None si lista vacía
    """
    if not paises:
        return None

    pais_mayor = paises[0]
    for pais in paises:
        if pais['superficie'] > pais_mayor['superficie']:
            pais_mayor = pais

    return pais_mayor


def obtener_pais_menor_superficie(paises):
    """
    Obtiene el país con menor superficie.

    Args:
        paises: Lista de diccionarios con países

    Returns:
        dict: País con menor superficie, None si lista vacía
    """
    if not paises:
        return None

    pais_menor = paises[0]
    for pais in paises:
        if pais['superficie'] < pais_menor['superficie']:
            pais_menor = pais

    return pais_menor
