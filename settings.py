"""
   Created by: Naina Maharjan
   Created on: 2024-07-27
"""
import os

def get_absolute_path_for_resource_files(target_file):
    # Current directory
    current_directory = os.getcwd()
    # Trace back to a certain directory
    target_directory = os.path.join(current_directory, 'resources', target_file)
    # Get the absolute path of the target directory
    target_directory = os.path.abspath(target_directory)
    return target_directory


EMBEDDINGS_MODEL_NAME = "BAAI/bge-base-en-v1.5"
LLM_MODEL_NAME = "gpt-3.5-turbo"
API_ENDPOINT = "http://localhost:8001/query"
CSV_FILE = get_absolute_path_for_resource_files("Covid Data.csv")
ROWS_TO_ADD = 1000
KEY = os.environ.get("API_KEY")
API_KEY = KEY