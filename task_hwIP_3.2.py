"""В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку."""

import re
from collections import Counter
from typing import List, Tuple

import requests
from bs4 import BeautifulSoup

MAX_WORDS: int = 10


def fetch_html_content(url: str) -> str:
    """Загружает HTML-контент по URL."""
    if url.startswith("http://"):
        print("Внимание: использование HTTP может быть небезопасным. Рекомендуется использовать HTTPS.")
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def extract_text_from_html(html: str) -> str:
    """Извлекает и возвращает текст из HTML-контента."""
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text(separator=' ', strip=True)


def clean_and_split_text(text_content: str) -> List[str]:
    """Очищает текст от знаков препинания и регистра, возвращает список слов."""
    cleaned_text = re.sub(r'[^\w\s]', '', text_content).lower()
    return cleaned_text.split()


def find_most_common_words(words: List[str], number_of_words: int = MAX_WORDS) -> List[Tuple[str, int]]:
    """Возвращает N самых частых слов и их количество."""
    word_counts = Counter(words)
    return word_counts.most_common(number_of_words)


if __name__ == "__main__":
    input_url = input("Введите URL или HTML-контент (рекомендуется использовать HTTPS): ")

    if input_url.startswith("http://") or input_url.startswith("https://"):
        html_content = fetch_html_content(input_url)
    else:
        html_content = input_url

    text_from_html = extract_text_from_html(html_content)
    list_of_words = clean_and_split_text(text_from_html)
    common_words_list = find_most_common_words(list_of_words)

    print("Топ-10 самых частых слов:")
    for word, count in common_words_list:
        print(f"{word}: {count}")
