#!/usr/bin/python
# -*- coding: utf8 -*-

import vfdpos
import time

wnpos = vfdpos.vfd_pos(0x0201)
print "PRESS CTRL+C TO QUIT"
try:
	while True:
		wnpos.poscur(1,1)
		prestime = time.localtime()
		date = time.strftime("%a %d %b %Y", prestime).center(20)
		wnpos.write_msg(date)
		hour = time.strftime("%H:%M", prestime).center(20)
		wnpos.poscur(3,1)
		wnpos.write_msg(hour) 
		time.sleep(10)
except KeyboardInterrupt:
	pass
wnpos.close()
