# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore

import sys
import datetime
from decimal import *
from views.FormPrincipal import Ui_qtPrincipal
from models.tarefas import Tarefas
from controllers.qtSobre import qtSobre
from controllers.qtSincronizar import qtSincronizar

class qtPrincipal(QtGui.QMainWindow):

	conn = ""

	def __init__(self, parent=None):

		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_qtPrincipal()
		self.ui.setupUi(self)
		self.ui.campo_data_tarefa.setDateTime(QtCore.QDateTime.currentDateTime())
		self.listagem_tarefas()

	def listagem_tarefas(self):

		lista = self.ui.lista_tarefas
		lista.setRowCount(0);
		lista.clearContents()
		tarefas = Tarefas()
		lista_tarefas = tarefas.listagem_tarefas()

		label = ['ID', 'Tarefa', 'Data Tarefa', 'Hora Inicio', 'Hora Final', 'Tempo']

		for i in label:
			lista.removeColumn(label.index(i))
			lista.insertColumn(label.index(i))

		lista.setHorizontalHeaderLabels(label)

		linha = 0
		for row in lista_tarefas:
			coluna = 0
			lista.removeRow(linha)
			lista.insertRow(linha)
			for reg in lista_tarefas[linha]:
				item = QtGui.QTableWidgetItem()
				item.setText(str(reg))
				item.setFlags(QtCore.Qt.ItemIsEnabled)
				lista.setItem(linha,coluna,item)
				coluna = coluna + 1

			linha = linha + 1

		lista.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		lista.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
		lista.doubleClicked.connect(self.click_item)

	def click_item(self, mi):
		self.ui.btn_salvar_dados.setText('Alterar')
		self.ui.btn_excluir.setEnabled(True)

		campo_tarefa = self.ui.campo_tarefa
		campo_data_tarefa = self.ui.campo_data_tarefa
		campo_hora_inicio = self.ui.campo_hora_inicio
		campo_hora_final = self.ui.campo_hora_final
		campo_descricao = self.ui.campo_descricao_tarefa
		campo_id_tarefa = self.ui.campo_id_tarefa
		campo_total_horas = self.ui.campo_total_horas

		campo_tarefa.setFocus()

		row = mi.row()
		lista = self.ui.lista_tarefas
		id = lista.item(row, 0).text()
		tarefa = Tarefas()
		tarefa = tarefa.busca_tarefas(id)

		valor_id_tarefa = int(tarefa[0])
		valor_tarefa = str(tarefa[1])
		valor_descricao = str(tarefa[2])
		valor_data_tarefa = tarefa[3]

		valor_data_tarefa = valor_data_tarefa.split("/")		
		
		ano = int(valor_data_tarefa[2])
		mes = int(valor_data_tarefa[1])
		dia = int(valor_data_tarefa[0])

		valor_data_tarefa = QtCore.QDate(ano, mes, dia)
				
		valor_hora_inicio = tarefa[4]
		valor_hora_inicio = valor_hora_inicio.split(":")
		valor_inicio_antigo = valor_hora_inicio
		valor_hora_inicio = QtCore.QTime(int(valor_hora_inicio[0]),int(valor_hora_inicio[1]))

		valor_hora_final  = tarefa[5]
		valor_hora_final = valor_hora_final.split(":")
		valor_final_antigo = valor_hora_final
		valor_hora_final = QtCore.QTime(int(valor_hora_final[0]),int(valor_hora_final[1]))

		campo_id_tarefa.setText(str(valor_id_tarefa))
		campo_tarefa.setText(valor_tarefa)
		campo_data_tarefa.setDate(valor_data_tarefa)
		campo_hora_inicio.setTime(valor_hora_inicio)
		campo_hora_final.setTime(valor_hora_final)
		campo_descricao.setText(valor_descricao)

		hora_final = datetime.timedelta(minutes=int(valor_final_antigo[1]), hours=int(valor_final_antigo[0]))
		hora_inicial = datetime.timedelta(minutes=int(valor_inicio_antigo[1]), hours=int(valor_inicio_antigo[0]))

		if(hora_final > hora_inicial):
			diferenca_horas = str(hora_final - hora_inicial)
			direfenca_horas = diferenca_horas.split(":")
			campo_total_horas.setTime(QtCore.QTime(int(direfenca_horas[0]), int(direfenca_horas[1])))
		else:
			tempo = QtCore.QTime(0,0)
			campo_total_horas.setTime(tempo)

	def salvar_dados(self):

		self.ui.btn_salvar_dados.setText('Salvar')
		self.ui.btn_excluir.setEnabled(False)

		campo_tarefa = self.ui.campo_tarefa
		campo_data_tarefa = self.ui.campo_data_tarefa
		campo_hora_inicio = self.ui.campo_hora_inicio
		campo_hora_final = self.ui.campo_hora_final
		campo_descricao = self.ui.campo_descricao_tarefa
		campo_id_tarefa = self.ui.campo_id_tarefa
		campo_total_horas = self.ui.campo_total_horas

		campo_tarefa.setFocus()

		tarefa = campo_tarefa.text()
		data_tarefa = campo_data_tarefa.text()
		hora_inicio = campo_hora_inicio.text()
		hora_final = campo_hora_final.text()
		descricao = campo_descricao.text()
		id_tarefa = campo_id_tarefa.text()

		valor_hora_inicio = hora_inicio
		valor_hora_inicio = valor_hora_inicio.split(":")

		valor_hora_final  = hora_final
		valor_hora_final = valor_hora_final.split(":")

		hora_final_total = datetime.timedelta(minutes=int(valor_hora_final[1]), hours=int(valor_hora_final[0]))
		hora_inicial_total = datetime.timedelta(minutes=int(valor_hora_inicio[1]), hours=int(valor_hora_inicio[0]))

		total_horas = str(hora_final_total - hora_inicial_total);

		if tarefa != "" and hora_inicio != "" and hora_final != "":
			
			tarefas = Tarefas()
			if id_tarefa == "":
				dados = (tarefa, descricao, data_tarefa, hora_inicio, hora_final, total_horas)
				tarefas.cadastrar_tarefa(dados)
			else:
				dados = (id_tarefa, tarefa, descricao, data_tarefa, hora_inicio, hora_final, total_horas)
				tarefas.alterar_tarefa(dados)

			tempo = QtCore.QTime(0,0)
			campo_tarefa.clear()
			campo_data_tarefa.setDateTime(QtCore.QDateTime.currentDateTime())
			campo_hora_inicio.setTime(tempo);
			campo_hora_final.setTime(tempo);
			campo_total_horas.setTime(tempo)
			campo_id_tarefa.clear()
			campo_descricao.clear();

			self.listagem_tarefas()

	def excluir_dados(self):

		excluir = QtGui.QMessageBox.question(self, 'Message', 'Deseja excluir a tarefa selecionada?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

		if excluir == QtGui.QMessageBox.Yes:
			campo_id_tarefa = self.ui.campo_id_tarefa
			id_tarefa = campo_id_tarefa.text()
			tarefas = Tarefas()
			tarefas.excluir_tarefa(id_tarefa)

		campo_tarefa = self.ui.campo_tarefa
		campo_data_tarefa = self.ui.campo_data_tarefa
		campo_hora_inicio = self.ui.campo_hora_inicio
		campo_hora_final = self.ui.campo_hora_final
		campo_descricao = self.ui.campo_descricao_tarefa
		campo_id_tarefa = self.ui.campo_id_tarefa
		campo_total_horas = self.ui.campo_total_horas

		campo_tarefa.setFocus()

		tempo = QtCore.QTime(0,0)
		campo_tarefa.clear()
		campo_data_tarefa.setDateTime(QtCore.QDateTime.currentDateTime())
		campo_hora_inicio.setTime(tempo);
		campo_hora_final.setTime(tempo);
		campo_total_horas.setTime(tempo)
		campo_id_tarefa.clear()
		campo_descricao.clear();

		self.ui.btn_salvar_dados.setText('Salvar')
		self.ui.btn_excluir.setEnabled(False)

		self.listagem_tarefas()

	def abrir_sobre(self):
		f = qtSobre(self)
		f.show()

	def abrir_sincronizacao(self):
		f = qtSincronizar(self)
		f.show()