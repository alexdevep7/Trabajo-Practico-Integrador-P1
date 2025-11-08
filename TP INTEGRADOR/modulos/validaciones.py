"""
Módulo de Validaciones
Funciones para validar entrada de datos y manejo de errores
"""


def validar_numero_positivo(valor, nombre="valor"):
    """
    Valida que un número sea positivo.

    Args:
        valor: El valor a validar (str o int)
        nombre: Nombre del campo para el mensaje de error

    Returns:
        tuple: (bool, int or str) - (is_valid, value_or_error_message)
    """
    # Convertir int a string si es necesario
    if isinstance(valor, int):
        valor = str(valor)

    if not isinstance(valor, str):
        return False, f"Error en {nombre}: debe ser un número entero positivo"

    if not valor.strip():
        return False, f"Error en {nombre}: debe ser un número entero positivo"

    if not valor.strip().isdigit():
        return False, f"Error en {nombre}: debe ser un número entero positivo"

    num = int(valor.strip())
    if num <= 0:
        return False, f"Error en {nombre}: debe ser un número entero positivo"

    return True, num


def validar_texto_no_vacio(texto, nombre="texto"):
    """
    Valida que un texto no esté vacío.

    Args:
        texto: El texto a validar
        nombre: Nombre del campo para el mensaje de error

    Returns:
        tuple: (bool, str or error_message) - (is_valid, value_or_error_message)
    """
    if not texto or not texto.strip():
        return False, f"Error: {nombre} no puede estar vacío"
    return True, texto.strip()


def validar_pais(nombre, poblacion, superficie, continente):
    """
    Valida los datos de un país.

    Args:
        nombre: Nombre del país
        poblacion: Población (debe ser número positivo)
        superficie: Superficie en km² (debe ser número positivo)
        continente: Continente

    Returns:
        tuple: (bool, dict or str) - (is_valid, data_or_error_message)
    """
    nombre_valid, nombre_result = validar_texto_no_vacio(nombre, "Nombre del país")
    if not nombre_valid:
        return False, nombre_result

    poblacion_valid, poblacion_result = validar_numero_positivo(poblacion, "Población")
    if not poblacion_valid:
        return False, poblacion_result

    superficie_valid, superficie_result = validar_numero_positivo(superficie, "Superficie")
    if not superficie_valid:
        return False, superficie_result

    continente_valid, continente_result = validar_texto_no_vacio(continente, "Continente")
    if not continente_valid:
        return False, continente_result

    return True, {
        "nombre": nombre_result,
        "poblacion": poblacion_result,
        "superficie": superficie_result,
        "continente": continente_result
    }


def validar_rango_poblacion(min_poblacion, max_poblacion):
    """
    Valida que los rangos de población sean válidos.

    Args:
        min_poblacion: Población mínima
        max_poblacion: Población máxima

    Returns:
        tuple: (bool, tuple or str) - (is_valid, (min_val, max_val) or error_message)
    """
    min_valid, min_result = validar_numero_positivo(min_poblacion, "Población mínima")
    if not min_valid:
        return False, min_result

    max_valid, max_result = validar_numero_positivo(max_poblacion, "Población máxima")
    if not max_valid:
        return False, max_result

    if min_result > max_result:
        return False, "Error en rango de población: La población mínima no puede ser mayor que la máxima"

    return True, (min_result, max_result)


def validar_rango_superficie(min_superficie, max_superficie):
    """
    Valida que los rangos de superficie sean válidos.

    Args:
        min_superficie: Superficie mínima
        max_superficie: Superficie máxima

    Returns:
        tuple: (bool, tuple or str) - (is_valid, (min_val, max_val) or error_message)
    """
    min_valid, min_result = validar_numero_positivo(min_superficie, "Superficie mínima")
    if not min_valid:
        return False, min_result

    max_valid, max_result = validar_numero_positivo(max_superficie, "Superficie máxima")
    if not max_valid:
        return False, max_result

    if min_result > max_result:
        return False, "Error en rango de superficie: La superficie mínima no puede ser mayor que la máxima"

    return True, (min_result, max_result)
