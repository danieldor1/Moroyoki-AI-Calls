import threading
import logging
import os
import base64
import json
import simple_websocket
import audioop
import time
import uuid

from twilio.rest import Client
from flask import Flask, send_from_directory, redirect
from flask_sock import Sock

from modules.call_sessions import _TwilioCallSession
from modules.conversation import CallJobCreator
from modules.config.settings import ConfigKeys
from modules.schemas.data_models import CallRequestDataSchema


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

connections = []
new_connections = []

@app.route('/call_status', methods=["POST"])
def call_status_endpoint_receiever():
    pass


@app.route('/create_call', methods=["POST"])
async def create_job_sequence(incoming_request:CallRequestDataSchema):
    connections.append(new_connections)
    return{}

@app.route('/incoming' , methods=["POST"])
def incoming_voice():
    return XML_MEDIA_STREAM

@socket.route('/audio_stream/<session_id>/', websocket=True)
async def media_stream(ws, session_id):
    session = _TwilioCallSession(
        ws=ws,    )
    return[]