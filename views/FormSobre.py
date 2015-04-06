# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/qtSobre.ui'
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

class Ui_qtSobre(object):
    def setupUi(self, qtSobre):
        qtSobre.setObjectName(_fromUtf8("qtSobre"))
        qtSobre.resize(400, 212)
        self.groupBox = QtGui.QGroupBox(qtSobre)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 191))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textBrowser = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 361, 161))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(qtSobre)
        QtCore.QMetaObject.connectSlotsByName(qtSobre)

    def retranslateUi(self, qtSobre):
        qtSobre.setWindowTitle(_translate("qtSobre", "Sobre", None))
        self.groupBox.setTitle(_translate("qtSobre", "Sobre", None))
        self.textBrowser.setHtml(_translate("qtSobre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Helvetica,sans\'; font-size:8pt; color:#000000;\">    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam posuere, leo non hendrerit lobortis, eros nisl sodales nisl, sit amet volutpat sapien mauris eu eros. Morbi ante tortor, imperdiet nec dapibus a, interdum in nulla. Nulla luctus fermentum arcu, non porttitor sapien gravida et. Ut a venenatis dui.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Helvetica,sans\'; font-size:8pt; color:#000000;\">    Suspendisse blandit enim at viverra gravida. Cras id sollicitudin felis, vel bibendum eros. Vivamus eleifend enim sed sapien facilisis egestas. Aliquam laoreet mi eu nunc placerat imperdiet. Suspendisse lectus magna, cursus et massa eget, euismod porta lectus. Sed porta nisi vitae aliquam sollicitudin.</span></p></body></html>", None))

