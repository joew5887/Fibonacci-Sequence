from functools import cache


@cache
def fibonacci_recursive(n_term: int) -> int:
    if n_term < 0:
        raise ValueError("Cannot have a negative term!")

    if n_term == 0 or n_term == 1:
        return n_term

    return fibonacci_recursive(n_term - 1) + fibonacci_recursive(n_term - 2)


def fibonacci_iterative(n_term: int) -> int:
    if n_term < 0:
        raise ValueError("Cannot have a negative term!")

    if n_term == 0 or n_term == 1:
        return n_term

    n_1 = 1
    n_2 = 1
    output_n = 1
    for _ in range(n_term - 2):
        output_n = n_1 + n_2
        n_2 = n_1
        n_1 = output_n

    return output_n
