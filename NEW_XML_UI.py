# -*- coding: utf-8 -*-
from mwclient import get_json
import os
import time
from lxml import etree
import config_main_win
from xml.etree.ElementTree import Element


def dir_as_tree(OB,request):
	node = etree.Element("node")
	node.attrib['name'] = OB["name"].decode('utf-8')
	node.attrib['postfix']=OB["name"][0][1:]

	if len(OB)==2 and OB:
		node.tag = 'dir'
		node.attrib['lastTime']=OB["last_modified"]
		node.attrib['size']="0"
		request = request+"/"+OB["name"]
		decoded=get_json(request)
		for i in decoded:
			child_node = dir_as_tree(i,request)
			node.append(child_node)
		return node

	elif len(OB)==4 and OB:
		node.tag ='file'
		node.attrib["lastTime"]=OB["modificationTime"]
		node.attrib['size']=str(OB["bytes"])
		node.attrib['md5']=OB["md5"]
		return node

def sendmsg_mw(request):
	s=socket.socket()
	s.connect(('127.0.0.1',10000))
	s.send(request)
	data = 'The data received is '
	while(1):
		recdata=s.recv(500)
		data = recdata
        	if(data.find(request) != -1):
	    		data = data.replace(request,'')
	    		break

    #print data
	s.close()
	return data

# Create a tree of the current working directory
def get_xml_ui():
	request = '-X GET -H "X-Auth-Token: " http://'+config_main_win.config_main_win().ip+':443/v1/AUTH_glfs'
	decoded = get_json(request)
	root = etree.Element("node")
	root.tag ='root'
	for i in decoded:
		node= dir_as_tree(i,request)
		root.append(node)
	root1 = etree.Element("node")
	root1.tag ='root'
	root1.append(root)
	tree = etree.ElementTree(root1)
	# Create an element tree from the root node
	# (in order to serialize it to a complete XML document)

	xml_document = etree.tostring(tree,
                              pretty_print=True,
                              xml_declaration=True,
                              encoding='utf-8')
	fileHandle = open ('file.xml', 'w' ) 
	fileHandle.write (xml_document)
	fileHandle.close()
