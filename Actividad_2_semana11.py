Arreglo= [
    [69, 6, 69],
    [444, 9, 8],
    [6689898989, 44, 96],
]


def quicksort(arr):
    if len(arr) <=2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def ordenar_fila_con_quicksort(Arreglo, fila):
    Arreglo[fila] = quicksort(Arreglo[fila])


fila_a_ordenar = 1




ordenar_fila_con_quicksort(Arreglo, fila_a_ordenar)
for fila in Arreglo:
    print(fila)