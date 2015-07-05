# -*- coding: utf-8 -*-

from threading import Thread
import sys
import socket
from q_send_item import *
from q_pending_item import *
import time
import global_vars



class sender(Thread):

	def __init__(self,socket):
		Thread.__init__(self)
		self.queue_enable = True
		self.socket = socket

	def run(self):
		while self.queue_enable:
			if not global_vars.q_send.empty():
				send_message = global_vars.q_send.get()

				q_send_size = global_vars.q_pending.qsize()

				if q_send_size != 0:
					for i in range(q_send_size):
						temp_item = global_vars.q_pending.get()
						if temp_item.str_to_send is not send_message.str_to_send:
							global_vars.q_pending.put(temp_item)
						else:
							return

				pending_message = q_pending_item(send_message.url,send_message.str_to_send,send_message.action_type,time.time())
				global_vars.q_pending.put(pending_message)
				self.socket.send(send_message.str_to_send)
				time.sleep(5)

	def stop(self):
		self.queue_enable = False

	def __del__(self):
		print "sender thread quits"

    # s=socket.socket()
    # s.connect(('127.0.0.1',10000))
    # s.send(request)
    # # data = 'The data received is '
    # while(1):
    #     recdata=s.recv(500)
    #     data = data + recdata
    #     if(data.find(request) != -1):
	   #  data = data.replace(request,'')
	   #  break

    # #print data
    # s.close()
    # return data