"""
Enunciado:
Implementa y compara el rendimiento de dos algoritmos de ordenamiento clásicos con Quicksort y Mergesort, en Python.

Funciones a desarrollar:
- `quicksort(arr: List[int]) -> List[int]`:
    Descripción:
    Ordena una lista de números enteros utilizando el algoritmo Quicksort, dividiendo la lista en subconjuntos menores,
    mayores o iguales a un elemento pivote, y luego ordenando esos subconjuntos recursivamente.
    Parámetros:
        - `arr` (List[int]): Lista de números enteros a ordenar.

- `mergesort(arr: List[int]) -> List[int]`:
    Descripción:
    Ordena una lista de números enteros utilizando el algoritmo Mergesort, dividiendo la lista en mitades hasta obtener
    subconjuntos que se consideran ordenados, para luego mezclar esos subconjuntos de manera ordenada.
    Parámetros:
        - `arr` (List[int]): Lista de números enteros a ordenar.

- `merge(left: List[int], right: List[int]) -> List[int]`:
    Descripción:
    Función auxiliar para el Mergesort que mezcla dos sublistas ordenadas en una sola lista ordenada.
    Parámetros:
        - `left` (List[int]): Sublista izquierda ordenada.
        - `right` (List[int]): Sublista derecha ordenada.

Ejemplo:
    start = time.time()
    sorted_array_quicksort = quicksort(test_array.copy())
    end_time = time.time() - start
    print(f"Quicksort on {size} elements took: {end_time:.5f} seconds.")
    print("First 10 elements after Quicksort:", sorted_array_quicksort[:10])

Salida esperada:
- Demostración del proceso de ordenación de una lista de números enteros con Quicksort y Mergesort, incluyendo la
visualización del tiempo que cada algoritmo toma para ordenar la misma lista.
"""

import random
import time
from typing import List


def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = []
    middle = []
    right = []
    
    for value in arr:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        elif value == pivot:
            middle.append(value)
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2

    left = mergesort(arr[middle:])
    right = mergesort(arr[:middle])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    indexLeft = indexRight = 0
    while len(result) < len(left) + len(right):
        print(indexLeft, len(left), indexLeft >= len(left), indexRight, len(right), indexRight >= len(right))
        if indexRight >= len(right):
            result += left[indexLeft:]
            break

        if indexLeft >= len(left):
            result += right[indexRight:]
            break

        if left[indexLeft] <= right[indexRight]:
            result.append(left[indexLeft])
            indexLeft += 1
        else:
            result.append(right[indexRight])
            indexRight += 1
    return result

# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    sizes = [100]  
    for size in sizes:
        test_array = [random.randint(1, 100) for _ in range(size)]
        
        print(f"\nOriginal array (first 10 elements of {size}):")
        print(test_array[:10])  
        
        start = time.time()
        sorted_array_quicksort = quicksort(test_array.copy())
        end_time = time.time() - start
        print(f"Quicksort on {size} elements took: {end_time:.5f} seconds.")
        print("First 10 elements after Quicksort:", sorted_array_quicksort[:10])
        
        start = time.time()
        sorted_array_mergesort = mergesort(test_array.copy())
        end_time = time.time() - start
        print(f"Mergesort on {size} elements took: {end_time:.5f} seconds.")
        print("First 10 elements after Mergesort:", sorted_array_mergesort[:10])
