from __future__ import annotations

from threading import RLock
from typing import Optional


class _SingletonMeta(type):
    """Thread-safe, lazy-initialized Singleton via metaclass."""

    _instance: Optional[object] = None
    _lock: RLock = RLock()

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class AppConfig(metaclass=_SingletonMeta):
    def __init__(self, name: str = "dev"):
        self.name = name


# Alternative style: module-level singleton (simple but hard to test; generally not recommended).
class _GlobalConfig:
    def __init__(self, name: str = "dev"):
        self.name = name


GLOBAL_CONFIG = _GlobalConfig()  # eager, created at import time
