import time


def time_count(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} time: {(end - start) * 1000} ms")
        return res

    return wrapper


@time_count
def lucky_number() -> int:
    count_lucky_number = 0
    for a1 in range(10):
        for a2 in range(10):
            sum_a = a1 + a2
            for b1 in range(10):
                for b2 in range(10):
                    sum_b = b1 + b2
                    if abs(sum_a - sum_b) <= 9:
                        count_lucky_number += 10 - abs(sum_a - sum_b)
    return count_lucky_number


if __name__ == '__main__':
    print(lucky_number())


