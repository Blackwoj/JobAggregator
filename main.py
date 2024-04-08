from pathlib import Path
from .textProcessing.TextProcessor import TextProcessor
from .model.NERTrainer import NERTrainer
from .text_samples.SamplesReader import SamplesReader
base_folder_path = Path(__file__).resolve().parent
sample_text_folder = base_folder_path / "Samples"


if __name__ == "__main__":
    text_processor = TextProcessor()
    ner_trainer = NERTrainer()
    text_reader = SamplesReader()

    sample_text = text_reader.read_files()

    tokens = text_processor.tokenize(sample_text)
    translated_text = text_processor.translate(sample_text)
