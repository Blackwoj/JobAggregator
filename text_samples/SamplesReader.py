from pathlib import Path
import logging
import json
from ..textProcessing.html_cleaner import extract_texts_from_html

class SamplesReader:

    def __init__(self, files_path_location: Path = Path(__file__).resolve().parent.parent / "samples"):
        self._files_path_location = files_path_location

    def read_files(self) -> dict[str, str]:
        all_txt_files = self._files_path_location.glob('*.txt')

        all_texts = {}  # Lista przechowująca zawartość wszystkich plików tekstowych

        for txt_file in all_txt_files:
            with open(txt_file, 'r', encoding='utf-8') as file:
                text = file.read()  # Odczytaj zawartość pliku tekstowego
                all_texts[txt_file.name] = text
        if not all_texts:
            logging.warning("No text in passed location: %s", self._files_path_location)
        return all_texts

    def read_json_file(self) -> list[dict[str, str]]:
        all_json_files = self._files_path_location.glob("*.json")
        all_text = []

        for json_file in all_json_files:
            with json_file.open('r', encoding='utf-8') as file:
                reader_json = json.load(file)
                for i in range(len(reader_json)):
                    if reader_json[i]["career_site"] != "not found":
                        all_text.append(self.clear_html(reader_json[i]))
        if not all_text:
            logging.warning("No text in passed location: %s", self._files_path_location)
        return all_text

    def clear_html(self, offer: dict[str, str]):
        cleaned_offer = offer["cleaned_html"]
        offer["cleaned_html"] = extract_texts_from_html(cleaned_offer)
        return offer
