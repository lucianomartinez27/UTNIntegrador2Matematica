import json

def convertir_a_conjunto(dni):
    conjunto = []
    for numero in dni:
        if numero not in conjunto:
            conjunto.append(numero)
    conjunto.sort()
    return conjunto

def calcular_union(conjunto1, conjunto2):
    union = [numero for numero in conjunto1]
    for numero in conjunto2:
        if numero not in union:
            union.append(numero)
    union.sort()
    return union

def calcular_interseccion(conjunto1, conjunto2):
    interseccion = []
    for numero in conjunto1:
        if numero in conjunto2:
            interseccion.append(numero)
    interseccion.sort()
    return interseccion

def calcular_diferencia(conjunto1, conjunto2):
    diferencia = [numero for numero in conjunto1]
    for numero in conjunto2:
        if numero in diferencia:
            diferencia.remove(numero)
    diferencia.sort()
    return diferencia

def calcular_diferencia_simetrica(conjunto1, conjunto2):
    union = calcular_union(conjunto1, conjunto2)
    interseccion = calcular_interseccion(conjunto1, conjunto2)
    diferencia = []
    for numero in union:
        if numero not in interseccion:
            diferencia.append(numero)
    diferencia.sort()
    return diferencia

def calculo_y_visualizacion(conjunto1, conjunto2):
    print(f"Union: {calcular_union(conjunto1, conjunto2)}")
    print(f"Interseccion: {calcular_interseccion(conjunto1, conjunto2)}")
    print(f"Diferencia: {calcular_diferencia(conjunto1, conjunto2)}")
    print(f"Diferencia Simetrica: {calcular_diferencia_simetrica(conjunto1, conjunto2)}")

def conteo_de_frecuencia(dni):
    conteo = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0
    }

    for numero in dni:
        conteo[numero] += 1
    return conteo

def suma_digitos_dni(dni):
    suma = 0
    for digito in dni:
        suma += int(digito)
    return suma

# Si algún dígito aparece en todos los conjuntos, se marca como dígito común.
def digitos_comunes(conjunto1, conjunto2):
    interseccion = calcular_interseccion(conjunto1, conjunto2)
    conjunto_univesal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for numero in conjunto_univesal:
        if str(numero) in interseccion:
            print(f"Dígito común: {numero}")
        else:
            print(f"No pertenece a dígito común: {numero}")

# Si conjunto tiene más números mayores o iguales a 5 que menores a 5 se marca como conjunto con predominio de dígitos altos
def calcular_predominio_digitos_altos(conjunto):
    digitos_altos = 0
    digitos_bajos = 0
    for numero in conjunto:
        if int(numero) >= 5:
            digitos_altos += 1
        else:
            digitos_bajos += 1
    if digitos_altos > digitos_bajos:
        print(f"{conjunto} es un conjunto predominio de dígitos altos")
    elif digitos_altos == digitos_bajos:
        print(f"{conjunto} es un conjunto sin predominio de dígitos")
    else:
        print(f"{conjunto} es un conjunto predominio de dígitos bajos")


#//////////////////////// anios /////////////////////

lista_anios = [1994, 1997]

# Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
def anio_par_impar(anios):
    pares = 0
    impares = 0

    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1 

    print(f'Nacidos en años pares: {pares}')
    print(f'Nacidos en años impares: {impares}')

# Si todos nacieron después del 2000, mostrar "Grupo Z".
def grupo_z():
    todos_son_mayores = True
    for anio in lista_anios:
        if anio <= 2000:
            todos_son_mayores = False
            print('El grupo tiene años menores a 2000')
            break
    if todos_son_mayores:
        print("Grupo Z")

# Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.
def producto_cartesiano(anios):
    edades = [30, 27]

    cartesiano = []

    for lista_anios in anios:
        for edad in edades:
            cartesiano.append((lista_anios, edad))

    print(cartesiano)

# Implementar una función para determinar si un año es bisiesto.
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
def verificar_anios_bisiestos(lista_anios):
    if any(es_bisiesto(anio) for anio in lista_anios):
        print("Tenemos un año especial")
    else:
        print("Ningún año es bisiesto")


if __name__ == "__main__":
    dni_luciano = "38262759"
    dni_santiago = "40679033"

    print("-" * 10, " A. Operaciones con DNIs ", "-" *10)
    conjunto1 = convertir_a_conjunto(dni_luciano)
    conjunto2 = convertir_a_conjunto(dni_santiago)
    calculo_y_visualizacion(conjunto1, conjunto2)
    print("-" * 20)
    print("Conteo Luciano: ", json.dumps(conteo_de_frecuencia(dni_luciano), indent=4))
    print("Conteo Santiago: ", json.dumps(conteo_de_frecuencia(dni_santiago), indent=4))

    print("-" * 20)
    print("Si algún dígito aparece en todos los conjuntos, se marca como dígito común:")
    digitos_comunes(conjunto1, conjunto2)
    print("-" * 20)
    print("Si conjunto tiene más números mayores o iguales a 5 que menores a 5 se marca como conjunto con predominio de dígitos altos")
    calcular_predominio_digitos_altos(conjunto1)
    calcular_predominio_digitos_altos(conjunto2)

    print("-" * 10, " B. Operaciones con años de nacimiento ", "-" * 10)
    producto_cartesiano(lista_anios)
    verificar_anios_bisiestos(lista_anios)
    grupo_z()
    anio_par_impar(lista_anios)