#!/usr/bin/env python3
"""
A module with tools for request caching and tracking.
"""

import redis
import requests
from functools import wraps
from typing import Callable

# Create a Redis instance
redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """
    Caches the output of fetched data and tracks the number of accesses.
    """
    @wraps(method)
    def invoker(url: str) -> str:
        """
        Wrapper function for caching the output.
        """
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """
    Returns the content of a URL after caching the request's response,
    and tracking the request.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    test_url = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://www.\
example.com"
    print(get_page(test_url))
    print(get_page(test_url))
    print(redis_store.get(f'count:{test_url}').decode('utf-8'))
