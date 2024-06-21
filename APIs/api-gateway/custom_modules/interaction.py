import requests
from typing import Dict, Any, AnyStr, List
from retry import retry
from http import HTTPStatus

@retry(tries=3, delay=0.5)
def post_method_interaction_wrapper(
    data:List[Dict[AnyStr, Any]], 
    url: AnyStr)->AnyStr:

    try:

        response = requests.post(
                url=url,
                data=data,
                timeout=2)  
        
        response.raise_for_status()             
        
        if response.ok:
            return HTTPStatus.ACCEPTED
        else: 
            return HTTPStatus.BAD_REQUEST

    except requests.exceptions.HTTPError:
        return HTTPStatus.BAD_REQUEST
    except requests.exceptions.ConnectionError:
        return HTTPStatus.SERVICE_UNAVAILABLE
    except requests.exceptions.Timeout:
        return HTTPStatus.REQUEST_TIMEOUT
    except requests.exceptions.RequestException:
        return HTTPStatus.INTERNAL_SERVER_ERROR

