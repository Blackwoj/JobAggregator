import requests
from bs4 import BeautifulSoup
import re
import os
import json
from urllib.parse import urlparse


def get_html(url, local=True):
    if local:
        try:
            with open(url, 'r') as file:
                html_content = file.read()
                return html_content
        except FileNotFoundError:
            print("HTML file not found.")
        except Exception as e:
            print("An error occurred while trying to read the HTML file:", e)
    else:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print("An error occurred while fetching the page:", e)
            return None


def save_to_file(text, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
        print("Displayed texts saved to file:", file_name)
    except IOError as e:
        print("An error occurred while saving to file:", e)


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


def create_json(file_name, text):
    text_info = {
        "filename": file_name,
        "text": text
    }
    return text_info


def website_name(url):
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc
    return netloc.replace(".", "_")



def extract_from_website(url):
    file = get_html(url, local=False)
    if file:
        raw_text = extract_texts_from_html(file)
        name = website_name(url)
        json_text = create_json(name, raw_text)
    return json_text


def extract_from_file(file, name):
    raw_text = extract_texts_from_html(file)
    json_text = create_json(name, file)
    return json_text

#Usage

# import html_cleaner

# website_json = html_cleaner.extract_from_website('https://jobs.volvogroup.com/job/G%C3%B6teborg-Senior-DevSecOps-Engineer-417-56/978075555/?feedId=361555')
