import os
from dotenv import load_dotenv
load_dotenv()

ollama_url = os.getenv('OLLAMA_URL')
location = os.getenv('LOCATION')
project = os.getenv('PROJECT')

