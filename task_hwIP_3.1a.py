"""Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
Если список элементов вводится пользователем, например, как текст из статьи."""

from collections import Counter
from typing import List


def find_duplicate_words(text: str) -> List[str]:
    # Разбиваем текст на слова, приводим к нижнему регистру для унификации
    words = text.lower().split()
    # Используем Counter для подсчета вхождений каждого слова
    word_count = Counter(words)
    # Отбираем слова, которые встречаются более одного раза
    duplicate_words = [word for word, count in word_count.items() if count > 1]

    return duplicate_words


# Пример использования: пользователь вводит текст
user_input = input("Введите текст: ")
found_duplicates = find_duplicate_words(user_input)  # Также изменил имя переменной здесь, для ясности
print("Дубликаты слов в тексте:", found_duplicates)
