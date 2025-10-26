from __future__ import annotations
from threading import RLock

class _SingletonMeta(type):
    _instance = None
    _lock = RLock()

    def __call__(cls, *args, **kwargs):
        # double-checked locking
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class AppConfig(metaclass=_SingletonMeta):
    def __init__(self, name: str = "dev"):
        self.name = name
