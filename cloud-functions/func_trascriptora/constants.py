import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()


class InvocatorKeyManager(Enum):

    azure_api_key = os.environ['AZURE_SPEECH_KEY']

class ConfigConstans(Enum):
    
    target_cloud_function_url = ""
    google_client_secret_file_name = "client_secret.json"
    azure_service_region = ""
    azure_recognition_language = ""
