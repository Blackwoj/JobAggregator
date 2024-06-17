import os
from dotenv import load_dotenv
import requests
import logging
from typing import Optional
import ast
load_dotenv()


class Llama3Model:

    API_KEY = os.getenv("LLAMA_API_KEY")

    def __init__(self):
        self.model_ulr = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
        self.header = {"Authorization": f'Bearer {self.API_KEY}'}

    def _query(self, payload):
        if self.API_KEY:
            try:
                response = requests.post(self.model_ulr, headers=self.header, json=payload)
                return response.json()
            except Exception as e:
                logging.error(e)
                return
        else:
            logging.info("Missing API key in .env file!")
            return

    @property
    def classification_labels(self) -> list[str]:
        return [
            'job title',
            'company name',
            'location',
            'job-type',
            'technologies',
            'salary',
            'requirements'
        ]

    @property
    def _prompt(self):
        return f'You are a robot that only outputs JSON. you reply in JSON format with the fields {", ".join(self.classification_labels)}'

    def final_prompt(self, description):
        return ''.join([
            '{} for job description: '.format(self._prompt),
            '{}. '.format(description),
            'Respond only as shown, with no additional discursive or explanatory text.'
        ])

    def classify_offer(self, offer_des) -> Optional[dict[str, str]]:
        self.offer_description = offer_des
        output = self._query({
            "inputs": ''.join([
                '<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n',
                '{}'.format(self.final_prompt(self.offer_description)),
                '<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n',
            ]),
            "parameters": {
                "return_full_text": False,
                "max_new_tokens": 500,
                "stop": ["<|end_of_text|>", "<|eot_id|>"]
            }
        })
        if output:
            try:
                return ast.literal_eval(output[0]['generated_text'])
            except Exception as e:
                logging.error("Something occured while parsing model output: %s, %s", e, output[0]['generated_text'])
        else:
            logging.info("Model did not return value!")
