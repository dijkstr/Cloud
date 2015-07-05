# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conveylist.ui'
#
# Created: Mon Jun 29 20:36:15 2015
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
        Dialog.resize(406, 455)
        Dialog.setMinimumSize(QtCore.QSize(406, 455))
        Dialog.setMaximumSize(QtCore.QSize(406, 455))
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 407, 28))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(32,117,218);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(175, 3, 71, 21))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 11pt \"Droid Sans Fallback\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 28, 410, 431))
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 407, 401))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.downloading = QtGui.QListWidget(self.tab_2)
        self.downloading.setGeometry(QtCore.QRect(0, 0, 407, 401))
        self.downloading.setObjectName(_fromUtf8("downloading"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.finished = QtGui.QListWidget(self.tab_3)
        self.finished.setGeometry(QtCore.QRect(0, 47, 407, 352))
        self.finished.setObjectName(_fromUtf8("finished"))
        self.clear = QtGui.QToolButton(self.tab_3)
        self.clear.setGeometry(QtCore.QRect(290, 0, 111, 47))
        self.clear.setStyleSheet(_fromUtf8("background-image: url(:/images/clear.png);\n"
"border-style: flat;"))
        self.clear.setText(_fromUtf8(""))
        self.clear.setObjectName(_fromUtf8("clear"))
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 161, 41))
        self.label_2.setStyleSheet(_fromUtf8("font: 12pt \"文泉驿微米黑\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "传输列表", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "       正   在   上   传       ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "       正   在   下   载       ", None))
        self.label_2.setText(_translate("Dialog", "已完成0个！", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "       传   输   完   成       ", None))

import resource_rc
