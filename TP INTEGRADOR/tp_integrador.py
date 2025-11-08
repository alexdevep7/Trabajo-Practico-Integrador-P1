"""
TRABAJO PRACTICO INTEGRADOR - PROGRAMACION 1
Gestion de Datos de Paises en Python: filtros, ordenamientos y estadisticas

Autores: Estudiantes TUPAD - Programacion 1
Universidad Tecnologica Nacional (UTN)
Anio: 2025
"""

import sys
import os
import modulos.datos as datos
from modulos.busquedas import buscar_pais
from modulos.filtros import filtrar_por_continente, filtrar_por_rango_poblacion, filtrar_por_rango_superficie, obtener_continentes
from modulos.ordenamiento import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie
from modulos.estadisticas import (
    obtener_pais_mayor_poblacion, obtener_pais_menor_poblacion,
    calcular_promedio_poblacion, calcular_promedio_superficie,
    contar_paises_por_continente, obtener_pais_mayor_superficie,
    obtener_pais_menor_superficie
)
from modulos.utilidades import mostrar_pais, mostrar_tabla_paises, mostrar_estadistica, limpiar_pantalla, pausa


def mostrar_menu_principal():
    """Muestra el menu principal y retorna opcion seleccionada."""
    limpiar_pantalla()
    print("=" * 60)
    print("GESTION DE DATOS DE PAISES".center(60))
    print("=" * 60)
    print("\n1.  Agregar un pais")
    print("2.  Actualizar datos de un pais")
    print("3.  Buscar un pais por nombre")
    print("4.  Filtrar paises")
    print("5.  Ordenar paises")
    print("6.  Ver estadisticas")
    print("7.  Ver todos los paises")
    print("8.  Salir")
    print("\n" + "-" * 60)
    return input("Seleccione una opcion (1-8): ").strip()


def agregar_pais():
    """Permite agregar un nuevo pais."""
    print("\n--- AGREGAR PAIS ---")

    nombre_input = input("Nombre del pais: ")
    if not nombre_input or not nombre_input.strip():
        print("X Error: Nombre no puede estar vacio")
        pausa()
        return

    poblacion_input = input("Poblacion: ")
    if not poblacion_input or not poblacion_input.isdigit() or int(poblacion_input) <= 0:
        print("X Error: Poblacion debe ser un numero entero positivo")
        pausa()
        return

    superficie_input = input("Superficie (km2): ")
    if not superficie_input or not superficie_input.isdigit() or int(superficie_input) <= 0:
        print("X Error: Superficie debe ser un numero entero positivo")
        pausa()
        return

    continente_input = input("Continente: ")
    if not continente_input or not continente_input.strip():
        print("X Error: Continente no puede estar vacio")
        pausa()
        return

    datos.agregar_pais(nombre_input.strip(), int(poblacion_input), int(superficie_input), continente_input.strip())
    pausa()


def actualizar_pais():
    """Permite actualizar poblacion y/o superficie de un pais."""
    print("\n--- ACTUALIZAR PAIS ---")

    nombre_input = input("Nombre del pais a actualizar: ")
    if not nombre_input or not nombre_input.strip():
        print("X Error: Nombre no puede estar vacio")
        pausa()
        return

    pais = datos.obtener_pais(nombre_input.strip())
    if not pais:
        print(f"X Pais '{nombre_input}' no encontrado")
        pausa()
        return

    mostrar_pais(pais)

    print("Ingrese los nuevos valores (dejar vacio para no cambiar)")
    poblacion_str = input("Nueva poblacion: ").strip()
    superficie_str = input("Nueva superficie: ").strip()

    poblacion = None
    superficie = None

    if poblacion_str:
        if not poblacion_str.isdigit() or int(poblacion_str) <= 0:
            print("X Error: Poblacion debe ser un numero entero positivo")
            pausa()
            return
        poblacion = int(poblacion_str)

    if superficie_str:
        if not superficie_str.isdigit() or int(superficie_str) <= 0:
            print("X Error: Superficie debe ser un numero entero positivo")
            pausa()
            return
        superficie = int(superficie_str)

    if poblacion is None and superficie is None:
        print("X No se ingreso ningun dato para actualizar")
    else:
        datos.actualizar_pais(nombre_input.strip(), poblacion, superficie)

    pausa()


def buscar_pais_menu():
    """Permite buscar un pais por nombre."""
    print("\n--- BUSCAR PAIS ---")

    nombre_input = input("Nombre a buscar: ")
    if not nombre_input or not nombre_input.strip():
        print("X Error: Nombre no puede estar vacio")
        pausa()
        return

    print("\n1. Busqueda exacta")
    print("2. Busqueda parcial")
    tipo = input("Seleccione tipo de busqueda (1-2): ").strip()

    resultados = buscar_pais(
        datos.obtener_todos(),
        nombre_input,
        busqueda_exacta=(tipo == "1")
    )

    if resultados:
        mostrar_tabla_paises(resultados, f"Resultados de busqueda: '{nombre_input}'")
    else:
        print(f"\nX No se encontraron paises con '{nombre_input}'")

    pausa()


# ========================
# CODIGO ALEX
# ========================


def ejecutar():
    """Bucle principal de la aplicacion."""
    ejecutando = True
    while ejecutando:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            agregar_pais()
        elif opcion == "2":
            actualizar_pais()
        elif opcion == "3":
            buscar_pais_menu()
        elif opcion == "4":
            filtrar_paises_menu()
        elif opcion == "5":
            ordenar_paises_menu()
        elif opcion == "6":
            mostrar_estadisticas_menu()
        elif opcion == "7":
            mostrar_todos_paises()
        elif opcion == "8":
            print("\nGracias por usar la aplicacion! Hasta luego.\n")
            ejecutando = False
        else:
            print("X Opcion invalida. Intente nuevamente.")
            pausa()


def main():
    """Punto de entrada de la aplicacion."""
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(ruta_script, "datos", "paises.csv")

    if not os.path.exists(ruta_csv):
        print("X No se pudo inicializar la aplicacion. Verifique el archivo CSV.")
        sys.exit(1)

    datos.inicializar(ruta_csv)
    ejecutar()


if __name__ == "__main__":
    main()
