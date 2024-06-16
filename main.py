from pathlib import Path
from Llama3.Llama3Model import Llama3Model
from text_samples.SamplesReader import SamplesReader
import hashlib
from database.MongoDB_MAnager import DbManager

def calculate_hash(text):
    hasher = hashlib.sha256()
    hasher.update(text.encode('utf-8'))
    return hasher.hexdigest()


base_folder_path = Path(__file__).resolve().parent
sample_text_folder = base_folder_path / "Samples"


if __name__ == "__main__":
    text_classification_model = Llama3Model()
    text_reader = SamplesReader()
    db_manager = DbManager()

    sample_text = text_reader.read_json_file()

    for text in sample_text:
        if db_manager.check_duplicate(text, ["job_offer_url"])
        text["job_offer_url"]
        text["cleaned_html"]
