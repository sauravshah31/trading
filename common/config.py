# Config class
from __future__ import annotations
from typing import *

from .constraint import ConstraintDefinition

class Config(ConstraintDefinition):
    DOWNLOAD_CHUNK_SIZE : int = 20000000  #download chunk size in bytes
    DATA_PATH : str = "./data"