#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-18 21:14:49
# @Author  : hbyandy (hbyandy@yeah.net)
# @Link    : 
# @Version : $Id$

import aiomysql
import asyncio
import logging

async def create_pool(loop,**kw):
	logging.info('create database connection pool')
	global __pool
	__pool = await aiomysql.create_pool(
		host = kw.get('host','locahost'),
		port = kw.get('port',3306),
		user = kw['user'],
		password = kw['password'],
		db = kw['db'],
		charset = kw.get('charset','utf-8'),
		autocommit = kw.get('autocommit',True),
		maxsize = kw.get('maxsize',10),
		minsize = kw.get('minxsize',1),
		loop = loop
		)

async def select(sql,args,size = None):
	logging.info(sql,args)
	global __pool
	with await __pool as conn:
		cur = await conn.cursor(aiomysql.DictCursor)
		await cur.execute(sql.replace('?','%s'),args or ())
		if size:
			rs = await cur.fetchmany(size)
		else:
			rs = await cur.fetchall()
		await cur.close()
		logging.info('rows returned : %s',len(rs))
		return rs

async def execute(sql,args):
	logging.info(sql)
	with await __pool as conn:
		try:
			cur = await conn.cursor()
			await cur.execute(sql.replace('?','%s'),args)
			affected = cur.rowcount
			await cur.close()
		except BaseException as e:
			raise
		return affected
