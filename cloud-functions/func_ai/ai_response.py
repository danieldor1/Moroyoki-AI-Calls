from typing import List
from openai import OpenAI
from settings import ConfigKeys, AiModelSettings
from constants import OpenaiConstants

OPENAI_API_KEY = ConfigKeys.openai_key.value
MODEL = AiModelSettings.openai_model.value
TEMPERATURE = AiModelSettings.model_temperature.value
MAX_TOKENS = AiModelSettings.model_max_tokens.value
ROLE = OpenaiConstants.role.value
SYSTEM = OpenaiConstants.system.value
CONTENT = OpenaiConstants.content.value
USER = OpenaiConstants.user.value
ASSISTANT = OpenaiConstants.assistant.value

client = OpenAI(
    api_key = OPENAI_API_KEY
)
class OpenAIChatCompletion:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    def get_response(self, transcript: List[str]) -> str:
        messages = [
            {ROLE: SYSTEM, CONTENT: self.system_prompt},
        ]
        for i, text in enumerate(reversed(transcript)):
            messages.insert(1, {ROLE: USER if i % 2 == 0 else ASSISTANT, CONTENT: text})
            
            
        try:
            completion = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE
            )
            return completion.choices[0].message.content

        except Exception:
            raise