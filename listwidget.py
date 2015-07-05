# -*-coding:utf-8-*-
from PyQt4 import QtCore, QtGui, QtXml
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os


class listwidget(QtGui.QListWidget):
    def __init__(self, parent=None):
        super(listwidget, self).__init__(parent)
        self.setAcceptDrops(True)
        # self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

        self.template_path = "doc/"
        # listwidget默认选项
        self.mode = QtGui.QListView.IconMode
        self.flow = QtGui.QListView.LeftToRight
        self.default_grid_height_icon = 100
        self.default_grid_width_icon = 100
        self.default_grid_height_list = 40
        self.default_grid_width_list = 200
        self.default_width = 600
        self.default_height = 370
        self.default_x_p = 20
        self.default_y_p = 10
        self.default_width_p = 591
        self.default_height_p = 441
        self.default_dragenabled = True
        self.default_spacing = 0
        self.default_batchsize = 100
        self.default_selectionrectvisible = True
        self.default_objectname = "listWidget"
        self.default_grid_width = self.default_grid_width_icon
        self.default_grid_height = self.default_grid_height_icon
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

    def seticonmode(self):
        self.mode = QtGui.QListView.IconMode
        self.flow = QtGui.QListView.LeftToRight
        self.default_grid_width = self.default_grid_width_icon
        self.default_grid_height = self.default_grid_height_icon

    def setlistmode(self):
        self.mode = QtGui.QListView.ListMode
        self.flow = QtGui.QListView.TopToBottom
        self.default_grid_width = self.default_grid_width_list
        self.default_grid_height = self.default_grid_height_list

    def ui_listwidget(self, array, horizontalLayout):
        self.clear()
        horizontalLayout.addWidget(self)
        icon_provider = QFileIconProvider()
        self.setObjectName(self.default_objectname)
        self.setMinimumSize(QtCore.QSize(self.default_width, self.default_height))
        self.setGeometry(QtCore.QRect(self.default_x_p, self.default_y_p, self.default_width_p, self.default_height_p))
        # self.setDragDropOverwriteMode(True)
        # self.setDragEnabled(self.default_dragenabled)
        # self.setMovement(QtGui.QListView.Snap)
        self.setFlow(self.flow)
        self.setResizeMode(QtGui.QListView.Fixed)
        self.setResizeMode(QtGui.QListView.Adjust)
        self.setLayoutMode(QtGui.QListView.Batched)
        self.setSpacing(self.default_spacing)
        self.setGridSize(QtCore.QSize(self.default_grid_width, self.default_grid_height))
        self.setViewMode(self.mode)
        self.setBatchSize(self.default_batchsize)
        self.setSelectionRectVisible(self.default_selectionrectvisible)
        for i in array:
            item = QtGui.QListWidgetItem()
            icon = QtGui.QIcon()
            if (i["type_"] == "folder"):
                icon = icon_provider.icon(QFileIconProvider.Folder)
            else:
                icon = self.fileExtensionIcon(i)
            item.setIcon(icon)
            item.setText(i["name"])
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
            self.addItem(item)

            # 生成文件图标

    def fileExtensionIcon(self, array_file):
        icon_provider = QFileIconProvider()
        icon = QtGui.QIcon()
        try:
            f = open(self.template_path + array_file["name"], 'w')
            icon = icon_provider.icon(QFileInfo(self.template_path + array_file["name"]))
            os.remove(self.template_path + array_file["name"])
        except:
            print "path error"
        return icon

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(listwidget, self).dragEnterEvent(event)

    def dropEvent(self, event):
        item = self.itemAt(event.pos())
        if item:
            print "tree item path:" + item.text()
        else:
            print "no target"
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                print url.path()
            event.acceptProposedAction()
        else:
            super(listwidget, self).dropEvent(event)


'''
	def mimeData(self, items):
		data = QMimeData()
		urls = []
		for item in items:
			urls.append(QUrl.fromLocalFile(item.text()))
			print item.text()
		data.setUrls(urls)
		return data 
'''
