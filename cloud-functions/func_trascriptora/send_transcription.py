import requests
import json

def send_transcription_to_cloud_function(
    transcript: str, 
    user_id: str,
    conversation_id: str,
    url: str) -> None:
    
    data = {
        'transcript': transcript, 
        'user_id': user_id, 
        'conversation_id': conversation_id
        }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        raise TranscriptionError(f"Error sending transcript to Cloud Function: {e}") from e