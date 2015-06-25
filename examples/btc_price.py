#!/usr/bin/python
# -*- coding: utf8 -*-

import time
from vfdpos import *
from easy_rest_json import * 


mypos = vfd_pos(0x0201)
price_api = rest_json('https://api.coindesk.com/v1/bpi/currentprice.json')
mypos.write_msg("Bitcoin Price")
print "PRESS CTRL+C TO QUIT"
try:
	while True:
		price_api.get_data()
		btc_price = float( price_api.getkey("bpi/USD/rate") )
		mypos.poscur(3,0)
		mypos.write_msg("1 BTC = %.2f USD  "%btc_price)
		time.sleep(60)
except KeyboardInterrupt:
	pass
mypos.close()
