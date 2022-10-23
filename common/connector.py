# Connection used to send HTTP request
from __future__ import annotations
from typing import *

import asyncio
import aiohttp

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

    async def http_request(self, auth_required, *args, **kwargs) -> aiohttp.ClientResponse:
        if (None == self.session) or (True == self.session.closed):
            self.update_session()
        if (True == auth_required) and (False == self._validate_auth()):
            self.update_auth()
        return self.session.request(*args, **kwargs)
    
    async def http_downloader(self, auth_required, output_path, *args, **kwargs) -> bool:
        if (None == self.session) or (True == self.session.closed):
            self.update_session()
        if (True == auth_required) and (False == self._validate_auth()):
            self.update_auth()
        response = self.session.request(*args, **kwargs)
    
    async def http_chunked_downloader(self, auth_required, output_path, *args, **kwargs) -> bool:
        if (None == self.session) or (True == self.session.closed):
            self.update_session()
        if (True == auth_required) and (False == self._validate_auth()):
            self.update_auth()

