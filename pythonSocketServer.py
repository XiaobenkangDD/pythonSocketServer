# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pythonSocketServer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 911, 441))
        self.textEdit.setObjectName("textEdit")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(670, 10, 75, 23))
        self.stopButton.setObjectName("stopButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(800, 10, 75, 23))
        self.exitButton.setObjectName("exitButton")
        self.startListenButton = QtWidgets.QPushButton(self.centralwidget)
        self.startListenButton.setGeometry(QtCore.QRect(550, 10, 75, 23))
        self.startListenButton.setObjectName("startListenButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stopButton.setText(_translate("MainWindow", "暂停"))
        self.exitButton.setText(_translate("MainWindow", "退出"))
        self.startListenButton.setText(_translate("MainWindow", "开始监听"))

    def showMessageInWindow(self,message):
        str = self.textEdit.toPlainText()
        str = str + message + "\r\n"
        self.textEdit.setPlainText(str)



