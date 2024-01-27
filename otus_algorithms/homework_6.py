import time
import random as ran


def time_count(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} time: {(end - start) * 1000} ms")
        return res

    return wrapper


@time_count
def buble_sort(array):
    """
    Cортировка пузырьком
    """
    n = len(array)
    for i in range(n - 1):
        count = 0
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                count += 1
        if count == 0:
            break
    return array


@time_count
def insert_sort(array):
    """
    Сортировка вставкой
    """
    n = len(array)

    for i in range(1, n):
        elem = array[i]
        j = i

        while j >= 1 and array[j - 1] > elem:
            array[j] = array[j - 1]
            j -= 1
        array[j] = elem

    return array

@time_count
def shell_sort(array):
    """
    Сортировка Шелла
    """
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2
    return array


if __name__ == '__main__':
    size_array = 100, 1000, 10000
    for size in size_array:
        random_array = [ran.randint(1, 20000) for _ in range(size)]
        print(f"size_array = {size}")
        buble_sort(random_array)
        insert_sort(random_array)
        shell_sort(random_array)
