import requests
import json

from retry import retry
from http import HTTPStatus


@retry(tries=3, delay=1)
def send_transcription_to_cloud_function(
    transcript: str, 
    user_id: str,
    conversation_id: str,
    url: str) -> HTTPStatus:
    
    data = {
        'transcript': transcript, 
        'user_id': user_id, 
        'conversation_id': conversation_id
        }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers, timeout=5)
        response.raise_for_status()
        
        return HTTPStatus.OK
    
    except requests.exceptions.ConnectionError:
        return HTTPStatus.SERVICE_UNAVAILABLE

    except requests.exceptions.Timeout:
        return HTTPStatus.REQUEST_TIMEOUT
    
    except requests.exceptions.HTTPError:
        return HTTPStatus.BAD_REQUEST
    
    except requests.exceptions.RequestException:
        return HTTPStatus.INTERNAL_SERVER_ERROR
    




