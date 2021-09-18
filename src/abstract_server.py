from logging import handlers
import logging

from aiohttp import web
import aiohttp
import asyncio

import os
from time import sleep
import json
import requests

class AbstractServer():
	def __init__(self, port: int, ip='0.0.0.0'):
		self._logger = logging.getLogger("server")
		formatter = logging.Formatter('%(asctime)s SRVR | %(levelname)s | %(message)s')
		sh = logging.StreamHandler()
		sh.setLevel(logging.DEBUG)
		sh.setFormatter(formatter)
		self._logger.addHandler(sh)
		self._logger.setLevel(logging.DEBUG)

		self._ip = ip
		self._port = port

	def process(self, data: dict):
		return "Default response"

	async def recv_req(self, request):
		self._logger.debug(request)
		data = await request.json()
		self._logger.debug(data)

		result = self.process(data)

		return web.Response(text=result)

	async def main(self):
		app = web.Application()
		app.router.add_post('/', self.recv_req)

		runner = web.AppRunner(app)
		await runner.setup()
		site = web.TCPSite(runner, self._ip, self._port)    
		await site.start()

		self._logger.info(f"Serving on ('{self._ip}', {self._port}) ...")

   	 	# wait forever
		await asyncio.Event().wait()

	def start(self):
		asyncio.run(self.main())

if __name__ == '__main__':
	a = AbstractServer(65000)
	a.start()