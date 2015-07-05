# -*- coding: utf-8 -*-

from threading import Thread
import global_vars
import sys
import socket
from sender import *
from receiver import *
from q_send_item import *

class queue_controller():
	def __init__(self):
		self.queue_enable = True
		s=socket.socket()
		s.connect(('127.0.0.1',10000))
		self.sender = sender(s)
		self.receiver = receiver(s)

	def queue_exec(self):
		self.sender.start()
		self.receiver.start()

	def stop(self):
		self.sender.stop()
		self.receiver.stop()

	def __del__(self):
 		print "queue_controller quit"


#debug routine
if __name__=="__main__":
	send_message = q_send_item('1','-X DELETE -H "X-Auth-Token: " http://192.168.68.103:443/v1/AUTH_glfs/jintao','delete')
	send_message2 = q_send_item('2','-X GET -H "X-Auth-Token: " http://192.168.68.103:443/v1/AUTH_glfs','get')
	global_vars.q_send.put(send_message)
	global_vars.q_send.put(send_message2)
	# global_vars.q_send.put(send_message)
	# global_vars.q_send.put(send_message)
	# global_vars.q_send.put(send_message)
	q_controller = queue_controller()
	q_controller.queue_exec()
