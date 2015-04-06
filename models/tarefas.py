# -*- coding: utf-8 -*-
from decimal import *
from models.model import Model

class Tarefas(Model):
	def __init__(self):
		super(Model, self).__init__()

		conn = self.getConn()
		cursor = conn.cursor()

		sql_verifica_tabela = """SELECT * FROM sqlite_master WHERE name ='tarefas' AND type='table'"""
		cursor.execute(sql_verifica_tabela)

		tabela = cursor.fetchone()
		conn.commit()

		if(tabela is None):
			sql = """CREATE TABLE 'tarefas' (
							'id_tarefa'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
							'tarefa'	NUMERIC NOT NULL,
							'descricao'	TEXT,
							'data_tarefa'	TEXT NOT NULL,
							'hora_inicio'	TEXT NOT NULL,
							'hora_final'	TEXT NOT NULL,
							'tempo_final'	TEXT
							)"""

			cursor.execute(sql)
			conn.commit()

	def listagem_tarefas(self):
		conn = self.getConn()
		cursor = conn.cursor()

		sql = "SELECT id_tarefa, tarefa, data_tarefa, hora_inicio, hora_final, tempo_final FROM tarefas ORDER BY id_tarefa DESC"
		cursor.execute(sql)
		tarefas = cursor.fetchall()
		conn.commit()

		return tarefas

	def busca_tarefas(self, id):
		conn = self.getConn()
		cursor = conn.cursor()

		sql = "SELECT * FROM tarefas WHERE id_tarefa = %d" % int(id)
		cursor.execute(sql)
		tarefa = cursor.fetchone()
		conn.commit()

		return tarefa

	def cadastrar_tarefa(self, dados):
		conn = self.getConn()
		cursor = conn.cursor()

		sql = "INSERT INTO tarefas(tarefa, descricao, data_tarefa, hora_inicio, hora_final, tempo_final) VALUES (%d,'%s','%s','%s','%s', '%s');" % (Decimal(dados[0]), dados[1], dados[2], dados[3], dados[4], dados[5])
		cursor.execute(sql)
		conn.commit()

	def alterar_tarefa(self, dados):
		conn = self.getConn()
		cursor = conn.cursor()

		sql = "UPDATE tarefas SET tarefa = %d, descricao = '%s', data_tarefa = '%s', hora_inicio = '%s', hora_final = '%s', tempo_final = '%s' WHERE id_tarefa = %d" % (Decimal(dados[1]), dados[2], dados[3], dados[4], dados[5], dados[6], int(dados[0]))
		cursor.execute(sql)
		conn.commit()

	def excluir_tarefa(self, id):
		conn = self.getConn()
		cursor = conn.cursor()

		sql = "DELETE FROM tarefas WHERE id_tarefa = %d" % int(id)
		cursor.execute(sql)
		conn.commit()