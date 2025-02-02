import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

# # OpenAI API Key
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Project_Id = os.getenv("Project_Id")
#
# # Batch size for processing
# BATCH_SIZE = 10
#
# # # Input and Output CSV File Paths
# INPUT_CSV = "data/input.csv"
# OUTPUT_CSV = "data/output.csv"
#
# # Column names
# TEXT_COLUMN = "text"  # The column that contains input text
# RESPONSE_COLUMN = "response"  # Column to store LLM responses

import os
import argparse
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

def get_config():
    parser = argparse.ArgumentParser(description="LLM Batch Processor Configuration")

    parser.add_argument("--api_key", type=str, default=os.getenv("OPENAI_API_KEY"),
                        help="OpenAI API Key (default: from environment variable)")
    parser.add_argument("--project_id", type=str, default=os.getenv("Project_Id"),
                        help="Project ID (default: from environment variable)")
    parser.add_argument("--batch_size", type=int, default=10,
                        help="Batch size for processing (default: 10)")
    parser.add_argument("--input_csv", type=str, default="data/input.csv",
                        help="Path to input CSV file (default: data/input.csv)")
    parser.add_argument("--output_csv", type=str, default="data/output.csv",
                        help="Path to output CSV file (default: data/output.csv)")
    parser.add_argument("--text_column", type=str, default="text",
                        help="Column name containing input text (default: text)")
    parser.add_argument("--response_column", type=str, default="response",
                        help="Column name for storing responses (default: response)")
    parser.add_argument("--prompt_file", type=str, default="data/prompt.txt",
                        help="Path to the text file containing the prompt")

    args = parser.parse_args()

    return {
        "OPENAI_API_KEY": args.api_key,
        "PROJECT_ID": args.project_id,
        "BATCH_SIZE": args.batch_size,
        "INPUT_CSV": args.input_csv,
        "OUTPUT_CSV": args.output_csv,
        "TEXT_COLUMN": args.text_column,
        "RESPONSE_COLUMN": args.response_column,
        "PROMPT_FILE": args.prompt_file
    }

# Load configuration when imported
CONFIG = get_config()
