from pydantic import BaseModel, FutureDatetime, PastDatetime, UUID1
from dataclasses import dataclass

@dataclass
class CallRequestDataSchema(BaseModel):
    
    request_hash: UUID1
    call_destination_number: str
    request_creation_datetime: PastDatetime
    time_to_initate_job: FutureDatetime
    details_request: str
    general_instruction: str
    init_phrase: str

