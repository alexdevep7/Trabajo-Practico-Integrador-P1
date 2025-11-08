"""
Módulo de Utilidades
Funciones auxiliares para formatear y mostrar información
"""


def mostrar_pais(pais):
    """
    Muestra los datos de un país de forma formateada.

    Args:
        pais: Diccionario con datos del país
    """
    if pais:
        print(f"\n┌─────────────────────────────────────────────────┐")
        print(f"│ {pais['nombre']:<45} │")
        print(f"├─────────────────────────────────────────────────┤")
        print(f"│ Población:  {pais['poblacion']:>30,} │")
        print(f"│ Superficie: {pais['superficie']:>30,} km² │")
        print(f"│ Continente: {pais['continente']:<30} │")
        print(f"└─────────────────────────────────────────────────┘\n")
    else:
        print("\n✗ País no encontrado\n")


def mostrar_tabla_paises(paises, titulo="Países"):
    """
    Muestra una tabla formateada con varios países.

    Args:
        paises: Lista de diccionarios con países
        titulo: Título de la tabla
    """
    if not paises:
        print(f"\n✗ No hay países para mostrar en '{titulo}'\n")
        return

    print(f"\n{'=' * 100}")
    print(f"{titulo.center(100)}")
    print(f"{'=' * 100}")
    print(f"{'#':<4} {'País':<25} {'Población':<20} {'Superficie':<20} {'Continente':<20}")
    print(f"{'-' * 100}")

    for i, pais in enumerate(paises, 1):
        print(
            f"{i:<4} "
            f"{pais['nombre']:<25} "
            f"{pais['poblacion']:>19,} "
            f"{pais['superficie']:>19,} "
            f"{pais['continente']:<20}"
        )

    print(f"{'=' * 100}\n")


def mostrar_estadistica(titulo, valor, unidad=""):
    """
    Muestra una estadística formateada.

    Args:
        titulo: Título de la estadística
        valor: Valor a mostrar
        unidad: Unidad (opcional)
    """
    if isinstance(valor, (int, float)):
        if isinstance(valor, float):
            print(f"{titulo:<40}: {valor:>20,.2f} {unidad}")
        else:
            print(f"{titulo:<40}: {valor:>20,} {unidad}")
    else:
        print(f"{titulo:<40}: {str(valor):>20} {unidad}")


def limpiar_pantalla():
    """
    Intenta limpiar la pantalla (funciona en Linux/Mac/Windows).
    """
    import os
    os.system('clear' if os.name == 'posix' else 'cls')


def pausa():
    """
    Pausa la ejecución hasta que el usuario presione Enter.
    """
    input("\nPresiona Enter para continuar...")
