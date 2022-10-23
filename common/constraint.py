# Utilities to constraint operations
from __future__ import annotations
from typing import *


# For Class that is to be used as a definition (Global, No objects)
class ConstraintDefinition:
    def __init__(self) -> None:
        raise NotImplementedError(
            "Class of type ConstraintDefinition must not be instantiated")
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        raise NotImplementedError(
            "Class of type ConstraintDefinition must not be instantiated")