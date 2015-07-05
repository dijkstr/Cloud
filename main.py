#!/usr/bin/python
# -*-coding:utf-8-*-
import sip
import os
# sip.setapi('QVariant', 2)
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, QtDBus, QtXml
import sys, threading, time, codecs, random
import ui.ui_main, ui.conveylist, ui.ctrl_safebox_login, ui.new_folder, ui.re_name, TreeWidget, listwidget, FileDialog, \
    main_win_right, systray_icon
import domfilexml, config_main_win
from ui.ui_main import Ui_mainWindow
from domChangeXML import *
from net.queue_controller import *
import net.global_vars

reload(sys)
sys.setdefaultencoding("utf-8")
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf-8"))


class Main(QtGui.QMainWindow, ui.ui_main.Ui_mainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.conf = config_main_win.config_main_win()
        self.items = []
        self.choseitems = []
        self.domfile = domfilexml.domfilexml()
        self.safebox = ui.ctrl_safebox_login.ctrl_safebox_login()
        self.new_folder = ui.new_folder.new_folder()
        self.re_name = ui.re_name.re_name()

        self.array = self.domfile.create_array()

        self.setupUi(self)
        self.progressBar.setValue(25)
        # self.clean_timer = QtCore.QTimer()
        self.treeWidget = TreeWidget.TreeWidget(self.centralwidget)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.listwidget = listwidget.listwidget(self.centralwidget)

        self.Tenant_id = "CloudTeam"
        self.Token_id = "yuntongbu"
        self.current_item_name = None
        self.listmode = self.conf.listmode
        self.iconmode = self.conf.iconmode
        self.zero = self.conf.zero
        self.one = self.conf.one
        self.two = self.conf.two
        self.current_path = self.domfile.current_path
        self.ui_flag = self.iconmode
        self.mode_UI = "save"
        self.display()
        self.mw_right = main_win_right.main_win_right()
        self.display_path()
        self.old_item_name = None

        self.none.addItem(QtGui.QIcon(':/images/bad.svg'), "Bad")
        self.none.addItem(QtGui.QIcon(':/images/yun.jpg'), "yun")
        self.createActions()
        self.createTrayIcon()
        self.none.currentIndexChanged.connect(self.setIcon)
        self.none.setCurrentIndex(1)
        self.trayIcon.show()

        self.convey = ui.conveylist.conveylist()
        self.filedialog = FileDialog.FileDialog()

        self.connect(self.delete_2, SIGNAL("clicked()"), self.delete_sure)
        self.connect(self.newfolder, QtCore.SIGNAL("clicked()"), self.name_newfolder)
        self.connect(self.refresh, QtCore.SIGNAL("clicked()"), self.refresh_)
        self.connect(self.back, QtCore.SIGNAL("clicked()"), self.back_)
        self.connect(self.forward, QtCore.SIGNAL("clicked()"), self.forward_)
        self.connect(self.iconMode, QtCore.SIGNAL("clicked()"), self.change_mode)
        self.connect(self.home, QtCore.SIGNAL("clicked()"), self.root_path_)
        self.connect(self.recyclebin, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("recycleBin_onClicked()"))

        self.connect(self.treeWidget, QtCore.SIGNAL("itemClicked(QTreeWidgetItem*,int)"), self,
                     QtCore.SLOT("curritem_onclicked()"))
        # self.action_conveylist.triggered.connect(self.dlg_conveylist_oncliecked)
        self.connect(self.conveylist, SIGNAL("clicked()"), self, QtCore.SLOT("dlg_conveylist_oncliecked()"))
        self.connect(self.conveylist_label, SIGNAL("clicked()"), self, QtCore.SLOT("dlg_conveylist_oncliecked()"))
        self.connect(self.upload, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("upload_onClicked()"))
        self.connect(self.download, SIGNAL("clicked()"), self, QtCore.SLOT("slot_download()"))
        self.connect(self.bao, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("safebox_onClicked()"))
        self.connect(self.bei, QtCore.SIGNAL("clicked()"), self.set_mode_save)

        self.mw_right.action_b1.triggered.connect(self.upload_onClicked)
        self.mw_right.action_b2.triggered.connect(self.name_newfolder)
        self.mw_right.action_b3.triggered.connect(self.pasty)
        self.mw_right.action_b4.triggered.connect(self.refresh_)
        self.mw_right.action_b5.triggered.connect(self.property_)
        self.mw_right.action_f1.triggered.connect(self.slot_enter_icon)
        self.mw_right.action_f2.triggered.connect(self.slot_download)
        self.mw_right.action_f3.triggered.connect(self.toSafeBox)
        self.mw_right.action_f4.triggered.connect(self.moveto)
        self.mw_right.action_f5.triggered.connect(self.copy)
        self.mw_right.action_f6.triggered.connect(self.cut)
        self.mw_right.action_f7.triggered.connect(self.rename)
        self.mw_right.action_f8.triggered.connect(self.delete_sure)
        self.mw_right.action_f0.triggered.connect(self.getfileattr)

        self.connect(self.listwidget, QtCore.SIGNAL("itemChanged(QListWidgetItem*)"),
                     self.slot_rename)
        self.connect(self.listwidget, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.slot_enter_icon)
        self.connect(self.listwidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), self.slot_item_icon)
        self.connect(self.textEdit, QtCore.SIGNAL("editingFinished()"), self.change_path)
        # 右侧右键单击信号槽
        self.listwidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listwidget.customContextMenuRequested[QtCore.QPoint].connect(self.myListWidgetContext_icon)

    ##等待完善
    def pasty(self):
        QMessageBox.information(self, "Message", self.tr("   等待完善~    "))

    def property_(self):
        QMessageBox.information(self, "Message", self.tr("   等待完善~    "))

    def toSafeBox(self):
        QMessageBox.information(self, "Message", self.tr("   等待完善~    "))

    def cut(self):
        QMessageBox.information(self, "Message", self.tr("   等待完善~    "))

    def forward_(self):
        QMessageBox.information(self, "Message", self.tr("   等待完善~    "))

    @QtCore.pyqtSlot()
    def dlg_conveylist_oncliecked(self):
        convey = self.convey
        convey.exec_()

    @QtCore.pyqtSlot()
    def recycleBin_onClicked(self):
        QMessageBox.information(self, "Message", self.tr("   等待完善~    "))

    @QtCore.pyqtSlot()
    def upload_onClicked(self):
        # dialog = self.filedialog
        s = str(self.filedialog.getOpenFileName(self, "Open File"))
        print s
        request = '-X GET -H "X-Auth-Token: " "http://' + self.conf.ip + ':443/v1/AUTH_glfs' + self.current_path + s[
                                                                                                                   s.rfind(
                                                                                                                       "/"):] + '?fype=f&type=NORMAL -o ' + str(
            s)
        url = "http://" + self.conf.ip + ":443/v1/AUTH_glfs" + self.current_path + s[s.rfind(
            "/"):] + "?fype=f&type=NORMAL"
        q = q_send_item(url, request, "upload")
        global_vars.q_send.put(q)
        print "request", request

    @QtCore.pyqtSlot()
    def slot_download(self):
        if self.listwidget.selectedItems():
            s = QFileDialog.getExistingDirectory(self, "Open Directory", "/home",
                                                 QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
            if s:
                for it in self.items:
                    request = '-X GET -H "X-Auth-Token: " "http://' + self.conf.ip + ':443/v1/AUTH_glfs' + self.current_path + it.text() + '?fype=f&type=NORMAL" -o ' + str(
                        s) + it.text()
                    url = "http://" + self.conf.ip + ":443/v1/AUTH_glfs" + self.current_path + it.text() + "?fype=f&type=NORMAL"
                    q = q_send_item(url, request, "download")
                    global_vars.q_send.put(q)
                    # print "request",request
        else:
            QtGui.QMessageBox.warning(self, self.tr("警告"), self.tr("请选择文件"))

    @QtCore.pyqtSlot()
    def safebox_onClicked(self):
        dialog = self.safebox
        dialog.exec_()

    def set_mode_save(self):
        self.mode_UI = "save"
        self.curritem_onclicked()
        self.refresh_()

    # 单击文件
    def slot_item_icon(self, item):
        item = self.listwidget.currentItem()
        self.items.append(item)

    # 双击文件
    def slot_enter_icon(self, item):
        dict_item = self.findpath(item.text())
        path = dict_item["path"]
        item_type = dict_item["type_"]
        parser = self.domfile
        if (item_type == "folder"):
            parser.itemlist.clear()
            parser.search_file(path, self.mode_UI)
            self.array = parser.create_array()
            self.current_path = parser.current_path
            self.display_path()
            self.display()
            self.refresh_()

    # rename文件
    def slot_rename(self, currentitem):
        if self.old_item_name != None and str(currentitem.text()) == '':
            QMessageBox.information(self, "Message", self.tr("错误!"))
            currentitem.setText(QtCore.QString(self.old_item_name))
            self.old_item_name = None
        if self.old_item_name != None and self.old_item_name != str(currentitem.text()):
            for folder_char in str(currentitem.text()):
                if folder_char in self.conf.folder_forbidden_charsets:
                    QMessageBox.information(self, self.tr("信息提示"), self.tr('不合法的字符：\ / : * ? " < > |'))
                    currentitem.setText(QtCore.QString(self.old_item_name))
                    self.old_item_name = None
                    return
            PATH = self.current_path + '/' + self.old_item_name
            newname = currentitem.text()
            NEW_PATH = self.current_path + '/' + newname
            if not self.domfile.rename_node(QtCore.QString(self.old_item_name), newname, self.mode_UI):
                QMessageBox.information(self, "Message", self.tr("当前目录已存在该文件夹!"))
                currentitem.setText(QtCore.QString(self.old_item_name))
                self.old_item_name = None
                return
            parser = self.domfile
            request = '-i -X PUT  -H "X-Auth-Token: " -H "Destination: ' + str(
                NEW_PATH) + '"  "http://' + self.conf.ip + ':443/v1/AUTH_glfs"' + str(
                PATH) + '"?op=RENAME&ftype=d&type=NORMAL"'
            url = "http://" + self.conf.ip + ":443/v1/AUTH_glfs" + str(PATH) + "?op=RENAME&ftype=d&type=NORMAL"
            q = q_send_item(url, request, "rename")
            global_vars.q_send.put(q)
            while (1):
                if not global_vars.q_recv.empty():
                    recv_message = global_vars.q_recv.get()
                    break
                    # print 'new****'+recv_message.response
            if recv_message.response.find("20"):
                parser.itemlist.clear()
                parser.search_file(self.current_path, self.mode_UI)
                self.array = self.domfile.create_array()
                self.display()
                self.refresh_()
            else:
                QMessageBox.information(self, "Message", self.tr("重命名失败!"))
                currentitem.setText(self.old_item_name)
            self.old_item_name = None

    @QtCore.pyqtSlot()
    def curritem_onclicked(self):
        item = self.treeWidget.currentItem()
        filepath = QtCore.QStringList()
        while (item is not None):
            filepath << item.text(0)
            item = item.parent()

        strpath = QtCore.QString()
        for i in reversed(range(0, filepath.count())):
            strpath += "/"
            strpath += filepath.takeAt(i)
        print strpath
        if strpath == "":
            strpath = "/include"

        parser = self.domfile
        parser.itemlist.clear()
        parser.search_file(strpath, self.mode_UI)
        self.array = parser.create_array()
        self.current_path = strpath
        self.display_path()
        self.listwidget.ui_listwidget(self.array, self.horizontalLayout)

    def open(self, filestr):
        inFile = QtCore.QFile(filestr)
        if not inFile.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            QtGui.QMessageBox.warning(self, "DOM Bookmarks",
                                      "Cannot read file %s:\n%s." % (fileName, inFile.errorString()))
            return

        if self.treeWidget.read(inFile):
            self.statusBar().showMessage("File loaded", 2000)

    # display方法
    def display(self):
        changeXML()
        if (self.ui_flag == self.iconmode):
            self.listwidget.seticonmode()
            self.listwidget.ui_listwidget(self.array, self.horizontalLayout)
        else:
            self.listwidget.setlistmode()
            self.listwidget.ui_listwidget(self.array, self.horizontalLayout)

    def change_path(self):
        print self.textEdit.text()
        if (self.topath(self.current_path)):
            self.current_path = self.textEdit.text()
            self.display_path()
            self.display()
            self.refresh_()
        else:
            print self.current_path
            print "error"

    # 路径显示
    def display_path(self):
        # self.textEdit.setEnabled(False)
        self.textEdit.setText(self.current_path)

    # 根路径
    def root_path_(self):
        path_array = self.current_path.split('/')
        if (len(path_array) > self.one):
            self.current_path = path_array[self.zero] + "/" + path_array[self.one]
            self.display_path()
            self.topath(self.current_path)
            self.display()
            self.refresh_()

    # 动态拖动事件
    def resizeEvent(self, resizeEvent):
        self.display()
        self.refresh_()

    # 刷新
    def refresh_(self):
        self.display_path()
        self.display()
        self.open("dirtree.xml")

    # 回退
    def back_(self):
        path_array = self.current_path.split('/')
        if (len(path_array) > self.one):
            lenght = len(self.current_path) - len("/" + path_array[len(path_array) - self.one])
            self.current_path = self.current_path[self.zero:lenght]
            self.display_path()
            self.topath(self.current_path)
            self.display()
            self.refresh_()

    # 弹出输入新建文件夹名称的方法的窗口
    @QtCore.pyqtSlot()
    def name_newfolder(self):
        dialog = self.new_folder
        if dialog.exec_():
            self.newname = dialog.name()
            print "http://IP:Port/vl/AUTH_{%s}/%s?op=MKDIRS[&type=%s]" % (
                self.Tenant_id, self.current_path, self.mode_UI)
            print "X-Auth-Token:%s" % (self.Token_id)
            self.create_folder(self.newname)
            # 新建完毕后清空foldername
            self.newname = None
            dialog.clear_edit()

    # 改变显示模式
    def change_mode(self):
        if (self.ui_flag == 1):
            self.ui_flag = 0
            self.display()
            self.refresh_()
        else:
            self.ui_flag = 1
            self.display()
            self.refresh_()

    # 新建文件夹
    def create_folder(self, newname):
        for folder_char in str(newname):
            if folder_char in self.conf.folder_forbidden_charsets:
                QMessageBox.information(self, self.tr("信息提示"), self.tr('不合法的字符：\ / : * ? " < > |'))
                return
        PATH = self.current_path + '/' + newname
        print "path:", PATH
        time_ = time.strftime('%a %b  %d %H:%M:%S %Y', time.localtime(time.time()))
        if not self.domfile.create_node(time_, newname, self.mode_UI):
            QMessageBox.information(self, "Message", self.tr("当前目录已存在该文件夹!"))
            return
        parser = self.domfile
        request = '-i -X PUT  -H "X-Auth-Token: "  "http://' + self.conf.ip + ':443/v1/AUTH_glfs"' + str(
            PATH) + '"?op=MKDIRS&ftype=d&type=NORMAL"'
        url = "http://" + self.conf.ip + ":443/v1/AUTH_glfs" + str(PATH) + "?op=MKDIRS&ftype=d&type=NORMAL"
        q = q_send_item(url, request, "mkdir")
        global_vars.q_send.put(q)
        while (1):
            if not global_vars.q_recv.empty():
                recv_message = global_vars.q_recv.get()
                break
        # print 'new****'+recv_message.response
        if recv_message.response.find("20"):
            parser.itemlist.clear()
            parser.search_file(self.current_path, self.mode_UI)
            self.array = self.domfile.create_array()
            self.display()
            self.refresh_()
        else:
            QMessageBox.information(self, "Message", self.tr("错误!"))

    # 移动到
    def moveto(self):
        destination = "/root"
        list_item = self.listwidget.selectedItems()
        item = list_item[self.zero]
        if (len(list_item) > self.one):
            for item in list_item:
                print  "from" + self.current_path + "/" + item.text()
                print  "to" + destination + "/" + list_item[self.zero].text()
            print "http://IP:Port/vl/AUTH_{%s}/batch?op=MOVE[&type=%s]" % (self.Tenant_id, self.mode_UI)
            print "X-Auth-Token:%s" % (self.Token_id)
        else:
            print "http://IP:Port/vl/AUTH_{%s}/%s/%s?op=MOVE[&recursive=false][&type=%s]" % (
                self.Tenant_id, self.current_path, list_item[self.zero].text(), self.mode_UI)
            print "X-Auth-Token:%s" % (self.Token_id)
            print "Destination:%s/%s" % (destination, list_item[self.zero].text())

    # 复制
    def copy(self):
        destination = "/root"
        list_item = self.listwidget.selectedItems()
        item = list_item[self.zero]
        if (len(list_item) > self.one):
            for item in list_item:
                print  "from" + self.current_path + "/" + item.text()
                print  "to" + destination + "/" + list_item[self.zero].text()
            print "http://IP:Port/vl/AUTH_{%s}/batch?op=COPY[&type=%s]" % (self.Tenant_id, self.mode_UI)
            print "X-Auth-Token:%s" % (self.Token_id)
        else:
            print "http://IP:Port/vl/AUTH_{%s}/%s/%s?op=COPY[&type=%s]" % (
                self.Tenant_id, self.current_path, list_item[self.zero].text(), self.mode_UI)
            print "X-Auth-Token:%s" % (self.Token_id)
            print "Destination:%s/%s" % (destination, list_item[self.zero].text())

    # 属性
    def getfileattr(self):
        list_item = self.listwidget.selectedItems()
        item = list_item[self.zero]
        print "http://IP:Port/vl/AUTH_{%s}/%s/%s?op=GETFILEATTR[&type=%s][&version=LATEST]" % (
            self.Tenant_id, self.current_path, list_item[self.zero].text(), self.mode_UI)
        print "X-Auth-Token:%s" % (self.Token_id)

    # 重命名
    def rename(self):
        list_item = self.listwidget.currentItem()
        list_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsEditable)
        self.listwidget.editItem(list_item)
        list_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
        self.old_item_name = list_item.text()

    # 删除文件确认
    def delete_sure(self):
        list_item = self.listwidget.selectedItems()
        if self.current_item_name == None and list_item == None:
            self.error()
        else:
            button = QMessageBox.question(self, "Warning", self.tr("是否确定删除文件/文件夹？"),
                                          QMessageBox.Ok | QMessageBox.Cancel)
            if button == QMessageBox.Ok:
                # self.label.setText("Question button/Ok")
                self.delete_onClicked()
            elif button == QMessageBox.Cancel:
                # self.label.setText("Question button/Cancel")
                pass

    # 删除文件
    @QtCore.pyqtSlot()
    def delete_onClicked(self):
        list_item = self.listwidget.selectedItems()
        if (len(list_item) > self.one):
            for item in list_item:
                print  self.current_path + "/" + item.text()
            print "http://IP:Port/vl/AUTH_{%s}/batch?op=DELETE[&recursive=false][&type=%s]" % (
                self.Tenant_id, self.mode_UI)
            print "X-Auth-Token:%s" % (self.Token_id)
        else:
            print "http://IP:Port/vl/AUTH_{%s}/%s/%s?op=DELETE[&recursive=false][&type=%s]" % (
                self.Tenant_id, self.current_path, list_item[self.zero].text(), self.mode_UI)
            print "X-Auth-Token:%s" % (self.Token_id)
        parser = self.domfile
        # ！！！！！！！！
        list_item = self.listwidget.selectedItems()
        for item in list_item:
            self.current_item_name = item.text()
        parser.delete_node(self.current_item_name, self.mode_UI)
        request = '-i -X DELETE -H "X-Auth-Token: " http://' + self.conf.ip + ':443/v1/AUTH_glfs' + str(
            self.current_path) + "/" + str(self.current_item_name)
        url = 'http://' + self.conf.ip + ':443/v1/AUTH_glfs/' + str(self.current_path) + "/" + str(
            self.current_item_name)
        q = q_send_item(url, request, "delete")
        global_vars.q_send.put(q)
        while (1):
            if not global_vars.q_recv.empty():
                recv_message = global_vars.q_recv.get()
                break
        # print 'delete****'+recv_message.response
        if recv_message.response.find("20"):
            parser.itemlist.clear()
            parser.search_file(self.current_path, self.mode_UI)
            self.array = self.domfile.create_array()
            self.display()
            self.refresh_()
            self.current_item_name = None
        else:
            QMessageBox.information(self, "Message", self.tr("错误!"))

    # 获得文件路径
    def findpath(self, name):
        dict_item = {}
        for i in self.array:
            if (name == i["name"]):
                dict_item = i
        return dict_item

    def myListWidgetContext_icon(self, point):
        try:
            item = self.listwidget.itemAt(point)
            print "item:" + item.text()
            if (item.text() == ""):
                self.mw_right.popMenu.exec_(QtGui.QCursor.pos())
            else:
                self.mw_right.popMenu_file.exec_(QtGui.QCursor.pos())
        except:
            self.mw_right.popMenu.exec_(QtGui.QCursor.pos())

    # 重载文件队列
    def topath(self, path):
        parser = self.domfile
        parser.itemlist.clear()
        parser.search_file(path, self.mode_UI)
        if (parser.create_array() != None):
            self.array = parser.create_array()
            return True
        else:
            return False

    ## 最小化
    def setVisible(self, visible):
        self.restoreAction.setEnabled(self.isMaximized() or not visible)
        super(Main, self).setVisible(visible)

    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            self.hide()
            event.ignore()

    def setIcon(self, index):
        icon = self.none.itemIcon(index)
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)
        self.trayIcon.setToolTip(self.none.itemText(index))

    def createActions(self):
        self.restoreAction = QtGui.QAction("&Restore", self,
                                           triggered=self.showNormal)
        self.quitAction = QtGui.QAction("&Quit", self,
                                        triggered=QtGui.qApp.quit)

    def createTrayIcon(self):
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

app = QApplication(sys.argv)
ui_icon = Main()
ui_icon.show()
ui_icon.open("dirtree.xml")
app.exec_()
