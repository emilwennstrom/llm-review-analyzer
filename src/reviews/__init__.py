import pandas as pd
import os
import re
import logging

STORAGE_BUCKET = os.getenv('BUCKET')
LOCATION = os.getenv('LOCATION')
PROJECT = os.getenv('PROJECT')

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')