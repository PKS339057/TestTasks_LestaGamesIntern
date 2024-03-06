from typing import Callable


def example_isEven(value: int) -> bool:
    return value % 2 == 0


def my_isEven(value: int) -> bool:
    return value & 1 == 0


def print_result(func: Callable, value: int) -> None:
    try:
        result = "Чётное" if func(value) else "Нечётное"
    except Exception:
        return print(f"При выполнении функции {func.__name__} возникла ошибка")
    print(f"Результат функции {func.__name__}: число {value} {result.lower()}")


if __name__ == "__main__":
    test_value = int(input("Введите число, которое хотите проверить на чётность: "))
    for f in (example_isEven, my_isEven):
        print_result(f, test_value)
