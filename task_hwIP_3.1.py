"""Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов."""

from typing import List


def find_duplicates(numbers: List[int]) -> List[int]:
    # Словарь для подсчета вхождений каждого элемента
    element_count: dict[int, int] = {}
    # Результат — список без дубликатов, содержащий только те элементы, что встретились более 1 раза
    duplicates: List[int] = []

    # Подсчет вхождений каждого элемента в исходном списке
    for element in numbers:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    # Отбор элементов, которые встречаются более одного раза
    for element, count in element_count.items():
        if count > 1:
            duplicates.append(element)

    return duplicates


# Пример использования
numbers_example = [1, 2, 3, 4, 2, 5, 3, 1, 6, 7, 8, 2]
print(find_duplicates(numbers_example))
