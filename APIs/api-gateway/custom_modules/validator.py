from typing import Dict, Any, AnyStr
from schemas.data import CallRequestDataSchema

def validate_request_data(data: Dict[AnyStr, Any]) -> CallRequestDataSchema:
    return CallRequestDataSchema(**data)

