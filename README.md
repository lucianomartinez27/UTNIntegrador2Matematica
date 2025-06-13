# Matemática
**Tecnicatura Universitaria en Programación** - *Universidad Tecnológica Nacional*
- **Trabajo Practico Integrador**
- **Implementación de Operaciones con Conjuntos Matemáticos en Python**

## Estudiantes
* Martínez Luciano Joaquín – lucianomartinez27@gmail.com
* Rodriguez Santiago Gabriel – santiii.ssg@gmail.com

**Comisión:** 4

**Profesor:** Eduardo Mónaco

**Tutor:** Araceli Rojas 

## Descripción del Proyecto

Este proyecto implementa un sistema para representar y operar con conjuntos matemáticos. 
Utilizando el concepto de teoría de conjuntos, el programa puede:

- Representar conjuntos matemáticos a partir de DNIs
- Realizar operaciones entre conjuntos: unión, intersección, diferencia y diferencia simétrica
- Visualizar la estructura de los conjuntos y sus operaciones
- Evaluar expresiones lógicas sobre los conjuntos

## Estructura del repositorio:

- **main.py**: Implementación principal de las funciones para operaciones con conjuntos
- **conjuntos.ipynb**: Notebook con ejemplos, visualizaciones y explicaciones matemáticas
- **carpeta imagenes**: Imágenes que muestran la representación visual de las operaciones entre conjuntos

El código fuente incluye comentarios y estructura adecuada, manteniendo un código limpio, ordenado y bien documentado.

## Desarrollo

El proyecto utiliza programación estructurada con funciones para cada operación:
- Funciones para operaciones básicas entre conjuntos: `calcular_union`, `calcular_interseccion`, `calcular_diferencia`, `calcular_diferencia_simetrica`
- Funciones para análisis de DNIs: `convertir_a_conjunto`, `conteo_de_frecuencia`
- Funciones para evaluación de expresiones lógicas: `digitos_comunes`, `calcular_predominio_digitos_altos`
- Funciones para operaciones con años de nacimiento: `anio_par_impar`, `es_bisiesto`, `producto_cartesiano`

## Tareas realizadas por cada integrante

El documento se realizó en conjunto, Santiago realizó las operaciones entre conjuntos y Luciano dibujó los diagramas.
En cuanto al código en Python Luciano realizó las operaciones con DNIs y generación de conjuntos mientras que Santiago realizó las operaciones con fechas de nacimiento.

## Relación entre expresiones lógicas y código implementado

El proyecto implementa varias expresiones lógicas matemáticas en código Python:

1. **Dígito común**: La expresión lógica `x ∈ A ∧ x ∈ B ⟹ x es dígito común` se implementa en la función `digitos_comunes()` que identifica elementos que pertenecen a la intersección de dos conjuntos.

2. **Conjunto con predominio de dígitos altos**: La expresión lógica `|{n ∈ S | n ≥ 5}| > |{n ∈ S | n < 5}| ⟹ S es conjunto con predominio de dígitos altos` se implementa en la función `calcular_predominio_digitos_altos()` que compara la cantidad de dígitos altos y bajos en un conjunto.

3. **Operaciones entre conjuntos**: Las operaciones matemáticas de unión (∪), intersección (∩), diferencia (-) y diferencia simétrica (△) se implementan en sus respectivas funciones, siguiendo fielmente las definiciones matemáticas.

## Presentación:

Link de video: https://www.youtube.com/watch?v=sIepq3JsBXk