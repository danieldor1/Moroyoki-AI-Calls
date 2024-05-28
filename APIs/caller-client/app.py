import requests

from twilio.rest import Client
from flask import Flask, jsonify, request
from flask_sock import Sock
from http import HTTPStatus

from modules.call_sessions import TwilioCallSession
from modules.conversation import CallJobCreator
from modules.config.settings import ConfigKeys
from modules.schemas.data_models import CallRequestDataSchema
from modules.config.enums import RequestInformationCodes


TWILIO_ACCOUNT_SID = ConfigKeys.twilio_sid.value
TWILIO_AUTH_TOKEN = ConfigKeys.twilio_auth_token.value



XML_MEDIA_STREAM = """
<Response>
    <Start>
        <Stream name="Audio Stream" url="wss://------/audiostream/{connection_id}" />
    </Start>
    <Pause length="60"/>
</Response>

"""



app = Flask(__name__)
socket = Sock(app=app)
client = Client(
    account_sid = TWILIO_ACCOUNT_SID, 
    password= TWILIO_AUTH_TOKEN)


import requests

URL_FUNCTION_CREATOR_OF_METADATA = ""

import uuid
from pydantic import ValidationError
from typing import Dict, Any


def create_unique_id()->str:
    return str(uuid.uuid4())

def validate_request_data(data: Dict[str, Any]) -> CallRequestDataSchema:
    return CallRequestDataSchema(**data)

def create_job_sequence_in_the_backend(
        data_to_send:list[dict[str, Any]], 
        url: str):

    try:

        response = requests.post(
            url=url,
            data=data_to_send,
            timeout=2
        )

        response.raise_for_status()

        if response.ok:
            return HTTPStatus.ACCEPTED
        
        else: 
            return HTTPStatus.BAD_REQUEST
    
    except requests.exceptions.HTTPError:
        return HTTPStatus.BAD_REQUEST
    except requests.exceptions.ConnectionError:
        return HTTPStatus.SERVICE_UNAVAILABLE
    except requests.exceptions.Timeout:
        return HTTPStatus.REQUEST_TIMEOUT
    except requests.exceptions.RequestException:
        return HTTPStatus.INTERNAL_SERVER_ERROR




@app.route('/call_status', methods=["POST"])
def call_status_endpoint_receiever():
    pass



@app.route('/incoming' , methods=["POST"])
def incoming_voice():
    return XML_MEDIA_STREAM

@socket.route('/audio_stream/<session_id>/', websocket=True)
async def media_stream(ws, session_id):
    session = TwilioCallSession(
        ws=ws,    
        client=client,
        )
    session.start_session
    return[]