import doctest


def select_sort(array):
    """
    Сортировка выбором

    >>> select_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(array)

    for index in range(n - 1):
        min_num = index
        for j in range(index + 1, n):
            if array[j] < array[min_num]:
                min_num = j
        array[index], array[min_num] = array[min_num], array[index]
    return array

def heapify(arr, n, i):
    """
    Функция heapify для пирамидальной сортировки
    """
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def HeapSort(arr):
    """
    Пирамидальная сортировка
    >>> HeapSort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

if __name__ == "__main__":
    doctest.testmod()
