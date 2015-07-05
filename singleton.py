# -*- coding: utf-8 -*-

import sys
import os
import errno
import tempfile
import unittest
import logging
from multiprocessing import Process
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class SingleInstance:

    def __init__(self, flavor_id=""):
        import sys
        self.initialized = False
        basename = os.path.splitext(os.path.abspath(sys.argv[0]))[0].replace(
            "/", "-").replace(":", "").replace("\\", "-") + '-%s' % flavor_id + '.lock'
        self.lockfile = os.path.normpath(
            tempfile.gettempdir() + '/' + basename)

        logger.debug("SingleInstance lockfile: " + self.lockfile)
        if sys.platform == 'win32':
            try:
                if os.path.exists(self.lockfile):
                    os.unlink(self.lockfile)
                self.fd = os.open(
                    self.lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            except OSError:
                type, e, tb = sys.exc_info()
                if e.errno == 13:
                    logger.error(
                        "Another instance is already running, quitting.")
                    QMessageBox.information(None, u"信息提示", u"程序已经在运行！")
                    sys.exit(-1)
                print(e.errno)
                raise
        else:  # non Windows
            import fcntl
            self.fp = open(self.lockfile, 'w')
            try:
                fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except IOError:
                logger.warning(
                    "Another instance is already running, quitting.")
                QMessageBox.information(None, u"信息提示", u"程序已经在运行！")
                sys.exit(-1)
        self.initialized = True

    def __del__(self):
        import sys
        import os
        if not self.initialized:
            return
        try:
            if sys.platform == 'win32':
                if hasattr(self, 'fd'):
                    os.close(self.fd)
                    os.unlink(self.lockfile)
            else:
                import fcntl
                fcntl.lockf(self.fp, fcntl.LOCK_UN)
                # os.close(self.fp)
                if os.path.isfile(self.lockfile):
                    os.unlink(self.lockfile)
        except Exception as e:
            if logger:
                logger.warning(e)
            else:
                print("Unloggable error: %s" % e)
            sys.exit(-1)


def f(name):
    tmp = logger.level
    logger.setLevel(logging.CRITICAL)  # we do not want to see the warning
    me2 = SingleInstance(flavor_id=name)
    logger.setLevel(tmp)
    pass

logger = logging.getLogger("tendo.singleton")
logger.addHandler(logging.StreamHandler())

if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    unittest.main()
