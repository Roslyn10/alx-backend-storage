#!/usr/bin/env python3
"""A module that can be used as a web cache and tracker"""

import redis
from functools import wraps
import requests


def cache_page(method):
    """
    Decorator to cache the page content with an expiration time
    """
    def decorator(fn):

        @wraps(fn)
        def wrap(url: str) -> str:
            cached_content = redis_clinet.get(f"cache: {url}")
            if cached_content:
                print("Cache hit")
                return cached_content.decode("utf-8")

            content = fn(url)
            redis_client.incr(f"cache:{url}")
            return content
        return wrap
    return decorator


@cache_page
def get_page(url: str) -> str:
    """
    Returns the HTML content of the url
    """
    result = requests.get(url)
    return result.text
