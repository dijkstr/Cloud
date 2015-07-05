import sys
import socket
import json
from net.queue_controller import *
import net.global_vars

def get_json(path):
	request = path
	result = sendmsg_mw(request)
	print "result",result[:result.find("]")+1]
	decoded = json.loads(result[:result.find("]")+1])
	return decoded

def sendmsg_mw(request):
	q=q_send_item("",request,"")
	global_vars.q_send.put(q)
	while(1):
		if not global_vars.q_recv.empty():
			recv_message = global_vars.q_recv.get()
			return recv_message.response

