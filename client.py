#!/usr/bin/python
# -*- coding: utf-8 -*-


# imports a lot of modules

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from singleton import *
from net.queue_controller import *
import sys
from NEW_XML_UI import get_xml_ui
from New_XML_T import get_xml_t
from login import *

if __name__ == "__main__":
    q_controller = queue_controller()
    q_controller.queue_exec()
    get_xml_ui()
    get_xml_t()
    # starting QT application
    app = QApplication(sys.argv)
    import main
    # me = SingleInstance()
    # dialog = login()
    # dialog.show()
    app.exec_()
