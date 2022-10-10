# Fetches stock listings from Zerodha
from __future__ import annotations
from typing import *

import asyncio
import aiohttp

from technical_analysis.src.ta_defs import StockListing
from technical_analysis.src.data_fetcher.zerodha_endpoints import ZerodhaEndpoint


async def get_stock_listing_data(exchange : str) -> AsyncIterator[StockListing]:
    pass

