import os 

from dotenv import load_dotenv
from enum import Enum

load_dotenv()

class ConfigKeys(Enum):
    
    openai_key = os.environ["OPENAI_API_KEY"]


class AiModelSettings(Enum):
    
    model_max_tokens=150,
    model_temperature=0.7
    openai_model = "gpt-3.5-turbo-0125"
