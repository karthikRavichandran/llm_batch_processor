import pandas as pd
from llm_batch_processor.api_client import OpenAIClient
from llm_batch_processor.get_prompt import base_prompt
from llm_batch_processor.config import CONFIG
from tqdm import tqdm


class BatchProcessor:
    def __init__(self):
        self.client = OpenAIClient()
        self.prompt_template = self.load_prompt()

    def load_prompt(self):
        """Reads the prompt from a text file."""
        try:
            with open(CONFIG["PROMPT_FILE"], "r", encoding="utf-8") as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"Error: Prompt file '{CONFIG['PROMPT_FILE']}' not found.")
            print(f"Warning !!! Using Default prompt : {base_prompt}")
            return base_prompt + ": {text}"

    def process_batch(self, batch):
        """Process a batch of text rows and return responses"""
        responses = []
        for text in batch:
            base_prompt = self.prompt_template.replace("{text}", text)
            prompt = f"{base_prompt}: {text}"
            response = self.client.get_response(prompt)
            responses.append(response)
        return responses

    def process_csv(self):
        """Reads input CSV, processes in batches, and writes output"""
        df = pd.read_csv(CONFIG["INPUT_CSV"])

        # Ensure response column exists
        if CONFIG["RESPONSE_COLUMN"] not in df.columns:
            df[CONFIG["RESPONSE_COLUMN"]] = None

        for start in tqdm(range(0, len(df), CONFIG["BATCH_SIZE"])):
            end = start + CONFIG["BATCH_SIZE"]
            batch = df.loc[start:end - 1, CONFIG["TEXT_COLUMN"]].tolist()
            responses = self.process_batch(batch)
            df.loc[start:end - 1, CONFIG["RESPONSE_COLUMN"]] = responses
            print(f"Processed rows {start} to {end - 1}")

            df.to_csv(CONFIG["OUTPUT_CSV"], index=False)
            print(f"Processing complete. Output saved to {CONFIG['OUTPUT_CSV']}")
