from google.cloud import storage

def download_audio_from_storage(bucket_name: str, blob_file_name: str) -> bytes:
    
    
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_file_name)
    
    content = blob.download_as_bytes()

    return content