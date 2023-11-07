import http.client
import json
from urllib.parse import urlparse
from typing import Any
from typing import Dict
from .enviroment import BASE_URL


def request(
    method: str,
    url: str,
    data: Dict[str, str] = None,
    api_key: str = None,
    error_message: str = None,
) -> Dict[Any, Any]:
    """
    Constructs and send a request
    :param method: method for the request: 'POST' and 'GET'
    :param url: URL for the request, include params
    :param data: (optional) Dictionary to send in the body
    :param api_key: (optional) Authorization api_key for protected endpoints
    :param error_message: (optional) Custom error message

    :return: Dictionary with the response data
    """
    res = None

    # parse url
    parsed_url = urlparse(BASE_URL + url)
    base_url = parsed_url.netloc
    path = "{}".format(parsed_url.path)

    if parsed_url.query:
        path = "{}?{}".format(path, parsed_url.query)

    # connection
    conn = http.client.HTTPSConnection(base_url)
    headers = {
        "content-type": "application/json",
    }

    # add api_key if exists
    if api_key:
        headers["X-Api-Key"] = "{}".format(api_key)

    kwargs = {}  # type: Dict[str, Any]
    if data:
        kwargs["body"] = json.dumps(data)

    try:
        conn.request(method, path, headers=headers, **kwargs)
        res = conn.getresponse()

        response_data = json.loads(res.read().decode())
    except Exception:
        if error_message is None:
            error_message = f"Url may be wrong. url: {url}"
            if res:
                error_message += f" HTTP status: {res.code}"

        raise ValueError(error_message)

    return response_data


def post(url: str, data: dict, api_key: str) -> Dict[Any, Any]:
    """
    Constructs and send a POST request
    :param url: URL for the request, include params
    :param data: Dictionary to send in the body
    :param api_key: (Authorization api_key for protected endpoints

    :return: Dictionary with the response data
    """
    # check api_key
    if not api_key:
        raise ValueError("You must include a valid api_key")
    return request("POST", url, data=data, api_key=api_key)


def get(url: str, api_key: str) -> Dict[Any, Any]:
    """
    Constructs and send a GET request
    :param url: URL for the request, include params
    :param api_key: Authorization api_key for protected endpoints

    :return: Dictionary with the response data
    """
    # check api_key
    if not api_key:
        raise ValueError("You must include a valid api_key")
    return request("GET", url, api_key=api_key)
