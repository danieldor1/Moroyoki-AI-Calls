import functions_framework

from  constants import ConfigConstans
from audio_downloader import download_audio_from_storage
from vox2text import transcribe_audio
from send_transcription import send_transcription_to_cloud_function

TARGET_CLOUD_FUNCTION_URL = ConfigConstans.target_cloud_function_url.value

@functions_framework.cloud_event
def hello_gcs(cloud_event):
    
    data = cloud_event.data
    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket_name = data["bucket"]
    file_name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    if not all((
        bucket_name,    
        file_name, 
        )):
        
        raise ValueError("Missing required environment variables")

    audio_data = download_audio_from_storage(bucket_name, file_name)
    transcript = transcribe_audio(audio_data)

    if transcript:
        send_transcription_to_cloud_function(transcript, TARGET_CLOUD_FUNCTION_URL)
    else:
        print("Transcription result is empty")
    