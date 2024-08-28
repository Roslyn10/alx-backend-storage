#!/usr/bin/env python3
"""A module that contains a redis class"""

from typing import Union
from uuid import uuid4
import redis



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
