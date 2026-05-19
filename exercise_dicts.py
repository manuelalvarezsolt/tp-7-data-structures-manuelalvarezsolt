# Ejercicios de diccionarios: sistema de inventario


def create_inventory(items):
    """
    Crea un diccionario "inventario" a partir de una lista de items.
    Cada clave es el nombre de un item y su valor es la cantidad de veces
    que aparece en la lista.

    Args:
        items: Lista de items (strings)

    Returns:
        Un diccionario con cada item y su cantidad
    """
    d = {}
    for element in items:
        d[element] = items.count(element)
    return d
def add_items(inventario, items):
    """
    Agrega una lista de items a un inventario existente. Si un item ya está
    en el inventario, incrementa su cantidad en 1. Si no, lo agrega con
    cantidad 1.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a agregar

    Returns:
        El inventario actualizado
    """
    for cosas in items:
        if cosas in inventario:
            inventario[cosas] += 1
        else:
            inventario[cosas] = 1
    return inventario



def decrement_items(inventario, items):
    """
    Resta 1 a la cantidad del inventario por cada vez que un item aparezca
    en la lista. Las cantidades no pueden ser negativas: si un item se quiere
    restar más veces que su cantidad disponible, debe quedar en 0 y las
    solicitudes extra deben ser ignoradas.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a decrementar

    Returns:
        El inventario actualizado (sin valores negativos)
    """
    for cosas in items:
        if cosas in inventario:
            if inventario[cosas] > 0:
                inventario[cosas] -= 1
    return inventario

def remove_item(inventario, item):
    """
    Elimina un item del inventario por completo (clave y cantidad).
    Si el item no está en el inventario, retornar el inventario sin cambios.

    Args:
        inventario: Diccionario con el inventario actual
        item: String con el nombre del item a eliminar

    Returns:
        El inventario actualizado (o sin cambios si el item no existe)
    """
    if item in inventario:
        inventario.pop(item)
    return inventario


def list_inventory(inventario):
    """
    Retorna una lista de tuplas (item, cantidad) con el contenido del
    inventario. Solo incluye los items con cantidad mayor a 0.

    Args:
        inventario: Diccionario con el inventario

    Returns:
        Lista de tuplas (item, cantidad) con cantidad > 0
    """
    lista = []
    for claves in inventario:
        if inventario[claves] > 0:
            lista.append((claves, inventario[claves]))
    return lista

def find_max_value(diccionario):
    """
    Recibe un diccionario de nombres y puntajes, y retorna la clave
    (nombre) con el valor (puntaje) más alto. Si el diccionario está
    vacío, retorna "".

    Args:
        diccionario: Diccionario {nombre: puntaje}

    Returns:
        String con la clave de mayor valor, o "" si el dict está vacío

    Ejemplo:
        find_max_value({'John': 85, 'Emma': 92, 'Sophia': 78}) -> 'Emma'
    """
    lista = []
    otralista = []
    if diccionario == {}:
        return ""
    for pibardos in diccionario:
        lista.append(diccionario[pibardos])
        otralista.append(pibardos)
    crack = max(lista)
    posicion = lista.index(crack)
    return otralista[posicion]




def reverse_dict(diccionario):
    """
    Invierte un diccionario: cada valor pasa a ser clave, y cada clave
    pasa a ser valor. Si varias claves comparten el mismo valor, sus
    nombres se concatenan (en el orden en que aparecen).

    Args:
        diccionario: Diccionario original

    Returns:
        Nuevo diccionario invertido

    Ejemplo:
        reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 2})
        -> {1: 'a', 2: 'be', 3: 'cd'}
    """
    nuevo = {}
    for claves in diccionario:
        if diccionario[claves] in nuevo:
            nuevo[diccionario[claves]] += claves
        else:
            nuevo[diccionario[claves]] = claves
    return nuevo

def word_frequency(palabras):
    """
    Cuenta cuántas veces aparece cada palabra en la lista y lo retorna
    como un diccionario {palabra: cantidad}.

    Args:
        palabras: Lista de palabras (strings). También debe soportar
                  un string vacío retornando un diccionario vacío.

    Returns:
        Diccionario con la frecuencia de cada palabra

    Ejemplo:
        word_frequency(["apple", "banana", "apple", "orange", "banana", "apple"])
        -> {'apple': 3, 'banana': 2, 'orange': 1}
    """
    d = {}
    for cosas in palabras:
        d[cosas] = palabras.count(cosas)
    return d


def find_biggest_expense(gastos):
    """
    Recibe un diccionario donde cada clave es una categoría y el valor
    una lista de gastos (números). Retorna la categoría con el
    promedio más alto. Si el diccionario está vacío, retorna "".

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        String con la categoría de mayor promedio, o "" si vacío

    Ejemplo:
        find_biggest_expense({'Food': [60, 80, 100],
                              'Transport': [10, 1, 2],
                              'Games': [10, 20, 30]}) -> 'Food'
    """
    if gastos == {}:
        return ""
    promedios = []
    lista = []
    for cosas in gastos:
        promedios.append(sum(gastos[cosas]) / len(gastos[cosas]))
        lista.append(cosas)
    maximo = max(promedios)
    indexado = promedios.index(maximo)
    return lista[indexado]


def sum_expenses(gastos):
    """
    Recibe un diccionario de categorías con listas de gastos y retorna
    un nuevo diccionario con la suma total de los gastos por categoría.

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        Diccionario {categoria: suma_total}

    Ejemplo:
        sum_expenses({'Food': [60, 80, 100],
                      'Transport': [10, 1, 2],
                      'Games': [10, 20, 30]})
        -> {'Food': 240, 'Transport': 13, 'Games': 60}
    """
    d = {}
    for cosas in gastos:
        d[cosas] = sum(gastos[cosas])
    return d

def sum_expenses_by_type(gastos):
    """
    Recibe un diccionario de categorías cuyos valores son listas de
    tuplas (tipo, monto). Retorna un nuevo diccionario con la suma
    de montos agrupada por tipo (no por categoría).

    Args:
        gastos: Diccionario {categoria: [(tipo, monto), ...]}

    Returns:
        Diccionario {tipo: suma_total_del_tipo}

    Ejemplo:
        sum_expenses_by_type({
            'Food': [("A", 60), ("B", 100), ("A", 20)],
            'Transport': [("A", 10), ("B", 50), ("C", 5)],
            'Games': [("A", 6), ("B", 24), ("C", 99)]
        })
        -> {'A': 96, 'B': 174, 'C': 104}
    """
    d = {}
    for cosas in gastos:
        for tuplas in gastos[cosas]:
            if tuplas[0] in d:
                d[tuplas[0]] += tuplas[1]
            else:
                d[tuplas[0]] = tuplas[1]
    return d
