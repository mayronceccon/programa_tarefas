# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui
from controllers.qtPrincipal import qtPrincipal

if __name__ == "__main__":			
	app = QtGui.QApplication(sys.argv)
	f = qtPrincipal()
	f.show()
	sys.exit(app.exec_())