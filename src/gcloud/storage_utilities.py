from . import * 

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
        print(blob)


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