from logging import handlers
import logging

from aiohttp import web
import aiohttp
import asyncio

import ssl

import os
from time import sleep
import json
import requests

class AbstractEventServer():
	def __init__(self, ip='0.0.0.0', port=65000, public_key='public.pem', private_key='private.key'):
		self.__logger = logging.getLogger("server")
		formatter = logging.Formatter('%(asctime)s SRVR | %(levelname)s | %(message)s')
		sh = logging.StreamHandler()
		sh.setLevel(logging.DEBUG)
		sh.setFormatter(formatter)
		self.__logger.addHandler(sh)
		self.__logger.setLevel(logging.DEBUG)

		self.__ip = ip
		self.__port = port
		self.__public_key = public_key
		self.__private_key = private_key

	async def process(self, data: dict):
		return "Default response"

	async def recv_req(self, request):
		self.__logger.debug(f"Request recv: {request}")
		data = await request.json()
		self.__logger.debug(f"Data recv: {data}")

		result = await self.process(data)

		return web.Response(text=result)

	async def main(self):
		app = web.Application()
		app.router.add_post('/', self.recv_req)

		runner = web.AppRunner(app)
		await runner.setup()

		ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
		ssl_context.load_cert_chain(self.__public_key, self.__private_key)
		site = web.TCPSite(runner, self.__ip, self.__port, ssl_context=ssl_context)
		await site.start()

		self.__logger.info(f"Serving on ('{self.__ip}', {self.__port}) ...")

   	 	# wait forever
		await asyncio.Event().wait()

	def start(self):
		asyncio.run(self.main())

if __name__ == '__main__':
	a = AbstractEventServer(public_key='/home/fourbolt/Documents/resume_formatter/keys/test.pem', private_key='/home/fourbolt/Documents/resume_formatter/keys/test.key')
	a.start()
