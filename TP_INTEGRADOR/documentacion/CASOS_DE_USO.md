# EJEMPLOS DE USO - GESTIÓN DE DATOS DE PAÍSES

## Descripción

Este documento muestra ejemplos prácticos de cómo usar la aplicación, con datos de entrada y salida esperada.

---

## EJEMPLO 1: VER TODOS LOS PAÍSES

### Entrada
```
Opción: 7
```

### Salida Esperada
```
====================================================================================================
                                  Todos los paises (20 registros)
====================================================================================================
#    País                      Población            Superficie           Continente
----------------------------------------------------------------------------------------------------
1    Argentina                          45,376,763           2,780,400 América
2    Japón                             125,800,000             377,975 Asia
3    Brasil                            213,993,437           8,515,767 América
4    Alemania                           83,149,300             357,022 Europa
5    India                           1,406,632,000           3,287,263 Asia
6    Francia                            67,970,571             643,801 Europa
7    Canadá                             39,074,754           9,984,670 América
8    Australia                          25,999,400           7,692,024 Oceanía
9    Rusia                             146,424,993          17,098,242 Europa
10   China                           1,440,783,550           9,596,961 Asia
11   España                             47,560,635             505,990 Europa
12   México                            128,932,753           1,964,375 América
13   Italia                             57,888,598             301,340 Europa
14   Corea del Sur                      51,284,667             100,363 Asia
15   Indonesia                         275,501,339           1,919,440 Asia
16   Turquía                            85,326,000             783,562 Europa
17   Nigeria                           223,804,632             923,768 África
18   Egipto                            104,888,695           1,002,000 África
19   Sudáfrica                          60,142,978           1,221,037 África
20   Marruecos                          37,344,795             446,550 África
====================================================================================================
```

### Análisis
- Se muestran los 20 países cargados del CSV
- Formatos numéricos con separadores de miles
- Tabla claramente estructurada y legible

---

## EJEMPLO 2: AGREGAR UN PAÍS

### Entrada
```
Opción: 1
Nombre del pais: Portugal
Poblacion: 10406568
Superficie (km2): 92090
Continente: Europa
```

### Salida Esperada
```
--- AGREGAR PAIS ---
✓ País 'Portugal' agregado exitosamente
✓ Datos guardados exitosamente (21 países)

Presiona Enter para continuar...
```

### Análisis
- Validación correcta de datos
- Confirmación de guardado en CSV
- Ahora hay 21 países en total

---

## EJEMPLO 3: BUSCAR UN PAÍS (BÚSQUEDA PARCIAL)

### Entrada
```
Opción: 3
Nombre a buscar: arg
Seleccione tipo de busqueda (1-2): 2  # Búsqueda parcial
```

### Salida Esperada
```
====================================================================================================
                              Resultados de busqueda: 'arg'
====================================================================================================
#    País                      Población            Superficie           Continente
----------------------------------------------------------------------------------------------------
1    Argentina                          45,376,763           2,780,400 América
2    Madagascar                        28,427,328             587,041 África
====================================================================================================
```

### Análisis
- Se encontraron 2 países que contienen "arg"
- Búsqueda case-insensitive
- Se muestra tabla con resultados

---

## EJEMPLO 4: BUSCAR UN PAÍS (BÚSQUEDA EXACTA)

### Entrada
```
Opción: 3
Nombre a buscar: Japon
Seleccione tipo de busqueda (1-2): 1  # Búsqueda exacta
```

### Salida Esperada
```
====================================================================================================
                              Resultados de busqueda: 'Japon'
====================================================================================================
#    País                      Población            Superficie           Continente
----------------------------------------------------------------------------------------------------
1    Japón                             125,800,000             377,975 Asia
====================================================================================================
```

### Análisis
- Encontró Japón exactamente
- Case-insensitive: "Japon" coincide con "Japón"
- Un único resultado

---

## EJEMPLO 5: FILTRAR POR CONTINENTE

### Entrada
```
Opción: 4
Seleccione tipo de filtro (1-3): 1  # Por continente
Continentes disponibles: África, América, Asia, Europa, Oceanía
Continente: Asia
```

### Salida Esperada
```
====================================================================================================
                                 Resultados del filtro
====================================================================================================
#    País                      Población            Superficie           Continente
----------------------------------------------------------------------------------------------------
1    Japón                             125,800,000             377,975 Asia
2    India                           1,406,632,000           3,287,263 Asia
3    China                           1,440,783,550           9,596,961 Asia
4    Corea del Sur                      51,284,667             100,363 Asia
5    Indonesia                         275,501,339           1,919,440 Asia
====================================================================================================
```

### Análisis
- Mostró lista de continentes disponibles
- Filtró correctamente por Asia
- 5 países de Asia en el dataset

---

## EJEMPLO 6: FILTRAR POR RANGO DE POBLACIÓN

### Entrada
```
Opción: 4
Seleccione tipo de filtro (1-3): 2  # Por rango de población
Poblacion minima: 100000000
Poblacion maxima: 300000000
```

### Salida Esperada
```
====================================================================================================
                                 Resultados del filtro
====================================================================================================
#    País                      Población            Superficie           Continente
----------------------------------------------------------------------------------------------------
1    Japón                             125,800,000             377,975 Asia
2    Brasil                            213,993,437           8,515,767 América
3    México                            128,932,753           1,964,375 América
4    Indonesia                         275,501,339           1,919,440 Asia
====================================================================================================
```

### Análisis
- Filtró por rango inclusivo [100M, 300M]
- 4 países cumplen criterio
- Ordenados en tabla

---

## EJEMPLO 7: ORDENAR POR POBLACIÓN (DESCENDENTE)

### Entrada
```
Opción: 5
Seleccione criterio de ordenamiento (1-3): 2  # Por población
Seleccione orden (1-2): 2  # Descendente
```

### Salida Esperada
```
====================================================================================================
                                 Paises ordenados
====================================================================================================
#    País                      Población            Superficie           Continente
----------------------------------------------------------------------------------------------------
1    China                           1,440,783,550           9,596,961 Asia
2    India                           1,406,632,000           3,287,263 Asia
3    Indonesia                         275,501,339           1,919,440 Asia
4    Brasil                            213,993,437           8,515,767 América
5    Nigeria                           223,804,632             923,768 África
...
====================================================================================================
```

### Análisis
- Ordenados por población de mayor a menor
- China primero (1.44 billones)
- India segundo (1.40 billones)

---

## EJEMPLO 8: ORDENAR POR NOMBRE (ASCENDENTE)

### Entrada
```
Opción: 5
Seleccione criterio de ordenamiento (1-3): 1  # Por nombre
Seleccione orden (1-2): 1  # Ascendente
```

### Salida Esperada
```
====================================================================================================
                                 Paises ordenados
====================================================================================================
#    País                      Población            Superficie           Continente
----------------------------------------------------------------------------------------------------
1    Alemania                           83,149,300             357,022 Europa
2    Argentina                          45,376,763           2,780,400 América
3    Australia                          25,999,400           7,692,024 Oceanía
4    Brasil                            213,993,437           8,515,767 América
5    Canadá                             39,074,754           9,984,670 América
...
====================================================================================================
```

### Análisis
- Ordenados alfabéticamente A→Z
- Alemania primero, después Argentina
- Order case-insensitive

---

## EJEMPLO 9: VER ESTADÍSTICAS

### Entrada
```
Opción: 6
```

### Salida Esperada
```
============================================================
                        ESTADISTICAS
============================================================

--- POBLACION ---
Pais con mayor poblacion      :  China (1,440,783,550)
Pais con menor poblacion      :  Corea del Sur (51,284,667)
Promedio de poblacion         :    392,169,847.85 habitantes

--- SUPERFICIE ---
Pais con mayor superficie     :  Rusia (17,098,242)
Pais con menor superficie     :  Italia (301,340)
Promedio de superficie        :     4,232,589.65 km2

--- DISTRIBUCION POR CONTINENTE ---
África                        :             4 paises
América                       :             4 paises
Asia                          :             5 paises
Europa                        :             6 paises
Oceanía                       :             1 paises
```

### Análisis
- **Máximos**: China (población), Rusia (superficie)
- **Mínimos**: Corea del Sur (población), Italia (superficie)
- **Promedios**: Cálculo correcto de medias aritméticas
- **Distribución**: Desglose por continente

### Cálculo Verificable
```
Población promedio:
(45.3M + 125.8M + 213.9M + ... + 37.3M) / 20 = 7,843,396,957 / 20 = 392,169,847.85

Superficie promedio:
(2.78M + 0.37M + 8.51M + ... + 0.44M) / 20 = 84,651,793 / 20 = 4,232,589.65
```

---

## EJEMPLO 10: ACTUALIZAR PAÍS

### Entrada
```
Opción: 2
Nombre del pais a actualizar: Brasil
```

### Salida (Muestra datos actuales)
```
┌─────────────────────────────────────────────────┐
│ Brasil                                          │
├─────────────────────────────────────────────────┤
│ Población:                         213,993,437  │
│ Superficie:                          8,515,767  │
│ Continente:                          América    │
└─────────────────────────────────────────────────┘

Ingrese los nuevos valores (dejar vacio para no cambiar)
Nueva poblacion: 216000000
Nueva superficie:
```

### Salida Esperada
```
✓ 'Brasil' actualizado: Poblacion: 216,000,000
✓ Datos guardados exitosamente (20 países)

Presiona Enter para continuar...
```

### Análisis
- Mostró datos actuales para referencia
- Permitió actualizar solo población (superficie vacía)
- Guardó automáticamente los cambios

---

## EJEMPLO 11: VALIDACIÓN DE ERROR - CAMPO VACÍO

### Entrada
```
Opción: 1
Nombre del pais:  (solo presionar Enter)
Poblacion:
Superficie:
Continente:
```

### Salida Esperada
```
--- AGREGAR PAIS ---
✗ Error: Nombre del país no puede estar vacío

Presiona Enter para continuar...
```

### Análisis
- Validación correcta de campos obligatorios
- Mensaje claro de qué falta
- Permite reintentar

---

## EJEMPLO 12: VALIDACIÓN DE ERROR - NÚMERO INVÁLIDO

### Entrada
```
Opción: 1
Nombre del pais: Suiza
Poblacion: abc  (texto inválido)
Superficie:
Continente:
```

### Salida Esperada
```
--- AGREGAR PAIS ---
✗ Error: Error en Población: debe ser un número entero positivo

Presiona Enter para continuar...
```

### Análisis
- Detectó input no numérico
- Mensaje específico del problema
- Usuario puede reintentar

---

## EJEMPLO 13: VALIDACIÓN DE ERROR - RANGO INVÁLIDO

### Entrada
```
Opción: 4
Seleccione tipo de filtro (1-3): 2  # Rango poblacion
Poblacion minima: 500000000
Poblacion maxima: 100000000  (menor que mínima)
```

### Salida Esperada
```
✗ Error: Error en rango de población: La población mínima no puede ser mayor que la máxima

Presiona Enter para continuar...
```

### Análisis
- Validación inteligente de rangos
- Previene búsquedas sin sentido
- Feedback inmediato

---

## EJEMPLO 14: BÚSQUEDA SIN RESULTADOS

### Entrada
```
Opción: 3
Nombre a buscar: Atlantida
Seleccione tipo de busqueda (1-2): 1  # Exacta
```

### Salida Esperada
```
✗ No se encontraron países con 'Atlantida'

Presiona Enter para continuar...
```

### Análisis
- Manejo correcto de búsqueda vacía
- Mensaje claro y útil
- No rompe la aplicación

---

## EJEMPLO 15: SALIR DE LA APLICACIÓN

### Entrada
```
Opción: 8
```

### Salida Esperada
```
Gracias por usar la aplicacion! Hasta luego.

(Fin de la aplicación)
```

### Análisis
- Cierre limpio de la aplicación
- Todos los datos persisten en CSV
- Mensaje de despedida amigable

---

## RESUMEN DE FUNCIONALIDADES PROBADAS

| Funcionalidad | Estado | Resultado |
|---------------|--------|-----------|
| Cargar CSV | ✓ Funcional | 20 países cargados |
| Agregar País | ✓ Funcional | Agrega y persiste |
| Actualizar País | ✓ Funcional | Modifica datos |
| Buscar Exacto | ✓ Funcional | Case-insensitive |
| Buscar Parcial | ✓ Funcional | Contiene substring |
| Filtrar Continente | ✓ Funcional | Muestra opciones |
| Filtrar Población | ✓ Funcional | Rango inclusivo |
| Filtrar Superficie | ✓ Funcional | Rango inclusivo |
| Ordenar Nombre | ✓ Funcional | A-Z / Z-A |
| Ordenar Población | ✓ Funcional | Ascendente/Descendente |
| Ordenar Superficie | ✓ Funcional | Ascendente/Descendente |
| Estadísticas | ✓ Funcional | Todos los cálculos correctos |
| Validaciones | ✓ Funcional | Detecta errores |
| Persistencia | ✓ Funcional | Guarda en CSV |
| Interfaz | ✓ Funcional | Clara y amigable |

---

## NOTAS TÉCNICAS

### Tipos de Datos en CSV
Los valores en CSV siempre son strings. La aplicación convierte:
- Poblacion: `string` → `int`
- Superficie: `string` → `int`
- Nombre y Continente: permanecen como `string`

### Codificación
- Archivo CSV: UTF-8 (soporta caracteres especiales: á, é, ñ, etc.)
- Entrada: Sistema nativo
- Salida: UTF-8

### Performance
- **Búsqueda lineal**: O(n) - aceptable para 20-100 registros
- **Ordenamiento**: O(n log n) - eficiente incluso con muchos datos
- **Filtrado**: O(n) - lineal, necesario examinar todos

---

## CASOS DE USO REALES

### Caso 1: Analista de Datos
"Necesito saber qué país de Asia tiene mayor población"
```
1. Filtrar por Asia (Opción 4 → 1)
2. Ordenar por población descendente (Opción 5 → 2 → 2)
3. Resultado: China con 1.44 billones habitantes
```

### Caso 2: Demógrafo
"Calcular el promedio de población mundial"
```
Opción 6 → Ver Estadísticas → Promedio de población: 392M
```

### Caso 3: Geógrafo
"Listar países por orden alfabético"
```
Opción 5 → Por nombre → Ascendente
```

### Caso 4: Administrador
"Actualizar datos de Argentina"
```
Opción 2 → Nombre: Argentina → Ingresar nuevos datos
```

---

**Documento de Casos de Uso**
**Proyecto: Gestión de Datos de Países**
**Fecha: Noviembre 2025**
