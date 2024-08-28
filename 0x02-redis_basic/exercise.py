#!/usr/bin/env python3
"""A module that contains a redis class"""

from typing import Union, Callable, Optional
from uuid import uuid4
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Counts the amount of times methods of the Cache class are called
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Returns the history of the input params to one list in redis, and stores
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper

def replay(fn: Callable):
    """
    Displays the history of calls
    """
    red = redis.Redis()
    func = fn.__qualname__
    call = red.get(func_name)
    try:
        call = int(call.decode("utf-8"))
    except Exception:
        call = 0
    print("{} was called {} times:".format(func, call))
    inputs = red.lrange("{}:inputs".format(func), 0, 1)
    outputs = red.lrange("{}:outputs".format(func), 0, -1)
    for inpu, outpu in zip(inputs, outputs):
        try:
            inpu = inpu.decode("utf-8)"
        except Exception:
            inpu = ""
        try:
            outpu = outpu.decode("utf-8")
        except Exception:
            outpu = ""
        print("{}(*{}) -> {}".format(func, inpu, outpu))



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

    @call_history
    @count_calls
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
