# Utilities to constraint operations
from __future__ import annotations
from typing import *


# For Class that is to be used as a definition (Global, No objects)
class ConstraintDefinition:
    def __init__(self) -> None:
        raise NotImplementedError(
            "Instance of Definitions must not be instantiated")
