#!/usr/bin/env python3
"""
This module defines the Cache class for storing data in Redis.
"""

import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    """
    Cache class for storing data in Redis.
    """

    def __init__(self):
        """
        Initialize a new Cache instance.

        This method initializes a Redis client and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.
                This can be of type str, bytes, int, or float.

        Returns:
            str: The randomly generated key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, bytes, int, float]]:
        """
        Retrieve data from Redis
        using the given key and optional conversion function.

        Args:
            key (str): The key to look up in Redis.
            fn (Optional[Callable]):
            A callable to convert the data back to the desired format.

        Returns:
            Optional[Union[str, bytes, int, float]]:
            The retrieved data, optionally converted.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value from Redis using the given key.

        Args:
            key (str): The key to look up in Redis.

        Returns:
            Optional[str]: The retrieved string value,
            or None if the key does not exist.
        """
        data = self.get(key, fn=lambda d: d.decode('utf-8'))
        return data if isinstance(data, str) else None

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis using the given key.

        Args:
            key (str): The key to look up in Redis.

        Returns:
            Optional[int]: The retrieved integer value,
            or None if the key does not exist.
        """
        data = self.get(key, fn=int)
        return data if isinstance(data, int) else None
