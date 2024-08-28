#!/usr/bin/env python3
"""A module that contains a redis class"""

from typing import Union, Callable, Optional
from uuid import uuid4
import redis


def count_calls(method: Callable) -> Callable:
    """
    Counts the amount of times methods of the Cache class are called
    """
    key = method.__qualname__

    @wraps(method)
    def wrap(self, *args, **kwargs):
        """
        Wrapper function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrap


class Cache:
    """
    A Class that defines a cache
    """
    def __init__(self):
        """
        Stores a method of redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in the cache
        """
        randomkey = str(uuid4())
        self._redis.set(randomkey,data)
        return randomkey

    def get(self, key :str, 
            fn: Optional[Callable] = None) -> Union[str, bytes, int,float]:
        """
        Converts data to desired format
        """
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        """
        Parametrize Cache.get with the correct conversion function
        """
        val = self._redis.get(key)
        return val.decode("utf-8")


    def get_int(self, key: str) -> str:
        """
        Parametrize Cache.get with the correct conversion function
        """
        val = self.redis.get(key)
        try:
            val = int(value.decode("utf-8"))
        except Exception:
            val = 0
        return val
