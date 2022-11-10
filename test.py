import pytest
from fibonacci import fibonacci_iterative, fibonacci_recursive


@pytest.mark.parametrize("n_term,expected_output", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (10, 55)])
def test_terms_for_fibonacci_iterative(n_term: int, expected_output: int) -> None:
    assert fibonacci_iterative(n_term) == expected_output


@pytest.mark.parametrize("n_term,expected_output", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (10, 55)])
def test_terms_for_fibonacci_recursive(n_term: int, expected_output: int) -> None:
    assert fibonacci_recursive(n_term) == expected_output


def test_list_fibonacci_iterative() -> None:
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    output = []

    for i in range(len(expected)):
        output.append(fibonacci_iterative(i))

    assert output == expected


def test_list_fibonacci_recursive() -> None:
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    output = []

    for i in range(len(expected)):
        output.append(fibonacci_recursive(i))

    assert output == expected


if __name__ == "__main__":
    pytest.main([__file__])
