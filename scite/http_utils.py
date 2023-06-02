# -*- coding: utf-8 -*-
import requests
from ratelimit import limits, sleep_and_retry  # type: ignore


@sleep_and_retry
@limits(calls=40, period=60)
def remote_call(
    endpoint: str,
    url: str = "https://api.scite.ai",
    payload: dict = {},
    params: dict = {},
) -> requests.Response:
    """Make a generic GET request with ratelimits applied."""
    response = requests.get(f"{url}/{endpoint}", json=payload, params=params)
    response.encoding = "UTF-8"
    response.raise_for_status()
    return response
