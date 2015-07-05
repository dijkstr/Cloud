#!/usr/bin/python
#-*-coding:utf-8-*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_conveylist
import sys

class conveylist(QDialog,ui_conveylist.Ui_Dialog):
	def __init__(self,parent=None):
		super(conveylist,self).__init__(parent)
		self.setupUi(self)
		self.connect(self.clear, QtCore.SIGNAL("clicked()"), self,QtCore.SLOT("slot_conveylist_clear()"))

	@QtCore.pyqtSlot()
	def slot_conveylist_clear(self):
		button = QtGui.QMessageBox.question(self,u"提示",u"确定清空所有纪录?",QMessageBox.Ok|QMessageBox.Cancel,QMessageBox.Ok)
		if button == QMessageBox.Ok:
			self.tab_finish.clear()
		#self.repaint()
