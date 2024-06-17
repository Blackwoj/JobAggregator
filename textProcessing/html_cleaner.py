from bs4 import BeautifulSoup
import re


def remove_duplicate_newlines(string):
    return re.sub(r'\n{1,}', r'', string)


def remove_double_spaces(string):
    return re.sub(r' {2,}', r' ', string)


def split_elements(lst):
    new_list = []
    for element in lst:
        new_elements = [e.strip() for e in element.split('\n')]
        new_list.extend(new_elements)
    return new_list


def extract_texts_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    displayed_texts = []
    content = soup.find("body")

    for element in content.find_all(['p', 'h1', 'h2', 'b', 'em', 'li', 'div', 'i', 'u', 'ol', 'ul', 'q', 'span', 'header']):
        if not element.find_all(recursive=False):
            displayed_texts.append(remove_duplicate_newlines(element.get_text()))

    displayed_texts = split_elements(displayed_texts)
    return remove_double_spaces(' '.join(displayed_texts))
