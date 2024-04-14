"""Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
Если список элементов для поиска дубликатов задавался через ссылку на статью в Википедии."""

from collections import Counter
from typing import List

import requests
from bs4 import BeautifulSoup


def get_text_from_url(url: str) -> str:
    # Получаем HTML-код страницы
    response = requests.get(url)
    # Проверяем, успешно ли выполнен запрос
    if response.status_code == 200:
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # Извлекаем весь текст со страницы; метод .get_text() объединяет весь текст в одну строку
        text = soup.get_text(separator=' ', strip=True)
        return text
    else:
        return "Ошибка загрузки страницы"


def find_duplicate_words(text: str) -> List[str]:
    words = text.lower().split()
    word_count = Counter(words)
    duplicate_words = [word for word, count in word_count.items() if count > 1]

    return duplicate_words


# Пример использования: пользователь вводит URL статьи Википедии
user_input_url = input("Введите URL статьи Википедии: ")
text_from_url = get_text_from_url(user_input_url)

if text_from_url != "Ошибка загрузки страницы":
    found_duplicates = find_duplicate_words(text_from_url)
    print("Дубликаты слов в тексте:", found_duplicates)
else:
    print(text_from_url)
