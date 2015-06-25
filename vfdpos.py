#!/usr/bin/python
# -*- coding: utf8 -*-

# VFD PoS library for WN USB using PyUSB
# Copyright (C) 2015  Antoine FERRON

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>


import usb.core
import usb.util

class vfd_pos:
	def __init__(self,pid):
		self.dev = usb.core.find(idVendor=0x0aa7, idProduct=pid)
		if self.dev is None:
			raise IOError("Error : Connect PoS VFD WN USB")
		try:
			self.dev.detach_kernel_driver(1)
		except:
			pass
		try:
			cfg=self.dev[0]
			ep = cfg[(0,0)][1]
			assert ep is not None
			if ep.wMaxPacketSize!=32:
				ep = cfg[(1,0)][1]
			assert ep.wMaxPacketSize==32
			self.endpoint = ep
		except:
			raise IOError("Error initializing VFD")
		self.set_charset(0x31)
		self.clearscreen()
		self.poscur(0,0)
	
	def close(self):
		self.clearscreen()
	
	def send_buffer(self,buffer):
		self.endpoint.write(buffer)
	
	def selftest(self):
		buffer = [0x00]*32
		buffer[1] = 0x10
		self.send_buffer(buffer)
	
	def reset(self):
		buffer = [0x00]*32
		buffer[1] = 0x40
		self.send_buffer(buffer)
	
	def send_ctrl_seq(self,esc_seq):
		buffer = [0x00]*32
		buffer[0] = 0x02
		len_seq = len(esc_seq)
		buffer[2] = len_seq
		for datx in range(0, len_seq):
			buffer[3+datx] = esc_seq[datx]
		self.send_buffer(buffer)
	
	def set_charset(self,chrset):
		self.send_ctrl_seq( [0x1B, 0x52, chrset] )
	
	def clearscreen(self):
		self.send_ctrl_seq( [0x1B, 0x5B, 0x32, 0x4A] )
	
	def printchr(self,chr):
		self.send_ctrl_seq( [chr] )
	
	def poscur(self,line,col):
		seq=[]
		seq.append( 0x1B )
		seq.append( 0x5B )
		assert( 0 <= line <= 9)
		seq.append( 0x30 + line )
		seq.append( 0x3B )
		assert( 0 <= col <= 99)
		diz,unit = divmod(col,10)
		seq.append( 0x30 + diz)
		seq.append( 0x30 + unit)
		seq.append( 0x48 )
		self.send_ctrl_seq( seq )
	
	def write_msg(self,msgu):
		msg=msgu.encode('cp858')
		msg_chr=list(msg)[0:29]
		self.send_ctrl_seq(map( ord, msg_chr ))

