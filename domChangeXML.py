import sys
import socket
import json
from xml.dom import minidom , Node

class bookscanner:
	def __init__(self,doc):
		self.D = minidom.Document()
		for child in doc.childNodes :
			if child.nodeType == Node.ELEMENT_NODE:
				title = self.D.createElement(child.nodeName)
				self.D.appendChild(title)
				self.handle_book(child,title)
		f = file("dirtree.xml","w")
		self.D.writexml(f)
		f.close()
                 
	def handle_book(self,node,element):
		for child in node.childNodes:
			if child.nodeType == Node.ELEMENT_NODE :
				if child.nodeName=="dir":
					file_element=self.D.createElement("folder")
					title =self.D.createElement("title")
					title.appendChild(self.D.createTextNode(child.getAttribute("name")))
					file_element.appendChild(title)
					element.appendChild(file_element)
					self.handle_book(child,file_element)
				if child.nodeName=="file":
					file_element=self.D.createElement("file")
					title =self.D.createElement("title")
					title.appendChild(self.D.createTextNode(child.getAttribute("name")))
					file_element.appendChild(title)
					element.appendChild(file_element)	

def changeXML():
	doc = minidom.parse("file.xml")
	for child in doc.childNodes :
		if child.nodeType == Node.ELEMENT_NODE:
			bookscanner(child)
