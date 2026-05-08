# Ejercicios de tuplas: búsqueda del tesoro pirata


def get_coordinate(registro):
    """
    Retorna la coordenada del mapa desde una tupla (tesoro, coordenada).

    Args:
        registro: Una tupla con el formato (tesoro, coordenada)

    Returns:
        Un string con la coordenada del mapa
    """

    tesoro, coordenada = registro
    return coordenada


def convert_coordinate(coordenada):
    """
    Separa una coordenada de formato "2A" en sus componentes ("2", "A").

    Args:
        coordenada: Un string con la coordenada (ej: "2A", "7F")

    Returns:
        Una tupla con los componentes individuales (ej: ("2", "A"))
    """

    individuales = (coordenada[0], coordenada[1])
    return individuales


def create_record(registro_azara, registro_rui):
    """
    Combina los registros de Azara y Rui si sus coordenadas coinciden.

    - Registro de Azara: (tesoro, coordenada) -> ej: ('Brass Spyglass', '4B')
    - Registro de Rui: (ubicacion, coordenada, cuadrante) ->
      ej: ('Abandoned Lighthouse', ('4', 'B'), 'Blue')

    Si las coordenadas coinciden, retornar una tupla combinada:
    (tesoro, coordenada_azara, ubicacion, coordenada_rui, cuadrante)

    Si NO coinciden, retornar el string "not a match".

    Args:
        registro_azara: Tupla (tesoro, coordenada)
        registro_rui: Tupla (ubicacion, coordenada, cuadrante)

    Returns:
        Tupla combinada si las coordenadas coinciden, o "not a match" si no.
    """

    azara = get_coordinate(registro_azara)
    coordazara = convert_coordinate(azara)
    coordrui = registro_rui[1]

    if coordazara == coordrui:
        resultado = (registro_azara[0], azara, registro_rui[0], coordrui, registro_rui[2])
        return resultado
    else:
        return "not a match"


def sum_tuple(numeros):
    """
    Recorre una tupla de números y retorna la suma total.
    Si la tupla está vacía, retorna 0.

    No se permite usar la función built-in sum(). Implementar la suma
    recorriendo la tupla con un for (o while).

    Args:
        numeros: Tupla de números (enteros o flotantes)

    Returns:
        La suma de todos los elementos de la tupla

    Ejemplo:
        sum_tuple((1, 2, 3, 4, 5)) -> 15
        sum_tuple(()) -> 0
    """
    suma = 0
    if len(numeros) == 0:
        return 0
    else:
        for num in numeros:
            suma += num

    return suma


def count_occurrences(tupla, elemento):
    """
    Recorre la tupla y cuenta cuántas veces aparece el elemento.

    No se permite usar el método .count(). Implementar el conteo
    recorriendo la tupla con un for (o while).

    Args:
        tupla: Tupla con elementos de cualquier tipo
        elemento: El elemento a contar

    Returns:
        La cantidad de veces que aparece el elemento (int)

    Ejemplo:
        count_occurrences((1, 2, 2, 3, 2), 2) -> 3
        count_occurrences(('a', 'b', 'a'), 'c') -> 0
    """
    count = 0
    for i in tupla:
        if elemento == i:
            count += 1

    return count


def find_index(tupla, elemento):
    """
    Recorre la tupla y retorna el índice de la PRIMERA aparición del
    elemento. Si el elemento no se encuentra, retorna -1.

    No se permite usar el método .index(). Implementar la búsqueda
    recorriendo la tupla con un for (o while).

    Args:
        tupla: Tupla con elementos
        elemento: El elemento a buscar

    Returns:
        El índice (int) de la primera aparición, o -1 si no está

    Ejemplo:
        find_index(('a', 'b', 'c', 'b'), 'b') -> 1
        find_index((1, 2, 3), 9) -> -1
    """
    if elemento not in tupla:
        return -1
    else:
        for i, objeto in enumerate(tupla):
            if objeto == elemento:
               return i
               break


def filter_positives(numeros):
    """
    Recorre una tupla de números y retorna una nueva tupla con solo
    los números positivos (> 0). El cero NO se considera positivo.

    Args:
        numeros: Tupla de números (enteros o flotantes)

    Returns:
        Tupla con los números positivos, en el orden original

    Ejemplo:
        filter_positives((-3, 1, 0, 5, -2, 7)) -> (1, 5, 7)
        filter_positives((-1, -2, -3)) -> ()
    """

    list = []
    for numero in numeros:
        if numero > 0:
            list.append(numero)

    newtupla = tuple(list)

    return newtupla
