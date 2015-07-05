from PyQt4 import QtCore, QtGui, QtXml
from PyQt4.QtGui import * 
from PyQt4.QtCore import *

class TreeWidget(QtGui.QTreeWidget):
    def __init__(self, parent=None):
        super(TreeWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        #self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)

        self.setObjectName("treeWidget")
        self.setMinimumSize(QtCore.QSize(170, 425))
        self.setMaximumSize(QtCore.QSize(170, 65525))
        self.setGeometry(QtCore.QRect(10, 135, 170, 425))

        self.header().setResizeMode(QtGui.QHeaderView.Stretch)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.header().setResizeMode(QHeaderView.ResizeToContents)
        self.header().setStretchLastSection(False)
        self.header().hide()
        self.setHeaderLabels([""])
        self.setExpandsOnDoubleClick(True)
        self.domDocument = QtXml.QDomDocument()
        self.domElementForItem = {}
        self.folderIcon = QtGui.QIcon()
        self.bookmarkIcon = QtGui.QIcon()
        self.folderIcon.addPixmap(self.style().standardPixmap(QtGui.QStyle.SP_DirClosedIcon),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.folderIcon.addPixmap(self.style().standardPixmap(QtGui.QStyle.SP_DirOpenIcon),
                QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.bookmarkIcon.addPixmap(self.style().standardPixmap(QtGui.QStyle.SP_FileIcon))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(TreeWidget, self).dragEnterEvent(event)

    def dropEvent(self, event):
        item = self.itemAt(event.pos())
        if item:
            filepath = QtCore.QStringList()
            while(item is not None):
                filepath << item.text(0)
                item = item.parent()
		
            strpath = QtCore.QString()
            for i in reversed(range(0, filepath.count())):
                strpath += "/"
                strpath += filepath.takeAt(i)
            print "tree item path:" + strpath
        else:
            print "no target"                  
        
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                #print url.path()
                print "local file path:" + url.path()
            event.acceptProposedAction()
        else:
            super(TreeWidget,self).dropEvent(event)

    def mimeData(self, items):
        print 123456789
        data = QMimeData()
        urls = []
        for item in items:
            filepath = QtCore.QStringList()
            while(item is not None):
                filepath << item.text(0)
                item = item.parent()
            strpath = QtCore.QString()
            for i in reversed(range(0, filepath.count())):
                strpath += "/"
                strpath += filepath.takeAt(i)
            urls.append(QUrl.fromLocalFile(strpath))
            print "drag items:" + strpath
        return data 

    def read(self, device):     
        ok, errorStr, errorLine, errorColumn = self.domDocument.setContent(device, True)
        root = self.domDocument.documentElement()
        self.clear()
        # It might not be connected.
        try:
            self.itemChanged.disconnect(self.updateDomElement)
        except:
            pass
        child = root.firstChildElement('folder')
        while not child.isNull():
            self.parseFolderElement(child)
            child = child.nextSiblingElement('folder')
        self.itemChanged.connect(self.updateDomElement)
        return True

    def write(self, device):
        indentSize = 4
        out = QtCore.QTextStream(device)
        #self.domDocument.save(out, indentSize)
        return True

    def updateDomElement(self, item, column):
        element = self.domElementForItem.get(id(item))
            
    def parseFolderElement(self, element, parentItem=None):
        item = self.createItem(element, parentItem)
        title = element.firstChildElement('title').text()

        item.setFlags(item.flags() | Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDropEnabled | Qt.ItemIsDragEnabled)
        item.setIcon(0, self.folderIcon)
        item.setText(0, title)
        child = element.firstChildElement()
        while not child.isNull():
            if child.tagName() == 'folder':
                self.parseFolderElement(child, item)
            child = child.nextSiblingElement()

    def createItem(self, element, parentItem=None):
        item = QtGui.QTreeWidgetItem()
        if parentItem is not None:
            item = QtGui.QTreeWidgetItem(parentItem)
        else:
            item = QtGui.QTreeWidgetItem(self)
        self.domElementForItem[id(item)] = element
        
        return item

    

