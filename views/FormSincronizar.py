# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/qtSincronizar.ui'
#
# Created: Wed Dec 10 10:18:29 2014
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

class Ui_qtSincronizar(object):
    def setupUi(self, qtSincronizar):
        qtSincronizar.setObjectName(_fromUtf8("qtSincronizar"))
        qtSincronizar.setWindowModality(QtCore.Qt.NonModal)
        qtSincronizar.resize(472, 176)
        self.centralwidget = QtGui.QWidget(qtSincronizar)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        qtSincronizar.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(qtSincronizar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        qtSincronizar.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(qtSincronizar)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        qtSincronizar.setStatusBar(self.statusbar)

        self.retranslateUi(qtSincronizar)
        QtCore.QMetaObject.connectSlotsByName(qtSincronizar)

    def retranslateUi(self, qtSincronizar):
        qtSincronizar.setWindowTitle(_translate("qtSincronizar", "Sincronizar", None))

