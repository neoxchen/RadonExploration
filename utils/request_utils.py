from typing import Tuple

import requests


def _recommend_request(url: str) -> Tuple[requests.Response, str]:
    """
    A simple recommend request to the target URL

    Args:
        url (str): the full URL to send the request to

    Returns:
        (Tuple[requests.Response, str]) tuple of (response, echoed URL)
    """
    return requests.get(url=url), url
