# Fetches data from Zerodha (Kite)
from __future__ import annotations
from typing import *

import asyncio
import aiohttp
from pydantic import BaseModel

from technical_analysis.src.ta_defs import StockListing
from technical_analysis.src.data_fetcher.connector import HTTPConnector
from technical_analysis.src.data_fetcher.zerodha_endpoints import ZerodhaEndpoint

class ZerodhaStockListing(BaseModel):
    instrument_token : str
    exchange_token : str
    trading_symbol : str
    name : str
    instrument_type : str
    segment : str
    exchange : str



async def get_stock_listing_data(connector : HTTPConnector) -> List[ZerodhaStockListing]:
    response = connector.http_request(False, 'GET', ZerodhaEndpoint.STOCK_LISTING_API, compress=True, )

