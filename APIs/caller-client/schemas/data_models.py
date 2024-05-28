from pydantic import BaseModel


class RequestSchemaOutput(BaseModel):
    conversation_history: list[str]


