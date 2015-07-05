# coding=utf-8
# !/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom
import sys
import time
import codecs


class domfilexml():
    def __init__(self):
        self.dom_save = xml.dom.minidom.parse("file.xml")
        self.dom_safe = xml.dom.minidom.parse("safebox_file.xml")
        self.collection = None
        self.max_item_num = 0
        self.pathlist = []
        self.itemlist = {}
        self.current_element = None
        self.current_path = "root/include/GL"
        self.search_file(self.current_path, "save")

    # 搜索路径下的所有item并返回一个字典
    def search_file(self, path, mode):
        if mode == "save":
            self.collection = self.dom_save.documentElement
        elif mode == "safe":
            self.collection = self.dom_safe.documentElement
        self.current_path = path
        primitive_path = path
        self.pathlist = path.split("/")
        del self.pathlist[0]
        root = self.collection.getElementsByTagName("root")[0]
        # 初始化当前路径
        self.current_element = root
        # 初始化当前路径下的元素
        current_elements_folders = self.collection.getElementsByTagName("root")
        current_elements_files = self.collection.getElementsByTagName("root")
        # 初始化当前路径下的所有文件夹
        child_folders = root.getElementsByTagName("dir")

        # 循环遍历整个路径直到找到最后的element
        for path in self.pathlist:
            for child_folder in child_folders:
                # print child_folder.nodeType
                if not child_folder.nodeType == 3:
                    title = child_folder.getAttribute('name')
                    if path == title:
                        self.current_element = child_folder
                        current_elements_folders = self.current_element.childNodes
                    # .getElementsByTagName("dir")  ###
                    # current_elements_files = self.current_element.childNodes.getElementsByTagName("file")   ###
            if self.current_element.getElementsByTagName("dir"):
                child_folders = self.current_element.childNodes  # .getElementsByTagName("dir")

        for child in current_elements_folders:
            if child.nodeName == "dir":
                folder_name = child.getAttribute("name")
                folder_lastTime = child.getAttribute("lastTime")
                folder_size = child.getAttribute("size")
                self.itemlist[folder_name] = {}
                self.itemlist[folder_name]["lastTime"] = folder_lastTime
                self.itemlist[folder_name]["size"] = folder_size
                self.itemlist[folder_name]["type_"] = "folder"
                self.itemlist[folder_name]["path"] = primitive_path + "/" + folder_name
            # for file_ in current_elements_files:
            elif child.nodeName == "file":
                file_name = child.getAttribute("name")
                self.itemlist[file_name] = {}
                file_type = child.getAttribute("postfix")
                file_lastTime = child.getAttribute("lastTime")
                file_size = child.getAttribute("size")
                self.itemlist[file_name]["lastTime"] = file_lastTime
                self.itemlist[file_name]["size"] = file_size
                self.itemlist[file_name]["type_"] = file_type
                self.itemlist[file_name]["path"] = primitive_path + "/" + file_name

    def create_node(self, time, name, mode):
        if mode == "save":
            name_e = self.dom_save.createElement("dir")
        elif mode == "safe":
            name_e = self.dom_safe.createElement("dir")
        child_nodes = self.current_element.getElementsByTagName("dir")
        for child_node in child_nodes:
            if child_node.getAttribute("name") == name:
                print "can't create same name file or dir"
                return False
        self.current_element.appendChild(name_e)
        name_e.setAttribute("name", name)
        name_e.setAttribute("lastTime", time)
        name_e.setAttribute("size", "0")
        name_e.setAttribute("postfix", "folder")
        self.write_xml(mode)
	return True

    def rename_node(self, name, new_name, mode):
        child_nodes = self.current_element.getElementsByTagName("dir")
	for child_node in child_nodes:
		if child_node.getAttribute("name") == new_name:
		    print "can't rename same name file or dir"
		    return False
        for child_node in child_nodes:
            if child_node.getAttribute("name") == name:
                child_node.setAttribute("name", new_name)
                print "name", new_name
                break
        self.write_xml(mode)
	return True

    def delete_node(self, name, mode):
        child_nodes = self.current_element.getElementsByTagName("dir")
        for child_node in child_nodes:
            if child_node.getAttribute("name") == name:
                self.current_element.removeChild(child_node)
        child_nodes = self.current_element.getElementsByTagName("file")
        for child_node in child_nodes:
            if child_node.getAttribute("name") == name:
                self.current_element.removeChild(child_node)
        self.write_xml(mode)

    def write_xml(self, mode):
        if mode == "save":
            f = file('file.xml', 'w')
            writer = codecs.lookup('utf-8')[3](f)
            self.dom_save.writexml(writer, encoding='utf-8')
        elif mode == "safe":
            f = file('safebox_file.xml', 'w')
            writer = codecs.lookup('utf-8')[3](f)
            self.dom_safe.writexml(writer, encoding='utf-8')
        writer.close()

    def create_array(self):
        content_list = []
        dictionary = self.itemlist
        for item_name in dictionary:
            if not dictionary[item_name]["type_"] == "folder":
                item = {"name": item_name, "lastTime": dictionary[item_name]["lastTime"],
                        "size": dictionary[item_name]["size"], "type_": dictionary[item_name]["type_"],
                        "path": dictionary[item_name]["path"]}
                self.isMaxitem(item)
                content_list.append(item)
            if dictionary[item_name]["type_"] == "folder":
                item = {"name": item_name, "lastTime": dictionary[item_name]["lastTime"],
                        "size": dictionary[item_name]["size"], "type_": "folder", "path": dictionary[item_name]["path"]}
                self.isMaxitem(item)
                content_list.append(item)
        return content_list

    def isMaxitem(self, item):
        if (len(item) > self.max_item_num):
            self.max_item_num = len(item)
            return False
        else:
            return True
