#!/usr/bin/python
# -*- coding: utf8 -*-

import vfdpos

mypos = vfdpos.vfd_pos(0x0201)

mypos.poscur(3,5)
mypos.printchr(0xC8)
mypos.poscur(4,15)
mypos.write_msg(u"¤")
mypos.poscur(0,0)
mypos.write_msg(u"Cet été sera\n\rtrès chaud!")
mypos.write_msg("CALIENTE!")

raw_input("PRESS ENTER TO EXIT")
mypos.close()
