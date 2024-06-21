import os 

from dotenv import load_dotenv
from enum import Enum

load_dotenv()

class ConfigKeys(Enum):
    
    openai_key = os.environ["OPENAI_API_KEY"]
    twilio_sid = os.environ["TWILIO_ACCOUNT_SID"]
    twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    twilio_phone_number = os.environ["TWILIO_PHONE_NUMBER"]
    azure_api_key = os.environ["AZURE_SPEECH2TEXT_API_KEY"]
    azure_region = os.environ["AZURE_SPEECH2TEXT_REGION"]
    CHAT_OPENAI_MODEL = "gpt-3.5-turbo-0125"

class SpeechRecognitionSettings(Enum):

    chunk_size = 1024
    sample_rate = 8000
    sample_width = 2
    recognizer_energy_threshold = 500
    recognizer_pause_threshold = 2
    recognizer_dynamic_energy_threshold = False
    tmp_name = "mic.wav"
    mic_capture_format = "wav"
