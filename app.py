#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-18 17:02:55
# @Author  : hbyandy (hbyandy@yeah.net)
# @Link    : 
# @Version : $Id$

from os import path
import logging
import logging.config
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

log_file_path = path.join(path.dirname(path.abspath(__file__)),'conf', 'logging.config')
logging.config.fileConfig(log_file_path)
app_logger = logging.getLogger("TEST_LOGGER")

def index(request):
	return web.Response(body = '<h1>Awesome</h1>')

async def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET','/',index)
	server = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return server

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()