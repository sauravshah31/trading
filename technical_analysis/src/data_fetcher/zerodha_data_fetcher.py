# Fetches data from Zerodha (Kite)
from __future__ import annotations
from typing import *

import asyncio
from pydantic import BaseModel
import os
import time
import csv

from common.connector import HTTPConnector
from common.config import Config
from technical_analysis.src.data_fetcher.zerodha_endpoints import ZerodhaEndpoint
from technical_analysis.src.data_fetcher.zerodha_constants import ZerodhaConstants

class ZerodhaStockListing(BaseModel):
    instrument_token : str
    exchange_token : str
    trading_symbol : str
    name : str
    instrument_type : str
    segment : str
    exchange : str

async def get_stock_listing_data(connector : HTTPConnector, force = False) -> List[ZerodhaStockListing]:
    data: List[ZerodhaStockListing] = []
    to_download = False
    fpath = os.path.join(Config.DATA_PATH, ZerodhaConstants.STOCK_LISITNG_FNAME)
    if force:
        to_download = True
    elif not(os.path.exists(fpath)):
        to_download = True
    else:
        # download listings only once in 24 hours
        fstat = os.stat(fpath)
        currtime = time.time()
        try:
            difftime = currtime - fstat.st_mtime #@todo: check for MacOS
            difftime /= (60 * 60) #seconds to hour
            if difftime >= 24.0:
                to_download = True
        except:
            to_download = True
    if (True == to_download):
        await connector.http_chunked_downloader(False, fpath)
    
    with open(fpath, "rb", newline='') as f:
        csvreader = csv.reader(f, delimiter=',')
        next(csvreader, None)
        for row in csvreader:
            listing = ZerodhaStockListing(instrument_token=row[0],
                                        exchange_token=row[1], 
                                        trading_symbol=row[2],
                                        name=row[3],
                                        instrument_type=row[9],
                                        segment=row[10],
                                        exchange=row[11])
            data.append(listing)
    #@todo: range return is better?
    return listing