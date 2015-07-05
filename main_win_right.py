#!/usr/bin/python
#-*-coding:utf-8-*-
import sip
# sip.setapi('QVariant', 2)
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, QtDBus, QtXml
import sys
import time
import codecs
import ui.ui_main
from ui.ui_main import Ui_mainWindow

class main_win_right(QtGui.QMainWindow, ui.ui_main.Ui_mainWindow):
	def __init__(self,parent=None):
		super(main_win_right,self).__init__(parent)	
		#menu_right
		#popMenu
		self.popMenu = QtGui.QMenu()
		self.action_b1 = QtGui.QAction(u'上传', self)
		self.action_b2 = QtGui.QAction(u'新建', self)
		self.action_b3 = QtGui.QAction(u'粘贴', self)
		self.action_b4 = QtGui.QAction(u'刷新', self)
		self.action_b5 = QtGui.QAction(u'属性', self)
		self.popMenu.addAction(self.action_b1)
		self.popMenu.addAction(self.action_b2)
		self.popMenu.addAction(self.action_b3)
		self.popMenu.addAction(self.action_b4)
		self.popMenu.addAction(self.action_b5)

		#popMenu_file
		self.popMenu_file = QtGui.QMenu()
		self.action_f1 = QtGui.QAction(u'打开', self)
		self.action_f2 = QtGui.QAction(u'下载', self)
		self.action_f3 = QtGui.QAction(u'转入保险箱', self)
		self.action_f4 = QtGui.QAction(u'移动至', self)
		self.action_f5 = QtGui.QAction(u'复制', self)
		self.action_f6 = QtGui.QAction(u'剪切', self)
		self.action_f7 = QtGui.QAction(u'重命名', self)
		self.action_f8 = QtGui.QAction(u'删除', self)
		self.action_f0 = QtGui.QAction(u'属性', self)
		self.popMenu_file.addAction(self.action_f1)
		self.popMenu_file.addAction(self.action_f2)
		self.popMenu_file.addAction(self.action_f3)
		self.popMenu_file.addAction(self.action_f4)
		self.popMenu_file.addAction(self.action_f5)
		self.popMenu_file.addAction(self.action_f6)
		self.popMenu_file.addAction(self.action_f7)
		self.popMenu_file.addAction(self.action_f8)
		self.popMenu_file.addAction(self.action_f0)

		


