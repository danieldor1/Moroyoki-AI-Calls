from retry import retry
from google.cloud import storage
from pathlib import Path
from google.api_core.exceptions import  GoogleAPICallError, NotFound, Forbidden
from exceptions import AudioDownloaderError
from constants import ConfigConstans 

google_client_secret_file_name = ConfigConstans.google_client_secret_file_name.value

client_secrets_file = Path(__file__).parent / google_client_secret_file_name


@retry(tries=2, delay=2, backoff=2)
def download_audio_from_storage(bucket_name: str, blob_file_name: str) -> bytes:

    try:

        client = storage.Client.from_service_account_json(json_credentials_path=client_secrets_file)
        bucket = client.bucket(bucket_name)
        blob = bucket.get_blob(blob_file_name)
        content = blob.download_as_bytes()
        return content
    
    except (NotFound, Forbidden, GoogleAPICallError, AudioDownloaderError):
        raise AudioDownloaderError

