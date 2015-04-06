# -*- coding: utf-8 -*-
import os
import sqlite3
from PyQt4 import QtSql, QtGui

class Conexao(object):
	
	conn = None
	
	def conexao__(self):

		path_tarefa = os.path.expanduser("~/.tarefas/")

		if(not os.path.exists(path_tarefa)):
			os.makedirs(path_tarefa)

		path_db = path_tarefa + "database.sqlite"

		if(not os.path.isfile(path_tarefa + "database.sqlite")):
			arq = open(path_db, "w")
			arq.close()		
		
		db = QtSql.QSqlDatabase.addDatabase("QSQLITE");
		db.setDatabaseName(path_db);
		ok = db.open()    
		if not ok:
			QtGui.QMessageBox.warning(self, "Error", "Invalid database!")
			return
	
	def getConn(self):
		return self.conn
	
	def __init__(self):

		path_tarefa = os.path.expanduser("~/.tarefas/")

		if(not os.path.exists(path_tarefa)):
			os.makedirs(path_tarefa)

		path_db = path_tarefa + "database.sqlite"

		if(not os.path.isfile(path_tarefa + "database.sqlite")):
			arq = open(path_db, "w")
			arq.close()

		self.conn = sqlite3.connect(path_db)		