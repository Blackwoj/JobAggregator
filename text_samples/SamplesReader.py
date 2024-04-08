from pathlib import Path
import logging


class SamplesReader:

    def __init__(self, files_path_location: Path = Path(__file__).resolve().parent / "samples"):
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
