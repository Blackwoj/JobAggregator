import os
from dotenv import load_dotenv
import requests


class LLM():
    def __init__(self) -> None:
        self.labels = ['job title', 'company name', 'location', 'responsibilities', 'salary', 'required_technology', 'optional_required_technology', 'remote_or_stationary']
        self.api_model = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
        self.api_key = ""
        self.labels_prompt = f'You are a robot that only outputs JSON. you reply in JSON format with the fields {", ".join(self.labels)}'
        self.headers = {"Authorization": f'Bearer {self.api_key}'}

    def dumb_to_json():
        pass

    def query(self, payload):
        response = requests.post(self.api_model, headers=self.headers, json=payload)
        return response.json()

    def extract_data(self, raw_text):
        final_prompt = f'{self.labels_prompt} for job description: {raw_text}. Respond only as shown, with no additional discursive or explanatory text, keep the elements short, do not provide information that does not exist.'

        output = self.query({
            "inputs": f'<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n{final_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n',
            "parameters": {
                "return_full_text": False,
                "max_new_tokens": 300,
                "stop": ["<|end_of_text|>", "<|eot_id|>"]
            }
        })

        return output[0]['generated_text']

#usage
#from lama import LLM
#import html_cleaner

#website_json = html_cleaner.extract_from_website('https://jobs.volvogroup.com/job/G%C3%B6teborg-Senior-DevSecOps-Engineer-417-56/978075555/?feedId=361555')

#model = LLM()
#json = model.extract_data(website_json['text'])
#print(json)
