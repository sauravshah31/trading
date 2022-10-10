# Definitions of Classes used for Technical Analysis
from __future__ import annotations
from typing import *

from pydantic import BaseModel

class StockListing(BaseModel):
    company : str       #ABC Pvt Ltd.
    symbol : str        #abc
    exchange : str      #bse
    desc : str          #Edtech company



class StockData(BaseModel):
    high : float
    low : float
    opening_price : float
    closing_price : float
    volume : int

