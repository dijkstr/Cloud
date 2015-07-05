#!usr/bin/python
# -*-coding:utf-8-*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_newfolder
import sys


class new_folder(QDialog, ui_newfolder.Ui_Dialog):
    def __init__(self, parent=None):
        super(new_folder, self).__init__(parent)
        self.setupUi(self)

    # 连接信号和槽

    def name(self):
        return self.lineEdit.text()

    def clear_edit(self):
        self.lineEdit.setText("")
