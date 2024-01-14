import doctest


def calculate_power(base, exponent):
    """
    функция возведения числа в степень
    :param base: число
    :param exponent: степень
    :return: result
    >>> calculate_power(2, 3)
    8
    >>> calculate_power(3, 5)
    243
    """
    result = 1
    for _ in range(exponent):
        result *= base
    return result


def fib(n):
    """
    функция вычисления числа Фибоначчи через рекурсию
    :param n: число
    :return: result
    >>> fib(3)
    2
    >>> fib(5)
    5
    >>> fib(11)
    89
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fibo(n):
    """
    функция вычисления числа Фибоначчи
    :param n: число
    :return: result
    >>> fibo(3)
    2
    >>> fibo(5)
    5
    >>> fibo(12)
    144
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_prime(num):
    """
    функция проверки числа на простоту
    :param num: число
    :return: bool
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(9)
    False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def count_prime_numbers(n):
    """
    функция вычисления количества простых чисел до n
    :param n: число
    :return: result
    >>> count_prime_numbers(10)
    4
    >>> count_prime_numbers(15)
    6
    >>> count_prime_numbers(20)
    8
    >>> count_prime_numbers(25)
    9
    """
    return len(list(filter(is_prime, range(2, n))))


if __name__ == '__main__':
    doctest.testmod(verbose=True)
