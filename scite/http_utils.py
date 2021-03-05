# -*- coding: utf-8 -*-
import requests
from ratelimit import limits, sleep_and_retry


@sleep_and_retry
@limits(calls=40, period=60)
def remote_call(
    endpoint: str,
    url: str = "https://api.scite.ai",
    payload: dict = {},
    params: dict = {},
):
    """Make a generic GET request with ratelimits applied."""
    r = requests.get(f"{url}/{endpoint}", json=payload, params=params)
    r.encoding = "UTF-8"
    return r.json()
