# URL endpoints for Zerodha (Kite)
from __future__ import annotations
from typing import *

from pydantic import BaseModel

from common.constraint import ConstraintDefinition


class ZerodhaEndpoint(ConstraintDefinition):
    STOCK_LISTING_BROWSER : str = ""
