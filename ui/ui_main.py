# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(906, 616)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(870, 80))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(32,117,218);\n"
"border-color: rgb(0, 0, 0);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.yun = QtGui.QToolButton(self.frame)
        self.yun.setMinimumSize(QtCore.QSize(136, 51))
        self.yun.setMaximumSize(QtCore.QSize(136, 51))
        self.yun.setStyleSheet(_fromUtf8("background-image: url(:/images/yunpan.png);\n"
"border-style: flat;"))
        self.yun.setText(_fromUtf8(""))
        self.yun.setObjectName(_fromUtf8("yun"))
        self.horizontalLayout_5.addWidget(self.yun)
        self.bao = QtGui.QToolButton(self.frame)
        self.bao.setMinimumSize(QtCore.QSize(136, 51))
        self.bao.setMaximumSize(QtCore.QSize(136, 51))
        self.bao.setStyleSheet(_fromUtf8("background-image: url(:/images/safebox.png);\n"
"border-style: flat;"))
        self.bao.setText(_fromUtf8(""))
        self.bao.setObjectName(_fromUtf8("bao"))
        self.horizontalLayout_5.addWidget(self.bao)
        self.bei = QtGui.QToolButton(self.frame)
        self.bei.setMinimumSize(QtCore.QSize(136, 51))
        self.bei.setMaximumSize(QtCore.QSize(136, 51))
        self.bei.setStyleSheet(_fromUtf8("background-image: url(:/images/yunbeifen.png);\n"
"border-style: flat;"))
        self.bei.setText(_fromUtf8(""))
        self.bei.setObjectName(_fromUtf8("bei"))
        self.horizontalLayout_5.addWidget(self.bei)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        spacerItem = QtGui.QSpacerItem(250, 38, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.label = QtGui.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setMaximumSize(QtCore.QSize(50, 50))
        self.label.setStyleSheet(_fromUtf8("background-image: url(:/images/headportrait.png);\n"
"border-style: flat;"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.back = QtGui.QToolButton(self.centralwidget)
        self.back.setMinimumSize(QtCore.QSize(21, 21))
        self.back.setMaximumSize(QtCore.QSize(21, 21))
        self.back.setStyleSheet(_fromUtf8("background-image: url(:/images/back.png);\n"
"border-style: flat;"))
        self.back.setText(_fromUtf8(""))
        self.back.setObjectName(_fromUtf8("back"))
        self.horizontalLayout_3.addWidget(self.back)
        self.forward = QtGui.QToolButton(self.centralwidget)
        self.forward.setMinimumSize(QtCore.QSize(21, 21))
        self.forward.setMaximumSize(QtCore.QSize(21, 21))
        self.forward.setStyleSheet(_fromUtf8("background-image: url(:/images/forward.png);\n"
"border-style: flat;"))
        self.forward.setText(_fromUtf8(""))
        self.forward.setObjectName(_fromUtf8("forward"))
        self.horizontalLayout_3.addWidget(self.forward)
        self.none = QtGui.QComboBox(self.centralwidget)
        self.none.setMaximumSize(QtCore.QSize(0, 0))
        self.none.setObjectName(_fromUtf8("none"))
        self.horizontalLayout_3.addWidget(self.none)
        self.refresh = QtGui.QToolButton(self.centralwidget)
        self.refresh.setMinimumSize(QtCore.QSize(21, 21))
        self.refresh.setMaximumSize(QtCore.QSize(21, 21))
        self.refresh.setStyleSheet(_fromUtf8("background-image: url(:/images/refresh.png);\n"
"border-style: flat;"))
        self.refresh.setText(_fromUtf8(""))
        self.refresh.setObjectName(_fromUtf8("refresh"))
        self.horizontalLayout_3.addWidget(self.refresh)
        self.home = QtGui.QToolButton(self.centralwidget)
        self.home.setMinimumSize(QtCore.QSize(21, 21))
        self.home.setMaximumSize(QtCore.QSize(21, 21))
        self.home.setStyleSheet(_fromUtf8("border-style: flat;\n"
"background-image: url(:/images/home.png);"))
        self.home.setText(_fromUtf8(""))
        self.home.setObjectName(_fromUtf8("home"))
        self.horizontalLayout_3.addWidget(self.home)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(450, 0))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_3.addWidget(self.textEdit)
        spacerItem1 = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.upload = QtGui.QToolButton(self.centralwidget)
        self.upload.setMinimumSize(QtCore.QSize(66, 27))
        self.upload.setMaximumSize(QtCore.QSize(66, 27))
        self.upload.setStyleSheet(_fromUtf8("background-image: url(:/images/upload.png);\n"
"border-style: flat;"))
        self.upload.setText(_fromUtf8(""))
        self.upload.setObjectName(_fromUtf8("upload"))
        self.horizontalLayout_3.addWidget(self.upload)
        self.download = QtGui.QToolButton(self.centralwidget)
        self.download.setMinimumSize(QtCore.QSize(66, 27))
        self.download.setMaximumSize(QtCore.QSize(66, 27))
        self.download.setStyleSheet(_fromUtf8("background-image: url(:/images/download.png);\n"
"border-style: flat;"))
        self.download.setText(_fromUtf8(""))
        self.download.setObjectName(_fromUtf8("download"))
        self.horizontalLayout_3.addWidget(self.download)
        self.newfolder = QtGui.QToolButton(self.centralwidget)
        self.newfolder.setMinimumSize(QtCore.QSize(21, 21))
        self.newfolder.setMaximumSize(QtCore.QSize(21, 21))
        self.newfolder.setStyleSheet(_fromUtf8("border-style: flat;\n"
"background-image: url(:/images/newfolder.png);"))
        self.newfolder.setText(_fromUtf8(""))
        self.newfolder.setObjectName(_fromUtf8("newfolder"))
        self.horizontalLayout_3.addWidget(self.newfolder)
        self.delete_2 = QtGui.QToolButton(self.centralwidget)
        self.delete_2.setMinimumSize(QtCore.QSize(21, 21))
        self.delete_2.setMaximumSize(QtCore.QSize(21, 21))
        self.delete_2.setStyleSheet(_fromUtf8("border-style: flat;\n"
"background-image: url(:/images/delete.png);"))
        self.delete_2.setText(_fromUtf8(""))
        self.delete_2.setObjectName(_fromUtf8("delete_2"))
        self.horizontalLayout_3.addWidget(self.delete_2)
        self.recyclebin = QtGui.QToolButton(self.centralwidget)
        self.recyclebin.setMinimumSize(QtCore.QSize(21, 21))
        self.recyclebin.setMaximumSize(QtCore.QSize(21, 21))
        self.recyclebin.setStyleSheet(_fromUtf8("border-style: flat;\n"
"background-image: url(:/images/recyclebin.png);"))
        self.recyclebin.setText(_fromUtf8(""))
        self.recyclebin.setObjectName(_fromUtf8("recyclebin"))
        self.horizontalLayout_3.addWidget(self.recyclebin)
        self.iconMode = QtGui.QToolButton(self.centralwidget)
        self.iconMode.setMinimumSize(QtCore.QSize(21, 21))
        self.iconMode.setMaximumSize(QtCore.QSize(21, 21))
        self.iconMode.setStyleSheet(_fromUtf8("border-style: flat;\n"
"background-image: url(:/images/mode.png);"))
        self.iconMode.setText(_fromUtf8(""))
        self.iconMode.setObjectName(_fromUtf8("iconMode"))
        self.horizontalLayout_3.addWidget(self.iconMode)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(870, 40))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_4.setStyleSheet(_fromUtf8("background-color: rgb(32,117,218);\n"
"border-top-color: rgb(0, 0, 0);"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.conveylist = QtGui.QToolButton(self.frame_4)
        self.conveylist.setMinimumSize(QtCore.QSize(21, 21))
        self.conveylist.setMaximumSize(QtCore.QSize(21, 21))
        self.conveylist.setStyleSheet(_fromUtf8("background-image: url(:/images/conveylist.png);\n"
"border-style: flat;"))
        self.conveylist.setText(_fromUtf8(""))
        self.conveylist.setObjectName(_fromUtf8("conveylist"))
        self.horizontalLayout_4.addWidget(self.conveylist)
        self.conveylist_label = QtGui.QToolButton(self.frame_4)
        self.conveylist_label.setStyleSheet(_fromUtf8("border-style: flat;"))
        self.conveylist_label.setObjectName(_fromUtf8("conveylist_label"))
        self.horizontalLayout_4.addWidget(self.conveylist_label)
        self.progressBar = QtGui.QProgressBar(self.frame_4)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_4.addWidget(self.progressBar)
        spacerItem2 = QtGui.QSpacerItem(40, 17, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_5 = QtGui.QLabel(self.frame_4)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout_2.addWidget(self.frame_4)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "中科院云存储", None))
        self.label_2.setText(_translate("mainWindow", "云同步小分队", None))
        self.label_3.setText(_translate("mainWindow", "cloudteam", None))
        self.conveylist_label.setText(_translate("mainWindow", "传输列表", None))
        self.label_5.setText(_translate("mainWindow", "12.5G / 50G", None))

import resource_rc
