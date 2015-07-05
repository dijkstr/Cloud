#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from PyQt4 import QtGui, Qt, QtCore

class FileDialog(QtGui.QFileDialog):
	def __init__(self, *args):
		QtGui.QFileDialog.__init__(self, *args)
		self.setOption(self.DontUseNativeDialog, True)
		self.setFileMode(self.ExistingFiles)
		btns = self.findChildren(QtGui.QPushButton)
		self.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
		self.openBtn.clicked.disconnect()
		self.openBtn.clicked.connect(self.openClicked)
		self.tree = self.findChild(QtGui.QTreeView)

	def openClicked(self):
		inds = self.tree.selectionModel().selectedIndexes()
		files = []
		for i in inds:
			if i.column() == 0:
				files.append(os.path.join(str(self.directory().absolutePath()),str(i.data())))
			self.selectedFiles = files
			self.close()
		for f in files:
			print (str(f))			
		return True

	def filesSelected(self):
		return self.selectedFiles
'''
if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	frm = FileDialog()    
	frm.show()
	sys.exit(app.exec_())
'''
