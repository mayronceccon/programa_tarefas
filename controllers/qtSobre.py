# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from views.FormSobre import Ui_qtSobre

class qtSobre(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_qtSobre()
        self.ui.setupUi(self)