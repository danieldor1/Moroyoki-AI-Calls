import os

from typing import Dict

AZURE_SUBS_KEY = os.environ['SPEECH_KEY']
LANGUAGE = os.environ['LANGUAGE']
TARGET_CLOUD_FUNCTION_URL = os.environ['TARGET_FUNCTION']


class TranscriptionError(Exception):
    pass

def transcribe_and_send(event: Dict, context) -> None:
    try:
        bucket_name = event.get("bucket", "")
        file_name = event.get("name", "")

        if not all((bucket_name, file_name, AZURE_SUBS_KEY, LANGUAGE, TARGET_CLOUD_FUNCTION_URL)):
            raise ValueError("Missing required environment variables")

        audio_data = download_audio_from_storage(bucket_name, file_name)
        transcript = transcribe_audio(audio_data, AZURE_SUBS_KEY, LANGUAGE)
        
        if transcript:
            send_transcription_to_cloud_function(transcript, TARGET_CLOUD_FUNCTION_URL)
        else:
            print("Transcription result is empty")
    except Exception as e:
        print(f"Error during transcription or Cloud Function communication: {e}")
        raise
