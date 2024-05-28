from enum import Enum

class RequestDetailsKeys(Enum):
    date = "date_request"
    time = "time_request"
    costumer = "costumer_name"
    details = "special_details_request"
    instruction = "general_instruction"

class OpenaiConstants(Enum):
    
    role = 'role'
    system = 'system'
    content = 'content'
    user = 'user'
    assistant = 'assistant'
    
