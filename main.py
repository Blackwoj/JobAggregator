from pathlib import Path
from Llama3.Llama3Model import Llama3Model
from text_samples.SamplesReader import SamplesReader
import hashlib
from database.MongoDB_MAnager import DbManager
import logging
import datetime
logging.basicConfig(encoding='utf-8', level=logging.INFO)


def calculate_hash(text):
    hasher = hashlib.sha256()
    hasher.update(text.encode('utf-8'))
    return hasher.hexdigest()


base_folder_path = Path(__file__).resolve().parent
sample_text_folder = base_folder_path / "Samples"
unprocessed_file = {}
if __name__ == "__main__":
    text_classification_model = Llama3Model()
    text_reader = SamplesReader()
    sample_text = text_reader.read_json_file()
    db_manager = DbManager()
    for text in sample_text:
        offer_hash = calculate_hash(text["cleaned_html"])
        text["hash_id"] = offer_hash
        if not db_manager.check_duplicate(text, ["job_offer_url"]):
            text["processing_date"] = datetime.date.today().strftime("%d/%m/%Y")
            if db_manager.check_hash(text, offer_hash):
                logging.info("Hash exist!")
                continue
            db_manager.delete_record({"job_offer_url": text["job_offer_url"]})
        model_output = None
        try:
            model_output = text_classification_model.classify_offer(text["cleaned_html"])
        except Exception:
            logging.info("Tokens are out!!!!")

        if model_output:
            try:
                text.update(model_output)
                db_manager.add_docs(text)
                logging.info("Offer pushed to mongodb!")
            except Exception as e:
                logging.error("Something went wrong: %s! Here is model output: %s", e, model_output)