from typing import List
from itertools import chain
from time import time


def quick_sort(arr: List[int]):
    if len(arr) <= 1:
        return arr
    pivot_el = arr[0]  # может быть любой элемент массива
    less_arr, equal_arr, greater_arr = [], [], []
    for el in arr:
        if el < pivot_el:
            less_arr.append(el)
        elif el == pivot_el:
            equal_arr.append(el)
        else:
            greater_arr.append(el)
    return list(chain(quick_sort(less_arr), equal_arr, quick_sort(greater_arr)))


if __name__ == "__main__":
    elements = input("Введите элементы массива через пробел: ")
    test_arr = list(map(int, elements.split()))
    print(f"Текущий массив: {test_arr}")

    start = time()
    sorted_arr = quick_sort(test_arr)
    end = time()

    print(f"Отсортированный массив: {sorted_arr}\n"
          f"Время сортировки: {end - start}")
