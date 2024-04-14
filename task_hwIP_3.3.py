"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака."""

from typing import Dict, List

# Тип для предметов и их веса
Items = Dict[str, float]
# Тип для списка предметов
PackingList = List[str]


def find_combinations(items_find: Items, max_weight_find: float) -> List[PackingList]:
    """Находит все возможные комбинации вещей, которые могут быть упакованы в рюкзак."""
    all_combinations = []
    current_combination = []

    def backtrack(remaining_items: List[str], current_weight: float) -> None:
        if current_weight <= max_weight_find:
            all_combinations.append(current_combination.copy())
        for i in range(len(remaining_items)):
            item = remaining_items[i]
            weight = items_find[item]
            if current_weight + weight <= max_weight_find:
                current_combination.append(item)
                backtrack(remaining_items[i + 1:], current_weight + weight)
                current_combination.pop()

    backtrack(list(items_find.keys()), 0)
    return all_combinations


# Пример использования
items = {
    "Палатка": 2.5,
    "Спальник": 1.5,
    "Котелок": 0.5,
    "Фонарик": 0.2,
    "Еда": 2.0,
    "Вода": 3,
    "Карта": 0.2,
    "Аптечка": 0.5
}
max_weight = 4.0

combinations = find_combinations(items, max_weight)
for i, combination in enumerate(combinations, start=1):
    print(f"Комбинация {i}: {combination}")
