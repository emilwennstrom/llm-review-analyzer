from . import * 
from google.cloud import storage
from google.cloud import translate
from io import StringIO
import pandas as pd
"""
Utilities for loading files from Google Storage Buckets

"""

def get_reviews_from_bucket(blob_name, bucket_name=STORAGE_BUCKET) -> str:
    """ Downloads a blob into memory.
    Format is foo/bar/etc.csv.
    """
    storage_client = storage.Client(project=PROJECT)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    return _decode_contents(blob=blob)

def list_blobs_in_bucket(bucket_name = STORAGE_BUCKET):
    storage_client = storage.Client(project=PROJECT)
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs()
    for blob in blobs:
        print(blob.name)
    


def add_blobs_from_bucket(bucket_name = STORAGE_BUCKET, project_id = PROJECT):
    review_list = []
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)
    blobs = list(bucket.list_blobs())

    while True:
        print("Select files to load: (press x to quit, r to reset)")
        available_blobs = [blob for blob in blobs if blob.name not in review_list]
        
        if not available_blobs:
            print("No more files available to add.")
            return review_list
        
        for index, blob in enumerate(available_blobs, start=1):
            print(f"{index}: {blob.name}")
        
        choice = input()
        if choice == 'x':
            if review_list:
                return review_list
            else:
                print("No files added")
                return None
        elif choice == 'r':
            review_list = []
            continue
        
        try:
            choice_index = int(choice) - 1
            if choice_index < 0 or choice_index >= len(available_blobs):
                print("Wrong input")
            else:
                selected_blob_name = available_blobs[choice_index].name
                if selected_blob_name not in review_list:
                    print(f"Added {selected_blob_name}")
                    review_list.append(selected_blob_name)
                else:
                    print("File already added")
        except ValueError:
            print("Please enter a valid number")
    

def _decode_contents(blob):
    """
    Try to decode the bytes downloaded from a blob using multiple encodings.
    Args:
    blob: The blob object from which to download the bytes.

    Returns:
    str: The decoded string.

    Raises:
    UnicodeDecodeError: If none of the specified encodings succeed.
    """
    contents = blob.download_as_bytes()
    encodings = ['utf-8', 'utf-16']

    last_exception = None
    for encoding in encodings:
        try:
            return contents.decode(encoding)
        except UnicodeDecodeError as e:
            last_exception = e
            continue

    raise last_exception