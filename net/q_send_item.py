# -*- coding: utf-8 -*-

class q_send_item(object):
	def __init__(self,url,str_to_send,action_type):
		self.url = url
		self.str_to_send = str_to_send
		self.action_type = action_type