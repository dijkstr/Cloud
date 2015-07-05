# -*- coding: utf-8 -*-

class q_recv_item(object):
	def __init__(self,url,str_to_send,action_type,send_time,response,recv_time):
		self.url = url
		self.str_to_send = str_to_send
		self.action_type = action_type
		self.send_time = send_time
		self.response = response
		self.recv_time = recv_time
		print "response",response
