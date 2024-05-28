import os
import functions_framework

from typing import Dict
from audio_downloader import download_audio_from_storage
from vox2text import transcribe_audio
from send_transcription import send_transcription_to_cloud_function

AZURE_SUBS_KEY = os.environ['SPEECH_KEY']
LANGUAGE = os.environ['LANGUAGE']
TARGET_CLOUD_FUNCTION_URL = os.environ['TARGET_FUNCTION']

                         

class TranscriptionError(Exception):
    pass


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
        AZURE_SUBS_KEY, 
        LANGUAGE, 
        TARGET_CLOUD_FUNCTION_URL
        )):
        
        raise ValueError("Missing required environment variables")

    audio_data = download_audio_from_storage(bucket_name, file_name)
    transcript = transcribe_audio(audio_data, AZURE_SUBS_KEY, LANGUAGE)

    if transcript:
        send_transcription_to_cloud_function(transcript, TARGET_CLOUD_FUNCTION_URL)
    else:
        print("Transcription result is empty")
    