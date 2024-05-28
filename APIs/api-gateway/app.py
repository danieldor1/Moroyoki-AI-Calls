import requests
from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)


@app.route('/create_call', methods=["POST"])
async def create_job_sequence():

    try:
        data = request.get_json()
        call_request_data = validate_request_data(data)
        unique_id = create_unique_id()

        call_request_dict = call_request_data.model_dump()
        call_request_dict['unique_id'] = unique_id
        
        response_from_backend = create_job_sequence_in_the_backend(
        data_to_send=call_request_dict,
        url=URL_FUNCTION_CREATOR_OF_METADATA)

        #if the information is created the func create job will return a 200 code
    
        if response_from_backend == HTTPStatus.ACCEPTED:
            returned_message_to_requester_client = RequestInformationCodes.request_acepted.value
        else:
            returned_message_to_requester_client = RequestInformationCodes.request_denied.value
        
        response = jsonify({"Code": returned_message_to_requester_client})
        return response
    
    except ValidationError:
        return jsonify({"code": RequestInformationCodes.request_denied.value})
    
    except Exception:
        return jsonify({"code": RequestInformationCodes.server.value})



