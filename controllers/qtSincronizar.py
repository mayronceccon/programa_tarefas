# -*- coding: utf-8 -*-
import gzip

from xmlrpc.client import ServerProxy, ProtocolError

from PyQt4 import QtGui
from views.FormSincronizar import Ui_qtSincronizar
from models.tarefas import Tarefas

class qtSincronizar(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_qtSincronizar()
        self.ui.setupUi(self)
        self.client()
           
    def client(self):
        proxy = ServerProxy("http://localhost:8000/")
       
        try:
            
            tarefas = Tarefas()
            lista_tarefas = tarefas.listagem_tarefas()

            result = proxy.salvar_tarefas(lista_tarefas)
            print(result)
            pass

        except ProtocolError as err:
            print("A protocol error occurred")
            print("URL: %s" % err.url)
            print("HTTP/HTTPS headers: %s" % err.headers)
            print("Error code: %d" % err.errcode)
            print("Error message: %s" % err.errmsg)