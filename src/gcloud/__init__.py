from google.cloud import storage
import os
from dotenv import load_dotenv
load_dotenv()


STORAGE_BUCKET = os.getenv('BUCKET')
LOCATION = os.getenv('LOCATION')
PROJECT = os.getenv('PROJECT')