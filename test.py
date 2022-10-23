#from technical_analysis.src.data_fetcher.zerodha_endpoints import ZerodhaEndpoint

#print(ZerodhaEndpoint.STOCK_LISTING_BROWSER)

import json
import requests
import pdb

import aiohttp
import asyncio

async def main():
    session = aiohttp.ClientSession()
    headers = {
        "Accept-Encoding": "identity",
    }
    response = await session.request('HEAD', "https://www.lawcommission.gov.np/en/wp-content/uploads/2019/07/The-Act-Relating-to-Compulsory-and-Free-Education-2075-2018.pdf", headers=headers)
    fsize = int(response.headers.get("content-length", -1))
    print(response)
    print(response.headers)
    print(f"file size : {fsize}")
    headers = {
        "Range" : f"bytes=0-500"
    }
    response = await session.request('GET', "https://filesamples.com/samples/document/pdf/sample3.pdf", headers=headers)
    print(response.status)
    data = await response.read()
    with open("./data/temp.pdf", "wb") as f:
        f.write(data)
    await session.close()



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
