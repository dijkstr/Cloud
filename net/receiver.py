# -*- coding: utf-8 -*-

from threading import Thread
import sys
import socket
from q_send_item import *
from q_pending_item import *
from q_recv_item import *
import time
import global_vars

class receiver(Thread):

	def __init__(self,socket):
		Thread.__init__(self)
		self.queue_enable = True
		self.socket = socket

	def run(self):
		while self.queue_enable:
			recdata=self.socket.recv(global_vars.recv_buff_size)
			data = recdata
			# print 'data' + data
			pending_message = global_vars.q_pending.get()
			recevie_message = q_recv_item(pending_message.url,pending_message.str_to_send,pending_message.action_type,pending_message.send_time,data,time.time())
			global_vars.q_recv.put(recevie_message)


	def stop(self):
		self.queue_enable = False

	def __del__(self):
		print "receiver thread quits"
