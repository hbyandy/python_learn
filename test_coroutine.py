#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-17 21:38:32
# @Author  : hbyandy (hbyandy@yeah.net)
# @Link    : 
# @Version : $Id$

def consumer():
	r =''
	while True:
		n = yield r
		if not n:
			return
		print('[CONSUMER] consuming %s ...' % n)
		r = "200 OK"


def producer(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n+1
		print('[PRODUCER] producing %s' % n)
		r=c.send(n)
		print('[PRODUCER] consumer retrun: %s' % r)
	c.close()

c=consumer()

c.next()

#producer(c)
