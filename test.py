#from technical_analysis.src.data_fetcher.zerodha_endpoints import ZerodhaEndpoint

#print(ZerodhaEndpoint.STOCK_LISTING_BROWSER)

import json
import pdb

import aiohttp
import asyncio

from technical_analysis.src.data_fetcher.zerodha_data_fetcher import get_stock_listing_data
from common.connector import HTTPConnector

async def main():
    connector = HTTPConnector()
    data = await get_stock_listing_data(connector)
    print(len(data))




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
