from pathlib import Path
from Llama3.Llama3Model import Llama3Model
from text_samples.SamplesReader import SamplesReader
import hashlib
from database.MongoDB_MAnager import DbManager
from logging import getLogger
logger = getLogger(__name__),

def calculate_hash(text):
    hasher = hashlib.sha256()
    hasher.update(text.encode('utf-8'))
    return hasher.hexdigest()


base_folder_path = Path(__file__).resolve().parent
sample_text_folder = base_folder_path / "Samples"

if __name__ == "__main__":
    # text_classification_model = Llama3Model()
    text_reader = SamplesReader()
    sample_text = text_reader.read_json_file()
    db_manager = DbManager()
    i = 1
    for text in sample_text:
        if db_manager.check_duplicate(text, ["job_offer_url"]):
            offer_hash = calculate_hash(text["cleaned_html"])
            if db_manager.check_hash(text, offer_hash):
                continue
        # model_output = text_classification_model.classify_offer(text["cleaned_html"])
        # print(model_output)

