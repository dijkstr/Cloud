# -*- coding: utf-8 -*-

class q_pending_item(object):
	def __init__(self,url,str_to_send,action_type,send_time):
		self.url = url
		self.str_to_send = str_to_send
		self.action_type = action_type
		self.send_time = send_time