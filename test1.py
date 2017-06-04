#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-18 07:40:12
# @Author  : hbyandy (hbyandy@yeah.net)
# @Link    : 
# @Version : $Id$
import asyncio
from my_dateutil import *

async def compute(x,y):
	print('%s Computing %s + %s ' % (print_current_time(),x,y))
	await asyncio.sleep(10.0)
	return x+y

async def print_sum(x,y):
	result = await compute(x,y)
	print ('%s %s + %s = %s' % (print_current_time(),x,y,result))

tasks=[print_sum(3,4),print_sum(1,2)]
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()