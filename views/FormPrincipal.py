# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/qtPrincipal.ui'
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

class Ui_qtPrincipal(object):
    def setupUi(self, qtPrincipal):
        qtPrincipal.setObjectName(_fromUtf8("qtPrincipal"))
        qtPrincipal.resize(647, 558)
        self.qtPrincipalForm = QtGui.QWidget(qtPrincipal)
        self.qtPrincipalForm.setObjectName(_fromUtf8("qtPrincipalForm"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.qtPrincipalForm)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(240, 10, 171, 95))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.campo_hora_inicio = QtGui.QTimeEdit(self.gridLayoutWidget_2)
        self.campo_hora_inicio.setObjectName(_fromUtf8("campo_hora_inicio"))
        self.gridLayout_2.addWidget(self.campo_hora_inicio, 1, 1, 1, 1)
        self.label_hora_final = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_hora_final.setObjectName(_fromUtf8("label_hora_final"))
        self.gridLayout_2.addWidget(self.label_hora_final, 2, 0, 1, 1)
        self.campo_hora_final = QtGui.QTimeEdit(self.gridLayoutWidget_2)
        self.campo_hora_final.setObjectName(_fromUtf8("campo_hora_final"))
        self.gridLayout_2.addWidget(self.campo_hora_final, 2, 1, 1, 1)
        self.label_total = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_total.setObjectName(_fromUtf8("label_total"))
        self.gridLayout_2.addWidget(self.label_total, 3, 0, 1, 1)
        self.campo_total_horas = QtGui.QTimeEdit(self.gridLayoutWidget_2)
        self.campo_total_horas.setReadOnly(True)
        self.campo_total_horas.setObjectName(_fromUtf8("campo_total_horas"))
        self.gridLayout_2.addWidget(self.campo_total_horas, 3, 1, 1, 1)
        self.label_hora_inicio = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_hora_inicio.setObjectName(_fromUtf8("label_hora_inicio"))
        self.gridLayout_2.addWidget(self.label_hora_inicio, 1, 0, 1, 1)
        self.gridLayoutWidget_3 = QtGui.QWidget(self.qtPrincipalForm)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 110, 611, 29))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.campo_descricao_tarefa = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.campo_descricao_tarefa.setObjectName(_fromUtf8("campo_descricao_tarefa"))
        self.gridLayout_3.addWidget(self.campo_descricao_tarefa, 1, 1, 1, 1)
        self.btn_salvar_dados = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.btn_salvar_dados.setObjectName(_fromUtf8("btn_salvar_dados"))
        self.gridLayout_3.addWidget(self.btn_salvar_dados, 1, 2, 1, 1)
        self.label_descricao_tarefa = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_descricao_tarefa.setObjectName(_fromUtf8("label_descricao_tarefa"))
        self.gridLayout_3.addWidget(self.label_descricao_tarefa, 1, 0, 1, 1)
        self.gridLayoutWidget = QtGui.QWidget(self.qtPrincipalForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 202, 62))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_id_tarefa = QtGui.QLabel(self.gridLayoutWidget)
        self.label_id_tarefa.setObjectName(_fromUtf8("label_id_tarefa"))
        self.gridLayout.addWidget(self.label_id_tarefa, 0, 0, 1, 1)
        self.campo_data_tarefa = QtGui.QDateEdit(self.gridLayoutWidget)
        self.campo_data_tarefa.setEnabled(True)
        self.campo_data_tarefa.setSpecialValueText(_fromUtf8(""))
        self.campo_data_tarefa.setAccelerated(False)
        self.campo_data_tarefa.setKeyboardTracking(True)
        self.campo_data_tarefa.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.campo_data_tarefa.setCalendarPopup(True)
        self.campo_data_tarefa.setTimeSpec(QtCore.Qt.LocalTime)
        self.campo_data_tarefa.setObjectName(_fromUtf8("campo_data_tarefa"))
        self.gridLayout.addWidget(self.campo_data_tarefa, 1, 1, 1, 1)
        self.label_data_tarefa = QtGui.QLabel(self.gridLayoutWidget)
        self.label_data_tarefa.setObjectName(_fromUtf8("label_data_tarefa"))
        self.gridLayout.addWidget(self.label_data_tarefa, 1, 0, 1, 1)
        self.campo_tarefa = QtGui.QLineEdit(self.gridLayoutWidget)
        self.campo_tarefa.setText(_fromUtf8(""))
        self.campo_tarefa.setMaxLength(9)
        self.campo_tarefa.setFrame(True)
        self.campo_tarefa.setEchoMode(QtGui.QLineEdit.Normal)
        self.campo_tarefa.setCursorPosition(0)
        self.campo_tarefa.setDragEnabled(False)
        self.campo_tarefa.setPlaceholderText(_fromUtf8(""))
        self.campo_tarefa.setObjectName(_fromUtf8("campo_tarefa"))
        self.gridLayout.addWidget(self.campo_tarefa, 0, 1, 1, 1)
        self.lista_tarefas = QtGui.QTableWidget(self.qtPrincipalForm)
        self.lista_tarefas.setGeometry(QtCore.QRect(10, 150, 621, 371))
        self.lista_tarefas.setObjectName(_fromUtf8("lista_tarefas"))
        self.lista_tarefas.setColumnCount(0)
        self.lista_tarefas.setRowCount(0)
        self.lista_tarefas.verticalHeader().setVisible(False)
        self.campo_id_tarefa = QtGui.QLineEdit(self.qtPrincipalForm)
        self.campo_id_tarefa.setEnabled(False)
        self.campo_id_tarefa.setGeometry(QtCore.QRect(20, 70, 50, 20))
        self.campo_id_tarefa.setMouseTracking(True)
        self.campo_id_tarefa.setFrame(False)
        self.campo_id_tarefa.setEchoMode(QtGui.QLineEdit.NoEcho)
        self.campo_id_tarefa.setDragEnabled(False)
        self.campo_id_tarefa.setReadOnly(True)
        self.campo_id_tarefa.setPlaceholderText(_fromUtf8(""))
        self.campo_id_tarefa.setObjectName(_fromUtf8("campo_id_tarefa"))
        self.btn_excluir = QtGui.QPushButton(self.qtPrincipalForm)
        self.btn_excluir.setEnabled(False)
        self.btn_excluir.setGeometry(QtCore.QRect(550, 80, 75, 23))
        self.btn_excluir.setObjectName(_fromUtf8("btn_excluir"))
        qtPrincipal.setCentralWidget(self.qtPrincipalForm)
        self.menubar = QtGui.QMenuBar(qtPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 25))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSobre = QtGui.QMenu(self.menubar)
        self.menuSobre.setObjectName(_fromUtf8("menuSobre"))
        self.menuSicronizar = QtGui.QMenu(self.menubar)
        self.menuSicronizar.setObjectName(_fromUtf8("menuSicronizar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        qtPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(qtPrincipal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        qtPrincipal.setStatusBar(self.statusbar)
        self.actionDeletar_Banco = QtGui.QAction(qtPrincipal)
        self.actionDeletar_Banco.setObjectName(_fromUtf8("actionDeletar_Banco"))
        self.actionSincronizar = QtGui.QAction(qtPrincipal)
        self.actionSincronizar.setObjectName(_fromUtf8("actionSincronizar"))
        self.actionSair = QtGui.QAction(qtPrincipal)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionSobre = QtGui.QAction(qtPrincipal)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        self.menuSobre.addAction(self.actionSobre)
        self.menuSicronizar.addAction(self.actionSincronizar)
        self.menuArquivo.addAction(self.actionSair)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuSicronizar.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(qtPrincipal)
        QtCore.QObject.connect(self.btn_salvar_dados, QtCore.SIGNAL(_fromUtf8("clicked()")), qtPrincipal.salvar_dados)
        QtCore.QObject.connect(self.actionSair, QtCore.SIGNAL(_fromUtf8("triggered()")), qtPrincipal.close)
        QtCore.QObject.connect(self.actionSobre, QtCore.SIGNAL(_fromUtf8("triggered()")), qtPrincipal.abrir_sobre)
        QtCore.QObject.connect(self.actionSincronizar, QtCore.SIGNAL(_fromUtf8("triggered()")), qtPrincipal.abrir_sincronizacao)
        QtCore.QObject.connect(self.btn_excluir, QtCore.SIGNAL(_fromUtf8("clicked()")), qtPrincipal.excluir_dados)
        QtCore.QMetaObject.connectSlotsByName(qtPrincipal)
        qtPrincipal.setTabOrder(self.campo_tarefa, self.campo_data_tarefa)
        qtPrincipal.setTabOrder(self.campo_data_tarefa, self.campo_hora_inicio)
        qtPrincipal.setTabOrder(self.campo_hora_inicio, self.campo_hora_final)
        qtPrincipal.setTabOrder(self.campo_hora_final, self.campo_descricao_tarefa)
        qtPrincipal.setTabOrder(self.campo_descricao_tarefa, self.btn_salvar_dados)
        qtPrincipal.setTabOrder(self.btn_salvar_dados, self.btn_excluir)
        qtPrincipal.setTabOrder(self.btn_excluir, self.campo_total_horas)
        qtPrincipal.setTabOrder(self.campo_total_horas, self.lista_tarefas)
        qtPrincipal.setTabOrder(self.lista_tarefas, self.campo_id_tarefa)

    def retranslateUi(self, qtPrincipal):
        qtPrincipal.setWindowTitle(_translate("qtPrincipal", "Principal", None))
        self.label_hora_final.setText(_translate("qtPrincipal", "Hora Final", None))
        self.label_total.setText(_translate("qtPrincipal", "Total Horas", None))
        self.label_hora_inicio.setText(_translate("qtPrincipal", "Hora Inicio", None))
        self.btn_salvar_dados.setText(_translate("qtPrincipal", "Salvar", None))
        self.label_descricao_tarefa.setText(_translate("qtPrincipal", "Descrição da Tarefa", None))
        self.label_id_tarefa.setText(_translate("qtPrincipal", "Tarefa", None))
        self.campo_data_tarefa.setDisplayFormat(_translate("qtPrincipal", "dd/MM/yyyy", None))
        self.label_data_tarefa.setText(_translate("qtPrincipal", "Data Tarefa", None))
        self.campo_tarefa.setInputMask(_translate("qtPrincipal", "000000000; ", None))
        self.btn_excluir.setText(_translate("qtPrincipal", "Excluir", None))
        self.menuSobre.setTitle(_translate("qtPrincipal", "Sobre", None))
        self.menuSicronizar.setTitle(_translate("qtPrincipal", "Sincronizar", None))
        self.menuArquivo.setTitle(_translate("qtPrincipal", "Arquivo", None))
        self.actionDeletar_Banco.setText(_translate("qtPrincipal", "Deletar Banco", None))
        self.actionSincronizar.setText(_translate("qtPrincipal", "Sincronizar", None))
        self.actionSair.setText(_translate("qtPrincipal", "Sair", None))
        self.actionSair.setShortcut(_translate("qtPrincipal", "Ctrl+F4", None))
        self.actionSobre.setText(_translate("qtPrincipal", "Sobre", None))
