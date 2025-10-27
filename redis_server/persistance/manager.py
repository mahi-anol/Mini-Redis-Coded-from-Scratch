"""
Persistance Manager

Central coordinator for aof operations and recovery.
"""
import time
import threading
from typing import Optional,Dict,Any
from .config import PersistenceConfig
from .aof import AOFWriter
from .recovery import RecoveryManager