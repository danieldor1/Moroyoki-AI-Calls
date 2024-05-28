
from twilio.rest import Client
from flask import Flask, jsonify, request
from flask_sock import Sock

from modules.call_sessions import TwilioCallSession
from config.settings import ConfigKeys


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