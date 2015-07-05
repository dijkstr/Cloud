# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename.ui'
#
# Created: Mon Jun 29 20:36:16 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(427, 138)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 427, 28))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(32,117,218);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(180, 3, 81, 21))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 11pt \"Droid Sans Fallback\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 35, 131, 31))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(112, 112, 112);\n"
"font: 10pt \"Noto Sans [unknown]\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 60, 371, 16))
        self.line.setStyleSheet(_fromUtf8("color: rgb(112, 112, 112);"))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 261, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("border-style: flat;"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.newfolder = QtGui.QPushButton(Dialog)
        self.newfolder.setGeometry(QtCore.QRect(160, 85, 109, 44))
        self.newfolder.setStyleSheet(_fromUtf8("background-image: url(:/images/new.png);\n"
"border-style: flat;"))
        self.newfolder.setText(_fromUtf8(""))
        self.newfolder.setObjectName(_fromUtf8("newfolder"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.newfolder, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "重命名", None))
        self.label_2.setText(_translate("Dialog", "重命名文件夹名称：", None))

import resource_rc
