import  doctest

def demucron_algorithm(A):
    """
    алгоритм Демюкрона
    :param A: вектор смежности в виде массива
    :return: результат сортировки
    >>> demucron_algorithm([[1, 2], [2, 3], [], [4], [3]])
    [[0], [1], [2]]
    """
    N = len(A)

    in_degree = [0] * N
    queue = []
    result = []

    for i in range(N):
        for j in A[i]:
            in_degree[j] += 1

    for i in range(N):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        level = []
        for _ in range(len(queue)):
            vertex = queue.pop(0)
            level.append(vertex)

            for item in A[vertex]:
                in_degree[
                    item] -= 1
                if in_degree[item] == 0:
                    queue.append(
                        item)

        result.append(level)
    return result


if __name__ == '__main__':
    doctest.testmod(verbose=True)