#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-18 07:55:22
# @Author  : hbyandy (hbyandy@yeah.net)
# @Link    : 
# @Version : $Id$

from datetime import datetime

def print_current_time():
	print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print_current_time()
