from pydantic import BaseModel


class RequestSchemaOutput(BaseModel):
    
    conversation_history: list[str]


class CallRequestDataSchema(BaseModel):
    
    user_id: str
    call_destination_number: str
    date_request: str
    time_request: str
    costumer_name: str
    details_request: str
    general_instruction: str
    init_phrase: str

