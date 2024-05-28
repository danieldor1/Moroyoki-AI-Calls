import uuid

from twilio.rest import Client

XML_MEDIA_STREAM = """
<Response>
    <Start>
        <Stream name="Audio Stream" url="wss://examplews.org/audio_stream/{session_id}/" />
    </Start>
    <Pause length="60"/>
</Response>
"""

URL = """"""

class CallJobCreator():

          def __init__(
                    self,
                    twilio_client: Client,
                    request_metadata: list[dict]
                    ):
                    self.twilio_client = twilio_client
                    self.request_metadata = request_metadata



          def start_call(self, call_destination_number:str)->None:

                    session_id = str(uuid.uuid4())  # Generar un ID para la llamada/splocitud
                    
                    self.twilio_client.calls.create(
                    twiml=XML_MEDIA_STREAM.format(session_id=session_id),
                    to=call_destination_number,
                    from_=self.from_phone,
                    status_callback=URL+"/voice/status",
                    status_callback_method="POST",
                    timeout=10
                    )
          


          def create_conversation_job_metadata_in_the_backend(self):
                  pass