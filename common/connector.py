# Connection used to send HTTP request
from __future__ import annotations
from typing import *

import asyncio
import aiohttp

from common.config import Config

# Connection class will be used when sending http request
class HTTPConnector:
    def __init__(self) -> None:
        self.cookies : dict = {}
        self.headers : dict = {}
        self.session : aiohttp.ClientSession = None
        self.storage : dict = {}
    
    def update_session(self) -> None:
        self.session = aiohttp.ClientSession()

    def update_auth(self) -> None:
        pass

    def _validate_auth(self) -> None:
        pass

    async def http_get_file_size(self, url : str, cookies : dict = {}, headers : dict = {}) -> int:
        headers["Accept-Encoding"] = "identity"
        response = await self.session.request('HEAD', url, headers=headers, cookies=cookies)
        fsize = int(response.headers.get("content-length", -1))
        return fsize

    async def http_request(self, auth_required : bool, *args, **kwargs) -> aiohttp.ClientResponse:
        if (None == self.session) or (True == self.session.closed):
            self.update_session()
        if (True == auth_required) and (False == self._validate_auth()):
            self.update_auth()
        response: aiohttp.ClientResponse  = await self.session.request(
            *args, **kwargs)
        return response
    
    async def http_downloader(self, auth_required : bool, output_path : str, *args, **kwargs) -> None:
        if (None == self.session) or (True == self.session.closed):
            self.update_session()
        if (True == auth_required) and (False == self._validate_auth()):
            self.update_auth()
        response = await self.session.request(*args, **kwargs)
        data = await response.read()
        with open(output_path, "wb") as f:
            f.write(data)
    
    async def http_chunked_downloader(self, auth_required : bool, output_path : str, *args, **kwargs) -> None:
        if (None == self.session) or (True == self.session.closed):
            self.update_session()
        if (True == auth_required) and (False == self._validate_auth()):
            self.update_auth()
        #@todo: Is using Range:bytes=start-end in header and read() better?
        response = await self.session.request(*args, **kwargs)
        with open(output_path, "wb") as f:
            async for chunk in response.content.iter_chunked(Config.DOWNLOAD_CHUNK_SIZE):
                f.write(chunk)