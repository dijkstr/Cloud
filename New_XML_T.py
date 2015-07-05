# -*- coding: utf-8 -*-
from mwclient import get_json 
import os
import time
from lxml import etree
import config_main_win
from xml.etree.ElementTree import Element


def dir_as_tree(OB,request):
	basename = OB["name"].decode('utf-8')
	node = etree.Element("node")
	node1 = etree.Element("title")
	node1.text= basename
	node.append(node1)

	if len(OB)==2 and OB:
		node.tag = 'folder'
		node.attrib['lastTime']=OB["last_modified"]
		request = request+"/"+OB["name"]
		decoded=get_json(request)
		for i in decoded:
			child_node = dir_as_tree(i,request)
			node.append(child_node)
		return node

	elif len(OB)==4 and OB:
		print "file",OB["name"]
		node.tag ='file'
		node.attrib["lastTime"]=OB["modificationTime"]
		node.attrib['size']=str(OB["bytes"])
		node.attrib['md5']=OB["md5"]
		return node

# Create a tree of the current working directory
def get_xml_t():
	request = '-X GET -H "X-Auth-Token: " http://'+config_main_win.config_main_win().ip+':443/v1/AUTH_glfs'
	decoded=get_json(request)
	root = etree.Element("node")
	root.tag ='root'
	for i in decoded:
		node= dir_as_tree(i,request)
		root.append(node)
	tree = etree.ElementTree(root)
	# Create an element tree from the root node
	# (in order to serialize it to a complete XML document)

	xml_document = etree.tostring(tree,
                              pretty_print=True,
                              xml_declaration=True,
                              encoding='utf-8')
	fileHandle = open ('dirtree.xml', 'w' ) 
	fileHandle.write (xml_document)
	fileHandle.close()
