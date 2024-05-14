from google.cloud import storage
from google.cloud import translate
from dotenv import load_dotenv
import os
load_dotenv('src/.env')


STORAGE_BUCKET = os.getenv('BUCKET')
LOCATION = os.getenv('LOCATION')
PROJECT = os.getenv('PROJECT')



# Your other code here


CLIENT_OPTIONS = {"api_endpoint": "translate-eu.googleapis.com:443"}